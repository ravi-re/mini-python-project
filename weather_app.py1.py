# import streamlit for creating the web app
import streamlit as st

# import matplotlib for plotting bar chart
import matplotlib.pyplot as plt

# set page layout to wide
st.set_page_config(layout="wide")

# title of the app
st.title("Weather Alert App")

# text input for temperature (string input)
temp_input = st.text_input("Enter temperature in Celsius")

# dropdown for weather selection
weather = st.selectbox(
    "Select weather",
    ["Sunny", "Rain", "Snow", "Storm", "Fog"]
)

# ---------------- BACKGROUND EFFECTS ----------------

if weather == "Rain":
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://i.imgur.com/UJ4QK0K.gif");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

elif weather == "Snow":
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://i.imgur.com/5bYQFqk.gif");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

elif weather == "Storm":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #1a1a1a;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

elif weather == "Fog":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #bfbfbf;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

elif weather == "Sunny":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #fff3b0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------------- BUTTON LOGIC ----------------

if st.button("Check Weather"):

    # convert temperature input to float FIRST
    try:
        temp = float(temp_input)
    except:
        st.error("Please enter a valid number for temperature")
        st.stop()

    # check for unrealistic temperature values
    if temp < -50 or temp > 60:
        st.error("Temperature is not realistic")
        st.stop()

    # ---------------- LOGICAL WEATHER ERRORS ----------------

    if weather == "Sunny" and temp <= 0:
        st.error("Sunny weather cannot occur at freezing temperature")
        st.stop()

    if weather == "Rain" and (temp < -2 or temp > 35):
        st.error("Rain cannot occur at this temperature")
        st.stop()

    if weather == "Snow" and temp > 5:
        st.error("Snow cannot occur above 5°C")
        st.stop()

    if weather == "Storm" and temp < 5:
        st.error("Storm cannot occur at very low temperature")
        st.stop()

    if weather == "Fog" and (temp < -5 or temp > 20):
        st.error("Fog cannot occur at this temperature")
        st.stop()

    # ---------------- ALERT OUTPUT ----------------

    if weather == "Storm":
        st.error("Storm alert! Stay indoors")

    elif temp >= 40:
        st.error("Extreme heat alert")

    elif temp <= 0:
        st.warning("Freezing weather")

    else:
        st.success("Weather is normal")

    # ---------------- BAR CHART ----------------

    st.subheader("Temperature Chart")

    fig, ax = plt.subplots()
    ax.bar(["Temperature"], [temp])
    ax.set_ylabel("Celsius")

    st.pyplot(fig)