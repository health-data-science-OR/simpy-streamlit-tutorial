'''
The code in this streamlit script adds in a basic plotly 
chart to display a histogram of replications
'''
import streamlit as st
import plotly.express as px
from model import Experiment, multiple_replications

INTRO_FILE = './resources/model_info.md'

def read_file_contents(file_name):
    ''''
    Read the contents of a file.

    Params:
    ------
    file_name: str
        Path to file.

    Returns:
    -------
    str
    '''
    with open(file_name) as f:
        return f.read()
    

###################################################################################
# MODIFICATION: code to create plotly histogram
def create_hist(results, column, value_label, marginal='box'):
    '''
    Create and return a plotly express histogram of
    the results column
    '''
    fig = px.histogram(results[column], labels={'value':value_label},
                       marginal=marginal)
    # hide legend
    fig.update(layout_showlegend=False)
    
    return fig
##################################################################################


##################################################################################
# MODIFICATION: update to wide page settings to help display results side by side
st.set_page_config(
     page_title="Urgent Care Sim App",
     layout="wide",
     initial_sidebar_state="expanded",
 )
#################################################################################

# We add in a title for our web app's page
st.title("Urgent care call centre")

# show the introductory markdown
st.markdown(read_file_contents(INTRO_FILE))

# side bar
with st.sidebar:

    # set number of resources
    n_operators = st.slider('Call operators', 1, 20, 13, step=1)
    n_nurses = st.slider('Nurses', 1, 15, 9, step=1)

    # set chance of nurse
    chance_callback = st.slider('Chance of nurse callback', 0.1, 1.0, 0.4,
                                step=0.05, help='Set the chance of a call back')

    # set number of replications
    n_reps = st.number_input("No. of replications", 100, 1_000, step=1)

# create experiment
exp = Experiment(n_operators=n_operators, n_nurses=n_nurses,
                 chance_callback=chance_callback)

# A user must press a streamlit button to run the model
if st.button("Run simulation"):

    #  add a spinner and then display success box
    with st.spinner('Simulating the urgent care system...'):
        # run multiple replications of experment
        results = multiple_replications(exp, n_reps=n_reps)#
    
    st.success('Done!')

    ############################################################################
    # MODIFICATION: create columns for histogram of the results
    col1, col2 = st.columns(2)
    with col1.expander('Tabular results', expanded=True):
        # show tabular results
        st.dataframe(results.describe())

    with col2.expander('Histogram', expanded=True):
    

        fig = create_hist(results, '01_mean_waiting_time', 
                          'Mean waiting time for operator')
     
        st.plotly_chart(fig, use_container_width=True)
        
     ############################################################################

    
    
    

