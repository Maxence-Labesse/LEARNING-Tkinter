import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image
import requests
import json

# First widget: global window
root = Tk()
root.title("Title")
root.iconbitmap("icon2.ico")
style = ttk.Style()
style.theme_use('clam')
root.geometry("600x100")

myLabel = Label(root, text="")
myLabel.grid(row=1, column=0, columnspan=2)

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=937E7911-4A52-4E84-8E32-4D1AAA95A07F

def ziplookup():
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

        global myLabel
        myLabel.grid_forget()
        myLabel = Label(root, text=city + " Air Quality: " + str(quality) + " (" + category + ")",
                        font="Helvetica", background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2)

        root.configure(background=weather_color)

    except Exception as e:
        api = "Error..."


zip = Entry(root)
zip.grid(row=0, column=0, stick=W + E + N + S)

zipButton = Button(root, text="Lookup Zipcode", command=ziplookup)
zipButton.grid(row=0, column=1, stick=W + E + N + S)

# Loop for dynamic screen
root.mainloop()
