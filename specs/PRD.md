# PRD: Weather-Aware Personal Assistant ("Nova")

## Problem
Users forget to check weather before events. This CLI assistant
cross-references their daily schedule with live weather data and
delivers actionable advice in seconds.

## Architecture
- services/weather_service.py — Fetch Open-Meteo API. No prints.
- services/calendar_service.py — Read calendar.json. No prints.
- services/advice_engine.py — Combine weather + events. No I/O.
- main.py — CLI entry point only. No business logic.

## Advice Rules
- rain_pct > 50 during event: "Bring an umbrella to [title]"
- temp_c < 20 during event: "Dress warmly for [title]"
- No events: "Clear schedule! Enjoy the day."

## API
- URL: https://api.open-meteo.com/v1/forecast
- Params: latitude=24.86, longitude=67.01
- No API key required
