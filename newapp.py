# app.py
import streamlit as st

# Page config
st.set_page_config(
    page_title="My Awesome App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Styling
st.markdown(
    """
    <style>
    /* Main background */
    body {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', sans-serif;
    }
    /* Card style */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    /* Heading */
    h1 {
        color: #0d6efd;
        text-align: center;
    }
    /* Buttons */
    .stButton>button {
        background-color: #0d6efd;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1>🚀 Welcome to My Awesome App</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Home Page
if page == "Home":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Interactive Calculator")
    num1 = st.number_input("Enter first number", value=0)
    num2 = st.number_input("Enter second number", value=0)
    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])
    if st.button("Calculate"):
        if operation == "Add":
            st.success(f"Result: {num1 + num2}")
        elif operation == "Subtract":
            st.success(f"Result: {num1 - num2}")
        elif operation == "Multiply":
            st.success(f"Result: {num1 * num2}")
        elif operation == "Divide":
            if num2 != 0:
                st.success(f"Result: {num1 / num2}")
            else:
                st.error("Cannot divide by zero!")
    st.markdown('</div>', unsafe_allow_html=True)

# About Page
elif page == "About":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("About This App")
    st.write(
        """
        This is a modern web application made with **Streamlit**.
        - Single Python file
        - Responsive UI
        - Interactive features
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Page
elif page == "Contact":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Contact Me")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Send"):
        if name and email and message:
            st.success("Message sent successfully! 🚀")
        else:
            st.error("Please fill all fields.")
    st.markdown('</div>', unsafe_allow_html=True)
