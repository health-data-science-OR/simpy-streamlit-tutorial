'''
The code in this streamlit provides a way to add multiple simulation control
to the simulation model.
'''
import streamlit as st
import os
import pandas as pd

from model import Experiment, run_all_experiments, experiment_summary_frame

INFO_1 = '**Execute multiple experiments in a batch**'
INFO_2 = '### Upload a CSV containing input parameters.'
    
def create_experiments(df_experiments):
    '''
    Returns dictionary of Experiment objects based on contents of a dataframe

    Params:
    ------
    df_experiments: pandas.DataFrame
        Dataframe of experiments. First two columns are id, name followed by 
        variable names.  No fixed width

    Returns:
    --------
    dict
    '''
    experiments = {}
    
    # experiment input parameter dictionary
    exp_dict = df_experiments[df_experiments.columns[1:]].T.to_dict()
    # names of experiments
    exp_names = df_experiments[df_experiments.columns[0]].T.to_list()
    
    # loop through params and create Experiment objects.
    for name, params in zip(exp_names, exp_dict.values()):
        experiments[name] = Experiment(**params)
    
    return experiments

# We add in a title for our web app's page
st.title("Urgent care call centre")

# show the introductory markdown
st.markdown(INFO_1)
st.markdown(INFO_2)

# A user adds an Experiment to the dataframe

uploaded_file = st.file_uploader("Choose a file")
df_results = pd.DataFrame()
if uploaded_file is not None:
    # assumes CSV
    df_experiments = pd.read_csv(uploaded_file, index_col=0)
    st.write('**Loaded Experiments**')
    st.table(df_experiments)

    # loop through scenarios, create and run model
    n_reps = st.slider('Replications', 3, 30, 5, step=1)

    if st.button('Execute Experiments'):
        # create the batch of experiments based on upload
        experiments = create_experiments(df_experiments) 
        print(experiments)
        with st.spinner('Running all experiments'):
            
            results = run_all_experiments(experiments, n_reps=n_reps)
            st.success('Done!')
            
            # combine results into a single summary table.
            df_results = experiment_summary_frame(results)
            # display in the app via table
            st.table(df_results.round(2))

