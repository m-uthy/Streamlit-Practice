import streamlit as st 
st.checkbox("I am a Male")
st.radio("Select a gender", options= ["Male", "Female"])
st.selectbox("Select a gender", options=["Male", "Female"])
st.multiselect("Select a gender", options=["Male", "Female"])
st.button("Click me !!! 😒😒😒")
st.text_input("Enter Your Name: ", placeholder= " e.g Uthman Makanjuola")
st.text_area("Tell me about yourself: ", placeholder= "I am a ......")

st.text_input("Enter Your Password: ", type= 'password')
st.slider("Pick a range", 1, 5)
st.number_input("Enter your weight: " )



st.title("Streamlit Class")
st.header("Uthman")
st.subheader("My surname is Makanjuola")
st.write("I love Money")
st.divider()
st.text("Mr Sam complains about all the apps he uses")
st.markdown("### This is a Markdown, I love food")
st.success("What is success")
st.warning("stop shebe!!!!")
st.info(" Plum Weapons!!! ")
st.error("Try Again!!! ")
st.exception(ZeroDivisionError("Trying to divide by Zero"))