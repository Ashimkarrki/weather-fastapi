# 🌤️ Weather Today

**Weather Today** is a simple FastAPI web application using Jinja2 templates that allows users to search for a location and get the current weather temperature and air quality information.

## 🚀 Features

- 🌍 Search for any location
- 🌡️ View current temperature
- 🌫️ Check real-time air quality index

## 📦 Setup Instructions

Follow these steps to get the app running locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Ashimkarrki/weather-fastapi
cd weather-fastapi
```

### 2. Create a .env file in the root directory with the following content

```bash
WEATHER_API={your_api_key_here}
WEATHER_ENDPOINT={endpoint_from_provider}
```

You can obtain a free API key from

https://www.weatherapi.com/

### 3. Build Docker Image

```bash
docker build -t weather .
```

### 4. Run the Docker Container

```bash
docker run -d -p 8000:8000 weather-today-app
```

### 5. Access the App

Open your browser and navigate to

http://127.0.0.1:8000

## 🛠️ Tech Stack

FastAPI

Jinja2
