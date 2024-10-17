Weather Out-Look
    Weather Out-Look is a weather forecasting application built using Python Django.
    It allows users to check the current weather information for any location, 
    receive real-time weather updates, set weather alerts, and customize the app's appearance.
    The app integrates several features like geolocation-based weather retrieval, manual location input,
    real-time weather updates, and more.


Features
    1. Current Weather Information
    Displays weather details such as:
    Temperature in Celsius
    Humidity percentage
    Wind Speed in m/s
    Atmospheric Pressure in hPa
    Shows weather condition icons based on real-time weather data.
    2. Manual Location Input
    Users can enter a city name manually to get the current weather for any location worldwide.
    3. Geolocation Weather Retrieval
    Automatically fetches the user's current location to provide real-time weather updates.
    4. Real-time Weather Updates
    Weather data is refreshed at regular intervals to display the most up-to-date information.
    5. Weather Alerts and Notifications
    Users can set weather alerts based on specific conditions and receive notifications.
    6. Themes and Customization
    A "Switch Theme" button allows users to toggle between dark and light themes for personalized user experience.
    7. Error Handling
    Includes error messages for invalid city inputs or connectivity issues.


Technology Stack
    Frontend: HTML, CSS, JavaScript, Bootstrap
    Backend: Python Django
    APIs: OpenWeatherMap API (for weather data)
    Database: SQLite (Django's default database)
    Additional Libraries:
    Django Rest Framework (optional for future API functionality)
    Requests (for handling API requests)
    Geolocation API (if needed)


Project Structure

    WeatherOutLook/
    │
    ├── manage.py
    ├── WeatherOutLook/                 # Project folder
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py                 # Contains all project configurations
    │   ├── urls.py                     # URL routing for the project
    │   ├── wsgi.py
    │
    ├── weather_app/                    # Main application folder
    │   ├── migrations/
    │   ├── static/                     # Static files (CSS, JS, images)
    │   ├── templates/                  # HTML templates
    │   │   └── base.html               # Base HTML template
    │   │   └── weather.html            # Main weather display template
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py                   # Database models (if needed for alerts)
    │   ├── tests.py
    │   ├── views.py                    # Main logic for handling weather requests
    │   ├── urls.py                     # URL routing for the app
    │
    └── db.sqlite3                      # Default SQLite database



Key Files and Directories
    settings.py: Contains the configuration for the project, such as API keys for OpenWeatherMap,
    installed apps, middleware, etc.
    urls.py: Maps URL paths to specific views within the app.
    views.py: Handles user requests, retrieves weather data from the API, and renders 
    the corresponding HTML templates with data.
    weather.html: Displays the current weather conditions and allows users to input cities and customize their view.


Installation and Setup
    Step 1: Create a Project Folder
        Create a folder, WeatherOutLook for the project on your machine.

    Step 2: Open the Terminal and Navigate to the Folder
        Move into the newly created folder

    Step 3: Create and Activate a Virtual Environment
        Run the following commands to set up a virtual environmen
        python -m venv env
        source env/bin/activate   # For Linux/MacOS
        env\Scripts\activate      # For Windows

    Step 4: Install Django
        Once the virtual environment is activated, install Django, pip install django

    Step 5: Start a New Django Project
        Create a new Django project within the folder, django-admin startproject WeatherOutLook

    Step 6: Start a New App
        Create a new Django app for the weather functionality, python manage.py startapp weather_app

    Step 7: Set Up the App in Django
        Open settings.py in the WeatherOutLook/ directory and add the new app to the INSTALLED_APPS list:
        INSTALLED_APPS = [
            ...
            'weather_app',
        ]

    Step 8: Apply Migrations
        Migrate the database schema using, 
        python manage.py makemigrations
        python manage.py migrate

    Step 9: Configure API Keys and Templates
        Add your OpenWeatherMap API key in settings.py or in a separate .env file.
        Set up your urls.py to direct traffic to the weather_app.
        Create HTML templates (base.html and weather.html) in the templates/ folder of your app.

    Step 10: Run the Server
        Start the Django development server: python manage.py runserver
        Open your browser and navigate to http://127.0.0.1:8000/ to view the app.


Future Improvements
    Integration of a weather forecast for upcoming days.
    Enhanced UI with animations for different weather conditions.
    Push notifications for severe weather alerts.
    User authentication for personalized weather alerts and preferences.


