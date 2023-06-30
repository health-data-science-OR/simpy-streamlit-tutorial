'''
Script to complete a basic run of the model and display a table of
results and a plotly histogram in a streamlit app.

The model is imported from a pypi package 'treat_sim'

Full documentation and source code for `treat_sim` is available as 
* Jupyter Book: https://tommonks.github.io/treatment-centre-sim/
* github: https://github.com/TomMonks/treatment-centre-sim

A conda environment has been provided locally,but the model can be pip installed
`pip install treat_sim==1.0.0`
'''
from treat_sim.model import Scenario, multiple_replications
import streamlit as st
import plotly.express as px

INTRO_FILE = 'resources/overview.md'

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

##################################################################
# MODIFICATION: Function to create plotly histogram
def create_hist(results, column, value_label, marginal='box'):
    '''
    Create and return a plotly express histogram of
    the results column
    
    Params:
    -------
    results: pd.DataFrame
        Rows = replications, columns = KPIs
        
    column: str
        Name of column in results to use
        
    value_label: str
        X-axis label
        
    marginal: str, optional (default='box')
        An additional plot to render above the histogram
        options to try: box, violin, rug
        
    Returns:
    ------
    plotly.figure
        
    '''
    fig = px.histogram(results[column], labels={'value':value_label},
                       marginal=marginal)
    # hide legend
    fig.update(layout_showlegend=False)
    
    return fig
#####################################################################

# give the page a title
st.title('Treatment Centre Simulation Model')

# show the introductory markdown
st.markdown(read_file_contents(INTRO_FILE))

# create a sidebar for sliders
with st.sidebar:
    n_triage = st.slider('Triage bays', 1, 5, 1)
    n_exam = st.slider('Exam rooms', 1, 5, 3)
    n_cubicles_1 = st.slider('Non-Trauma Treatment cubicles', 1, 5, 1, 
                             help='Set the number of non trauma pathway '
                             + 'treatment cubicles')

    # examination mean
    exam_mean = st.slider('Mean examination time', 10.0, 45.0, 
                           16.0, 1.0)

    # runs
    replications = st.slider('No. replications', 1, 50, 10)

# Setup scenario using supplied variables
args = Scenario(n_triage=n_triage, n_exam=n_exam, n_cubicles_1=n_cubicles_1,
                exam_mean=exam_mean)

# Only execute model if a streamlit button is pressed.
if st.button('Simulate treatment centre'):

    # in this example run a single replication of the model.
    with st.spinner('Simulating the treatment centre...'):
        results = multiple_replications(args, n_reps=replications)

    st.success('Done!')

    # display results using st.table (or st.dataframe)
    st.table(results.mean().round(1))

    # ######################################################################
    # MODIFICATION: Show results of a KPI as histogram
    fig = create_hist(results, column='03a_examination_wait', 
                  value_label='Mean examination waiting time',
                  marginal='violin')

    st.plotly_chart(fig, use_container_width=True)
    ########################################################################