import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('rock_vs_mine_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set page config
st.set_page_config(page_title="Rock vs Mine Predictor", layout="wide")

# Custom CSS for background
page_bg = """
<style>
body {
    background-image: url("submarine.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# App content
st.title("Rock vs Mine Predictor")

# Input form
input_data = st.text_input(
    "Enter sonar data (exactly 60 numerical values, comma-separated):",
    placeholder="e.g., 0.03, 0.12, 0.45, ... (60 values)"
)

# Prediction button
if st.button("Predict"):
    if input_data:
        try:
            # Convert the input string to a numpy array
            input_data_list = list(map(float, input_data.strip().split(',')))

            if len(input_data_list) != 60:
                st.error("Input must contain exactly 60 numerical values.")
            else:
                input_data_reshaped = np.array(input_data_list).reshape(1, -1)
                prediction = model.predict(input_data_reshaped)

                # Display the result and image
                if prediction[0] == 'R':
                    st.write("Prediction: **No need to worry<br>This is rock**", unsafe_allow_html=True)
                    st.image("rock.jpg", caption="This is a rock.", use_container_width=True)
                else:
                    st.write("Prediction: **Be cautious<br>This is mine**", unsafe_allow_html=True)
                    st.image("mine.jpg", caption="This is a mine.", use_container_width=True)
        except ValueError:
            st.error("Invalid input format. Please enter valid numerical values separated by commas.")
    else:
        st.error("Please enter the sonar data before clicking Predict.")
