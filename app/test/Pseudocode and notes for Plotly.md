## Pseudocode and notes for Plotley

### to dos
make starter file
* com  import streamlit into test_
* inp - get some starting data (got churn_clean. get another one )
* com - file select page
* inp - write pseudo code
* TEST - does this model even know how to do streamlit graphs? gotta test this pretty quickly!





### Pseudo code and notes

1) show entry screen
2) go to file select screen
3) Select file
    should now be able to show all of the summary stats
        includes dataframe viewer, df.info, df.summary, 
    need column spec with data types
    branch to graphing page (or other EDA page?)
Note Do we run all of the langchain stuff at this point? Thinking yes
5) graphing page (see note above)
    input - need the column and datatype spec in the system state
    prompt templates
        system (SM) and human messages (HM)
        Human Message -> plot x vs y using box plot
        HM -> filter the dataset
        SM -> you are a code generator for streamlit graphs. Given a dataframe, df with the following columns and datatypes, you will be asked to generate python code using streamlit, pandas, and plotting in Matplotlib.