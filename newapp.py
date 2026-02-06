# app.py
import streamlit as st

# Page config
st.set_page_config(
    page_title="My Awesome App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern CSS Styling
st.markdown(
    """
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea, #764ba2);
        font-family: 'Segoe UI', sans-serif;
        color: white;
    }

    /* Main title */
    h1 {
        text-align: center;
        font-size: 42px;
        color: #ffffff;
        font-weight: bold;
        margin-bottom: 30px;
    }

    /* Card container */
    .card {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(12px);
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        color: white;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #141e30, #243b55);
        color: white;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #ff512f, #dd2476);
        color: white;
        border: none;
        border-radius: 12px;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #36d1dc, #5b86e5);
    }

    /* Input boxes */
    input, textarea {
        border-radius: 10px !important;
    }

    /* Success message */
    .stSuccess {
        background-color: rgba(0,255,150,0.2);
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1>🚀 Welcome to My Modern App</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Home Page
if page == "Home":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🧮 Interactive Calculator")

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
    st.subheader("📖 About This App")
    st.write(
        """
        This is a modern web application built using **Streamlit**.
        
        ✔ Beautiful modern UI  
        ✔ Interactive calculator  
        ✔ Multi-page navigation  
        ✔ CI/CD using Jenkins & GitHub  
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Page
elif page == "Contact":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📩 Contact Me")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if name and email and message:
            st.success("Message sent successfully! 🚀")
        else:
            st.error("Please fill all fields.")

    st.markdown('</div>', unsafe_allow_html=True)
