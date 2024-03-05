import streamlit as st




st.header('Dynamic URLs')

query_params = st.query_params

if 'id' not in query_params:
    query_params['id'] = 1



st.write(query_params)


st.write("Dashboard for Person with ID: ", query_params['id'])


