# This is a simple weather program that fetches weather data from an API and displays either the current or forecast here from a location of your choosing
import requests 
import json
from datetime import datetime

print("Enter location:")

location = input()

if not location:
    raise ValueError("Error: Location not found")

print("Would you like the current or the forecast?")

feature = input()

if feature == "current":
    url = f"http://api.weatherapi.com/v1/current.json?key=5d7460b286bf4f33af985103230406&q={location}" 

else:
    url = f"http://api.weatherapi.com/v1/forecast.json?key=5d7460b286bf4f33af985103230406&&days=3&q={location}"

try:
    response = requests.get(url, headers={'Accept': 'application/json'})
    response.raise_for_status()
    data = response.json()

    if 'error' in data:
        error_message = data['error']['message']
        print("Error:", error_message)

    else:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"weather_data_{timestamp}.json"
        with open(file_name, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Weather data has been saved as {file_name}, check programs folder")

except requests.exceptions.HTTPError:
    print("Error: Location is not defined")

except requests.exceptions.RequestException:
    print("Error: Connection not secure")

#further steps
# add location <-- done
# errors <-- done
# display in table <-- not now, seems redundant
# download <-- done 
# old way of printing I came up with: f"Weather data has been saved as {file_name}"
