import json
# Define a function to fetch weather data from a JSON file
def fetch_weather_data(file_path):
 try:
  with open(file_path, 'r') as json_file:
   weather_data = json.load(json_file)
  return weather_data
 except FileNotFoundError:
  print(f"File not found: {file_path}")
  return None
# Specify the path to the JSON file containing weather data
json_file_path = 'weather10b.json'
# Fetch the weather data from the JSON file
weather_data = fetch_weather_data(json_file_path)
# Check if the data was successfully loaded
if weather_data:
    # Print the weather data or access specific values as needed
 print("Current Weather Data:")
 print(f"Current Temperature: {weather_data ['current temperature']}")
 print(f"Humidity: {weather_data ['Humidity']}")
 print(f"Weather description:{weather_data ['Weather description']}")
else:
 print("Failed to fetch weather data.")
