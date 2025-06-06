Can be accessed through this link: "https://weather-application-using-python.onrender.com"

START SERVER  -->  Visit http://localhost:8000  -->  Flask handles '/'
                                             |
                                             v
                                      Render 'index.html'

'index.html':
  - User sees a form
  - User types a city name
  - User clicks "Submit"
       |
       v
    Sends GET request to '/weather?city=CityName'

'/weather' route:
  - Extracts city name from request
  - Calls get_current_weather(city) from weather.py
       |
       v
  weather.py makes a request to OpenWeatherMap API
       |
       v
  Gets weather JSON data
       |
       v
  Passes data to 'weather.html' to display it

  ---> 'weather.html' is rendered and shown in browser
