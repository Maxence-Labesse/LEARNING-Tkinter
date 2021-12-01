"""
Get weather by zipcode using Airnow website API
"""
import tkinter.ttk as ttk
from tkinter import *

import requests
import json

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')
root.geometry("400x50")

#
weather_label = Label(root, text="")


def ziplookup():
    """
    when button is pressed, get weather from API for filled zipcode
    """
    global weather_label

    api_request = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=937E7911-4A52-4E84-8E32-4D1AAA95A07F"
    )
    try:
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]["Category"]["Name"]

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "##660000"

        # display weather with related color
        weather_label.grid_forget()
        weather_label = Label(root, text=city + " Air Quality: " + str(quality) + " (" + category + ")",
                              font="Helvetica", background=weather_color)
        weather_label.grid(row=1, column=0, columnspan=2)
        root.configure(background=weather_color)

    except Exception as e:
        api = "Error..."


# Zipcode entry
zip = Entry(root)
zip.grid(row=0, column=0, stick=W + E + N + S)

# Submit button
zipButton = Button(root, text="Lookup Zipcode", command=ziplookup)
zipButton.grid(row=0, column=1, stick=W + E + N + S)

# Loop for dynamic screen
root.mainloop()
