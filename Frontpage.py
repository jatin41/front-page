import streamlit as st

def main():
    
    st.markdown("<h1 style='text-align: center; font-size: 48px; color:White'>DiseaseDetective: Uncovering Your Health Risks 🩺</h1>", unsafe_allow_html=True)
    
    st.header("Welcome to Disease Detective")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image('https://cdn-icons-png.flaticon.com/512/3774/3774299.png')
    with col2:
        st.write(
            """
            We are committed to helping you stay on top of your health.Our disease predictor website provides personalized risk assessments for various illnesses using an advanced algorithm that analyzes your age, gender, and medical history. We use the latest medical research and data to provide accurate risk assessments that empower you to take control of your well-being. Our user-friendly platform is accessible to everyone and allows you to proactively reduce your risk of developing certain diseases. Take charge of your health and start monitoring your health risks today with our reliable and easy-to-use website.
            """
        )
    
    st.markdown(
    """
    <div style='text-align: center;font-size: 24px;'>
        <a href='http://localhost:8502' target='_blank'>Start here</a>
    </div>
    """,
    unsafe_allow_html=True
)


if __name__ == '__main__':
    main()
