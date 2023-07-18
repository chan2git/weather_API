### Import requests module
import requests                                                                                       

### Enter your OpenWeatherMap API Key before running this script. See Footnotes (Line 60)
API_KEY = "<Enter your API Key Here>"

### Prompts user to enter name of city
city = input("Enter a city name: ")

### Establishes the API call URL and passes the city name and API key to appropriate position in the URL, and submits a get request
request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
response = requests.get(request_url)


### Checks to see if the API call response returns a 200 OK code, otherwise display an error
### Apply the json() function to response, and stores in var called data
if response.status_code == 200:
    data = response.json()

    # Formats the results
    # Access the desired specific information in data, and stores in the corresponding named variables
    # Prints the results to the user
    print(" ")                                                                             
    print("===========================")

    weather = data['weather'][0]['description']
    print(f"Weather: {weather}")

    temp = data['main']['temp']
    print(f"Temperature: {temp}F")

    humidity = data['main']['humidity']
    print(f"Humidity: {humidity}%")

    print("===========================")

else:
    print("Error. Please check your input, API key, or try again later.")





################################################ FOOTNOTES ################################################

#############################
# Version:    1.00          #
# Date:       07/17/2023    #
# Coder:      CH @chan2git  #
#############################

################################################
# Learning Resources/Guides                    #
# https://www.youtube.com/watch?v=Oz3W-LKfafE  #
#                                              #
# API documentation:                           #
# https://openweathermap.org/current#data      #
################################################

# Sign up at https://openweathermap.org/ to get your own API Key, and use it in line 5
