'''
The code in this streamlit script modifies the basic script 
we had for running a scenario
'''
import streamlit as st
from model import Experiment, multiple_replications

# #############################################################################
# MODIFICATION: We add in a title for our web app's page
st.title("Urgent care call centre")
###############################################################################

# set number of resources
n_operators = 13
n_nurses = 9

# set chance of nurse
chance_callback = 0.4

# set number of replications
n_reps = 5

# create experiment
exp = Experiment(n_operators=n_operators, n_nurses=n_nurses,
                 chance_callback=chance_callback)

###############################################################################
# MODIFICATION: A user must press a streamlit button to run the model
if st.button("Run simulation"):

    # run multiple replications of experment
    results = multiple_replications(exp, n_reps=n_reps)

    # show results
    st.dataframe(results.describe())
################################################################################

