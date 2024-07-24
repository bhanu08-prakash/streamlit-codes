import streamlit as st
st.title("palindrome",anchor=False)

a = st.text_input(label="Enter the term number (n)")
if st.button("Submit"):
    b=a[::-1]
    if a==b:
        st.write("pal")
    else:

        st.write("not pal")    
