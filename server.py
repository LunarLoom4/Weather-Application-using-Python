from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

# Creates the core Flask app object
app = Flask(__name__)

# This is the Homepage. When a user visits the URL path / or /index, run the index() function.
# When someone goes to http://localhost:8000/      → Flask runs index()
# When someone goes to http://localhost:8000/index → Flask runs index()
@app.route('/')
@app.route('/index')        # Multiple entry points for the same page
def index():
    return render_template('index.html')

# When the form is submitted in index.html, this '/weather' route is called in the Flask app.
@app.route('/weather')
def get_weather():
    # Grabs query parameters from the URL (/weather?city=Pune) as the browser makes a GET request to (/weather?city=Pune).
    city = request.args.get('city')

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = 'Hadapsar'
    else:
        city = city.strip()     # Is not required as trailing spaces are handled by 'OpenWeatherMap' automatically.

    # This calls the function in weather.py.
    weather_data = get_current_weather(city)

    # Easy Way of handling the case if city is 'not found' by API
    # if weather_data['cod'] != 200:
    #     return "City not found. Please check the city name."

    # Professional Way of handling the case if city is 'not found' by API (creating a separate template)
    if weather_data['cod'] != 200:
        return render_template('city-not-found.html')

    # Sends our data to weather.html.
    # Jinja2 replaces placeholders like {{ title }}, {{ status }}, etc., in the HTML file.
    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}")

# Starts the app using Waitress (a WSGI server) when this file is run directly
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
