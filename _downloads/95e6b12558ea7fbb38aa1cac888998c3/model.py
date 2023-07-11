'''
A simple urgent care call centre model built in streamlit

This code is used as part of an introduction to simpy and streamlit
tutorial.

To use the model a script must import `Experiment` and the functions 
`single_run()` and/or `multiple_replications()`

'''
import numpy as np
import pandas as pd
import simpy
import itertools

# CONSTANTS AND MODULE LEVEL VARIABLES #########################################

# default resources
N_OPERATORS = 13

# number of nurses available
N_NURSES = 9

# default mean inter-arrival time (exp)
MEAN_IAT = 60 / 100

## default service time parameters (triangular)
CALL_LOW = 5.0
CALL_MODE = 7.0
CALL_HIGH = 10.0

# nurse distribution parameters (uniform and bernoulli)
NURSE_CALL_LOW = 10.0
NURSE_CALL_HIGH = 20.0
CHANCE_CALLBACK = 0.4

# Seeds for distributions (for repeatable single run)
ARRIVAL_SEED = 42
CALL_SEED = 101
CALLBACK_SEED = 1966
NURSE_SEED = 2020

# Boolean switch to simulation results as the model runs
TRACE = False

# run variables
RESULTS_COLLECTION_PERIOD = 1000

# DISTRIBUTION CLASSES #########################################################

class Bernoulli():
    '''
    Convenience class for the Bernoulli distribution.
    packages up distribution parameters, seed and random generator.
    
    Use the Bernoulli distribution to sample success or failure.
    '''
    def __init__(self, p, random_seed=None):
        '''
        Constructor
        
        Params:
        ------
        p: float
            probability of drawing a 1
        
        random_seed: int, optional (default=None)
            A random seed to reproduce samples.  If set to none then a unique
            sample is created.
        '''
        self.rand = np.random.default_rng(seed=random_seed)
        self.p = p
        
    def sample(self, size=None):
        '''
        Generate a sample from the exponential distribution
        
        Params:
        -------
        size: int, optional (default=None)
            the number of samples to return.  If size=None then a single
            sample is returned.
        
        Returns:
        -------
        float or np.ndarray (if size >=1)
        '''
        return self.rand.binomial(n=1, p=self.p, size=size)

class Uniform():
    '''
    Convenience class for the Uniform distribution.
    packages up distribution parameters, seed and random generator.
    '''
    def __init__(self, low, high, random_seed=None):
        '''
        Constructor
        
        Params:
        ------
        low: float
            lower range of the uniform
            
        high: float
            upper range of the uniform
        
        random_seed: int, optional (default=None)
            A random seed to reproduce samples.  If set to none then a unique
            sample is created.
        '''
        self.rand = np.random.default_rng(seed=random_seed)
        self.low = low
        self.high = high
        
    def sample(self, size=None):
        '''
        Generate a sample from the exponential distribution
        
        Params:
        -------
        size: int, optional (default=None)
            the number of samples to return.  If size=None then a single
            sample is returned.
            
        Returns:
        -------
        float or np.ndarray (if size >=1)
        '''
        return self.rand.uniform(low=self.low, high=self.high, size=size)

class Triangular():
    '''
    Convenience class for the triangular distribution.
    packages up distribution parameters, seed and random generator.
    '''
    def __init__(self, low, mode, high, random_seed=None):
        '''
        Constructor. Accepts and stores parameters of the triangular dist
        and a random seed.
        
        Params:
        ------
        low: float
            The smallest values that can be sampled
            
        mode: float
            The most frequently sample value
            
        high: float
            The highest value that can be sampled
        
        random_seed: int, optional (default=None)
            Used with params to create a series of repeatable samples.
        '''
        self.rand = np.random.default_rng(seed=random_seed)
        self.low = low
        self.high = high
        self.mode = mode
        
    def sample(self, size=None):
        '''
        Generate one or more samples from the triangular distribution
        
        Params:
        --------
        size: int
            the number of samples to return.  If size=None then a single
            sample is returned.
            
        Returns:
        -------
        float or np.ndarray (if size >=1)
        '''
        return self.rand.triangular(self.low, self.mode, self.high, size=size)

class Exponential():
    '''
    Convenience class for the exponential distribution.
    packages up distribution parameters, seed and random generator.
    '''
    def __init__(self, mean, random_seed=None):
        '''
        Constructor
        
        Params:
        ------
        mean: float
            The mean of the exponential distribution
        
        random_seed: int, optional (default=None)
            A random seed to reproduce samples.  If set to none then a unique
            sample is created.
        '''
        self.rand = np.random.default_rng(seed=random_seed)
        self.mean = mean
        
    def sample(self, size=None):
        '''
        Generate a sample from the exponential distribution
        
        Params:
        -------
        size: int, optional (default=None)
            the number of samples to return.  If size=None then a single
            sample is returned.
            
        Returns:
        -------
        float or np.ndarray (if size >=1)
        '''
        return self.rand.exponential(self.mean, size=size)


# EXPERIMENT CLASS ############################################################

class Experiment:
    '''
    Parameter class for 111 simulation model
    '''
    def __init__(self, n_operators=N_OPERATORS, n_nurses=N_NURSES, 
                 mean_iat=MEAN_IAT, call_low=CALL_LOW, call_mode=CALL_MODE, 
                 call_high=CALL_HIGH, chance_callback=CHANCE_CALLBACK, 
                 nurse_call_low=NURSE_CALL_LOW, nurse_call_high=NURSE_CALL_HIGH,
                 arrival_seed=None, call_seed=None,
                 callback_seed=None, nurse_seed=None):
        '''
        The init method sets up our defaults, resource counts, distributions
        and result collection objects.
        '''
        # no. resources
        self.n_operators = n_operators
        self.n_nurses = n_nurses

        # create distribution objects
        self.arrival_dist = Exponential(mean_iat, random_seed=arrival_seed)
        self.call_dist = Triangular(call_low, call_mode, call_high, 
                                    random_seed=call_seed)
        
        self.callback_dist = Bernoulli(chance_callback, 
                                       random_seed=callback_seed)
        
        self.nurse_dist = Uniform(nurse_call_low, nurse_call_high, 
                                  random_seed=nurse_seed)

        # resources
        # these variable are placeholders. 
        self.operators = None
        self.nurses = None
        
        # initialise results to zero
        self.init_results_variables()
        
    def init_results_variables(self):
        '''
        Initialise all of the experiment variables used in results 
        collection.  This method is called at the start of each run
        of the model
        '''
        # variable used to store results of experiment
        self.results = {}
        self.results['waiting_times'] = []
        
        # total operator usage time for utilisation calculation.
        self.results['total_call_duration'] = 0.0

        # nurse sub process results collection
        self.results['nurse_waiting_times'] = []
        self.results['total_nurse_call_duration'] = 0.0

# SIMPY MODEL LOGIC #########################################################

def trace(msg):
    '''
    Turing printing of events on and off.
    
    Params:
    -------
    msg: str
        string to print to screen.
    '''
    if TRACE:
        print(msg)

def service(identifier, args, env):
    '''
    simulates the service process for a call operator 
    and nurse.

    1. request and wait for a call operator
    2. phone triage (triangular)
    3. check if patient requires nurse callback? (bernoulli)
    4. request and wait for nurse practitioner
    5. nurse consultation (uniform)
    6. Exit system

    Params:
    ------
    identifier: int 
        A unique identifer for this caller
        
    args: Experiment
        The settings and input parameters for the current experiment
        
    env: simpy.Environment
        The current environent the simulation is running in
        We use this to pause and restart the process after a delay.
    
    '''
    # record the time that call entered the queue
    start_wait = env.now
    
    # request an operator
    with args.operators.request() as req:
        yield req
        
        # record the waiting time for call to be answered
        waiting_time = env.now - start_wait
        
        # store the results for an experiment 
        args.results['waiting_times'].append(waiting_time)

        trace(f'operator answered call {identifier} at ' \
              + f'{env.now:.3f}')

        # the sample distribution is defined by the experiment.
        call_duration = args.call_dist.sample()       
        
        # schedule process to begin again after call_duration
        yield env.timeout(call_duration)
        
        # update the total call_duration 
        args.results['total_call_duration'] += call_duration
        
        # print out information for patient.
        trace(f'call {identifier} ended {env.now:.3f}; ' \
              + f'waiting time was {waiting_time:.3f}')
        
    # nurse callback
    callback_patient = args.callback_dist.sample()

    if callback_patient:
        trace(f'Patient {identifier} waiting for nurse call back')

        start_nurse_wait = env.now

        # request a nurse
        with args.nurses.request() as req:
            yield req

            # record the waiting time for nurse call back
            nurse_waiting_time = env.now - start_nurse_wait
            args.results['nurse_waiting_times'].append(nurse_waiting_time)

            # sample nurse the duration of the nurse consultation
            nurse_call_duration = args.nurse_dist.sample()       

            trace(f'nurse called back patient {identifier} at ' \
              + f'{env.now:.3f}')

            # schedule process to begin again after call duration
            yield env.timeout(nurse_call_duration)

            args.results['total_nurse_call_duration'] += nurse_call_duration

            trace(f'nurse consultation for {identifier}' \
              + f' competed at {env.now:.3f}')

def arrivals_generator(env, args):
    '''
    IAT is exponentially distributed

    Parameters:
    ------
    env: simpy.Environment
        The simpy environment for the simulation

    args: Experiment
        The settings and input parameters for the simulation.
    '''

    # use itertools as it provides an infinite loop 
    # with a counter variable that we can use for unique Ids
    for caller_count in itertools.count(start=1):

        # the sample distribution is defined by the experiment.
        inter_arrival_time = args.arrival_dist.sample()
        yield env.timeout(inter_arrival_time)

        trace(f'call arrives at: {env.now:.3f}')

        # we pass the experiment to the service function
        env.process(service(caller_count, args, env))

#  MODEL WRAPPER FUNCTIONS ##################################################

def single_run(experiment, rc_period=RESULTS_COLLECTION_PERIOD):
    '''
    Perform a single run of the model and return the results
    
    Parameters:
    -----------
    
    experiment: Experiment
        The experiment/paramaters to use with model

    rc_period: float, optional (default=RESULTS_COLLECTION_PERIOD)
        Model run length.
    '''
    # results dictionary.  Each KPI is a new entry.
    run_results = {}
    
    # reset all results variables to zero and empty
    experiment.init_results_variables()
    
    # environment is (re)created inside single run
    env = simpy.Environment()

    # we create simpy resources here - this has to be after we
    # create the simpy environment object.
    experiment.operators = simpy.Resource(env, capacity=experiment.n_operators)
    experiment.nurses = simpy.Resource(env, capacity=experiment.n_nurses)
    
    # we pass the experiment to the arrivals generator
    env.process(arrivals_generator(env, experiment))
    env.run(until=rc_period)

    # end of run results: calculate mean waiting time
    run_results['01_mean_waiting_time'] = \
        np.mean(experiment.results['waiting_times'])
    
    # end of run results: calculate mean operator utilisation
    run_results['02_operator_util'] = \
        (experiment.results['total_call_duration'] \
         / (rc_period * experiment.n_operators)) * 100.0
    
    # end of run results: nurse waiting time
    run_results['03_mean_nurse_waiting_time'] = \
        np.mean(experiment.results['nurse_waiting_times'])
    
    # end of run results: calculate mean nurse utilisation
    run_results['04_nurse_util'] = \
        (experiment.results['total_nurse_call_duration'] \
         / (rc_period * experiment.n_nurses)) * 100.0
    
    # return the results from the run of the model
    return run_results

def multiple_replications(experiment, 
                          rc_period=RESULTS_COLLECTION_PERIOD,
                          n_reps=5):
    '''
    Perform multiple replications of the model.
    
    Params:
    ------
    experiment: Experiment
        The experiment/paramaters to use with model
    
    rc_period: float, optional (default=DEFAULT_RESULTS_COLLECTION_PERIOD)
        results collection period.  
        the number of minutes to run the model to collect results

    n_reps: int, optional (default=5)
        Number of independent replications to run.
        
    Returns:
    --------
    pandas.DataFrame
    '''

    # loop over single run to generate results dicts in a python list.
    results = [single_run(experiment, rc_period) for rep in range(n_reps)]
        
    # format and return results in a dataframe
    df_results = pd.DataFrame(results)
    df_results.index = np.arange(1, len(df_results)+1)
    df_results.index.name = 'rep'
    return df_results

# Support for running batch experiments

def run_all_experiments(experiments, rc_period=RESULTS_COLLECTION_PERIOD,
                        n_reps=5):
    '''
    Run each of the scenarios for a specified results
    collection period and replications.
    
    Params:
    ------
    experiments: dict
        dictionary of Experiment objects
        
    rc_period: float
        model run length
    
    '''
    print('Model experiments:')
    print(f'No. experiments to execute = {len(experiments)}\n')

    experiment_results = {}
    for exp_name, experiment in experiments.items():
        
        print(f'Running {exp_name}', end=' => ')
        results = multiple_replications(experiment, rc_period, n_reps)
        print('done.\n')
        
        #save the results
        experiment_results[exp_name] = results
    
    print('All experiments are complete.')
    
    # format thje results
    return experiment_results

def experiment_summary_frame(experiment_results):
    '''
    Mean results for each performance measure by experiment
    
    Parameters:
    ----------
    experiment_results: dict
        dictionary of replications.  
        Key identifies the performance measure
        
    Returns:
    -------
    pd.DataFrame
    '''
    columns = []
    summary = pd.DataFrame()
    for sc_name, replications in experiment_results.items():
        summary = pd.concat([summary, replications.mean()], axis=1)
        columns.append(sc_name)

    summary.columns = columns
    return summary
                    