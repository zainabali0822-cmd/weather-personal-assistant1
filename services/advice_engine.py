def get_closest_weather(hour, weather):
    """Return weather entry closest to the given hour."""
    return min(weather, key=lambda w: abs(w["hour"] - hour))

def generate_advice(events, weather):
    """Generate advice by matching events to nearest weather hour."""
    if not events:
        return ["Clear schedule! Enjoy the day."]
    advice = []
    for event in events:
        event_hour = event["start"].hour
        w = get_closest_weather(event_hour, weather)
        if w["rain_pct"] > 50:
            advice.append(f"Bring an umbrella to '{event['title']}'")
        if w["temp_c"] < 20:
            advice.append(f"Dress warmly for '{event['title']}'")
        if w["rain_pct"] <= 50 and w["temp_c"] >= 20:
            advice.append(f"'{event['title']}' looks weather-friendly!")
    return advice[:3]
