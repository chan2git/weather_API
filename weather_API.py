### Import modules, functions
import requests
import json
import datetime
from city_extract import print_us_cities, print_international_cities

### city.list.json (sourced from OpenWeatherMap) and imported functions are required to run menu option 3/4. Ensure files are in the same directory/repo
json_file_path = 'city.list.json'

### Enter your OpenWeatherMap API Key before running this script. See Footnotes (Line 60)
API_KEY = "<Enter your API Key Here>"


### Code block for menu
print("===========================")
print("Please select from the menu: ")
print("1. Current weather")
print("2. 5 day forecast")
print("3. List available US cities")
print("4. List available international cities")
print("")
print("Q. Quit")
print("===========================")
user_choice = input("Selection: ")


while True:
    if user_choice == "1":
        ### Prompts user to enter name of city
        city = input("Enter a city name: ")

        ### Establishes the API call URL and passes the city name and API key to appropriate position in the URL, and submits a get request, and stores the response in var response
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
            break

        else:
            print("Error. Please try again")
    elif user_choice == "2":
        ### Prompts user to enter name of city
        city = input("Enter a city name: ")

        ### Establishes the API call URL and passes the city name and API key to appropriate position in the URL, and submits a get request, and stores the response in var response
        request_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=imperial"
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

            # Identifies the unix timestamp provided by JSON results, and converts it to a human friendly format
            unix_timestamp1 = data['list'][0]['dt']
            datetime1 = datetime.datetime.fromtimestamp(unix_timestamp1)
            print(f"Date & Time: {datetime1}")

            weather1 = data['list'][0]['weather'][0]['description']
            print(f"Weather: {weather1}")

            temp1 = data['list'][0]['main']['temp']
            print(f"Temperature: {temp1}F")
          
            humidity1 = data['list'][0]['main']['humidity']
            print(f"Humidity: {humidity1}%")

            print("")

            unix_timestamp2 = data['list'][6]['dt']
            datetime2 = datetime.datetime.fromtimestamp(unix_timestamp2)
            print(f"Date & Time: {datetime2}")

            weather2 = data['list'][6]['weather'][0]['description']
            print(f"Weather: {weather2}")

            temp2 = data['list'][6]['main']['temp']
            print(f"Temperature: {temp2}F")
          
            humidity2 = data['list'][6]['main']['humidity']
            print(f"Humidity: {humidity2}%")

            print("")

            unix_timestamp3 = data['list'][14]['dt']
            datetime3 = datetime.datetime.fromtimestamp(unix_timestamp3)
            print(f"Date & Time: {datetime3}")

            weather3 = data['list'][14]['weather'][0]['description']
            print(f"Weather: {weather3}")

            temp3 = data['list'][14]['main']['temp']
            print(f"Temperature: {temp3}F")
          
            humidity3 = data['list'][14]['main']['humidity']
            print(f"Humidity: {humidity3}%")

            print("")

            unix_timestamp4 = data['list'][22]['dt']
            datetime4 = datetime.datetime.fromtimestamp(unix_timestamp4)
            print(f"Date & Time: {datetime4}")

            weather4 = data['list'][22]['weather'][0]['description']
            print(f"Weather: {weather4}")

            temp4 = data['list'][22]['main']['temp']
            print(f"Temperature: {temp4}F")
          
            humidity4 = data['list'][22]['main']['humidity']
            print(f"Humidity: {humidity4}%")

            print("")

            unix_timestamp5 = data['list'][30]['dt']
            datetime5 = datetime.datetime.fromtimestamp(unix_timestamp5)
            print(f"Date & Time: {datetime5}")

            weather5 = data['list'][30]['weather'][0]['description']
            print(f"Weather: {weather5}")

            temp5 = data['list'][30]['main']['temp']
            print(f"Temperature: {temp5}F")
          
            humidity5 = data['list'][30]['main']['humidity']
            print(f"Humidity: {humidity5}%")

            print("")

            unix_timestamp6 = data['list'][38]['dt']
            datetime6 = datetime.datetime.fromtimestamp(unix_timestamp6)
            print(f"Date & Time: {datetime6}")

            weather6 = data['list'][38]['weather'][0]['description']
            print(f"Weather: {weather6}")

            temp6 = data['list'][38]['main']['temp']
            print(f"Temperature: {temp6}F")
          
            humidity6 = data['list'][38]['main']['humidity']
            print(f"Humidity: {humidity6}%")

            print("===========================")
            break

    elif user_choice == "3":
        ### Calls imported function that prints list of available US cities
        print_us_cities(json_file_path)
        break

    elif user_choice == "4":
        ### Calls imported function that prints list of available international cities
        print_international_cities(json_file_path)
        break

    elif user_choice.lower() == "q":
        print("Quitting...goodbye!")
        break

    else:
        print("Error. Please select from the menu")
        print("===========================")
        print("1. Current weather")
        print("2. 5 day weather forecast")
        print("")
        print("Q. Quit")
        print("===========================")
        user_choice = input("Selection: ")

            
           

           











################################################ FOOTNOTES ################################################

#############################
# Version:    1.02          #
# Date:       07/27/2023    #
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
