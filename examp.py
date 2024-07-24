import streamlit as st
st.set_page_config(page_icon="",page_title="bhanu's portifolio",)
st.title("GALAM BHANU PRAKASH", anchor=False)
st.subheader("WEB DEVOLOPPER", anchor=False)
with st.container(border=True):
    st.info("I am vit student")
col1,col2,col3=st.columns(3)
with col1:
   with st.expander(label="BTECH",expanded=True):

        st.info("BHIMAVARAM VIT COLLEGE")
    
with col2:
   with st.expander(label="DIPLAMA",expanded=True):
        st.warning("GUDLAVALLERU")
with col3:
    with st.expander(label="SSC",expanded=True):
        st.error("VELPUR")
    

