'''
The code in this streamlit script modifies the basic script 
we had for running a scenario
'''
import streamlit as st
from model import Experiment, multiple_replications

# We add in a title for our web app's page
st.title("Urgent care call centre")

# ##############################################################################
# MODIFICATION: side bar

with st.sidebar:

    # set number of resources
    n_operators = st.slider('Call operators', 1, 20, 13, step=1)
    n_nurses = st.slider('Nurses', 1, 15, 9, step=1)

    # set chance of nurse
    chance_callback = st.slider('Chance of nurse callback', 0.1, 1.0, 0.4,
                                step=0.05, help='Set the chance of a call back')

    # set number of replications
    n_reps = st.slider("No. of replications", 5, 100, step=1)

################################################################################

# create experiment
exp = Experiment(n_operators=n_operators, n_nurses=n_nurses,
                 chance_callback=chance_callback)

# A user must press a streamlit button to run the model
if st.button("Run simulation"):

    # ##########################################################################
    # MODIFICATION: add a spinner and then display success box
    with st.spinner('Simulating the urgent care system...'):
        # run multiple replications of experment
        results = multiple_replications(exp, n_reps=n_reps)#
    
    st.success('Done!')
    ###########################################################################

    # show results
    st.dataframe(results.describe())

