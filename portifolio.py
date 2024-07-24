import streamlit as st

st.title("GALAM BHANU PRAKASH")

st.subheader("Welcome to my portfolio")
st.write("""
Hello! I am currently a 3rd-year student pursuing my Bachelor's degree in Computer Science Engineering (CSE). I have a strong passion for technology and a keen interest in exploring the latest developments in the field.

Throughout my academic journey, I have developed a solid foundation in programming languages such as Java, Python, and C++, and I enjoy applying these skills to solve real-world problems. My coursework has equipped me with knowledge in data structures, algorithms, database management, and software engineering principles.

Beyond academics, I actively participate in extracurricular activities such as hackathons, coding competitions, and tech workshops. These experiences have not only honed my technical skills but also taught me the importance of teamwork, creativity, and continuous learning in the ever-evolving field of technology.

As I continue my journey in CSE, I am enthusiastic about gaining hands-on experience through internships and projects that allow me to apply my knowledge in practical scenarios. I am eager to contribute to the tech industry and make a meaningful impact through innovation and problem-solving.
""")
st.header("Projects")

# Example project 1
st.subheader("Project 1:Registration form and store data in firebase ")
st.subheader("Project 2:Telegram chatbot using API ")
st.header("Skills")

# List your skills
skills = ["Python","html","css","Basics of JAVA","Data structures","cpp"]
for skill in skills:
    st.write(f"- {skill}")
st.header("Contact Information")
st.write("""
Feel free to reach out to me:
- Email: 23pa5a0508@vishnu.edu.in
-contact:7702427832
         """)
