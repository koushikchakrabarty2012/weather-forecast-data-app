import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place :")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of Forecasted Days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
if place:
    try:
        # Get the temperature/sky data
        filtered_data = get_data(place, days)

        match option:
            case "Temperature":
                temperatures = [i["main"]["temp"] / 10 for i in filtered_data]
                type(temperatures)
                dates = [d["dt_txt"] for d in filtered_data]
                # Create a Temperature plot
                figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
                st.plotly_chart(figure)
            case "Sky":
                sky_conditions = [i["weather"][0]["main"] for i in filtered_data]
                print(sky_conditions)
                images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                          "Rain": "images/rain.png", "Snow": "images/snow.png"}
                image_paths = [images[i] for i in sky_conditions]
                st.image(image_paths, width=115)
    except KeyError:
        st.write("That Place does not exist")
