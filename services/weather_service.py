import requests
from datetime import datetime

def get_hourly_weather(latitude=24.86, longitude=67.01):
    """Fetch today's hourly weather from Open-Meteo. Returns [{hour, temp_c, rain_pct}]"""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,precipitation_probability",
        "forecast_days": 1,
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    times = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]
    rains = data["hourly"]["precipitation_probability"]
    today = datetime.now().date()
    results = []
    for time_str, temp, rain in zip(times, temps, rains):
        dt = datetime.fromisoformat(time_str)
        if dt.date() == today:
            results.append({"hour": dt.hour, "temp_c": temp, "rain_pct": rain})
    return results
