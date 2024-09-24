import streamlit as st

from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1,col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("https://via.placeholder.com/150")
with col2 :
    st.title("Arnaud Yilmaz", anchor=False)
    st.write(
        "Junior Data Scientist"
    )
    if st.button("✉️Contact Me"):
        show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.subheader("Experience & Qualifications")
st.write(
    """
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBI, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)