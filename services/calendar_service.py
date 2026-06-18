import json
from datetime import datetime

def get_todays_events(filepath="calendar.json"):
    """Read calendar.json and return only today's events."""
    with open(filepath, "r") as f:
        data = json.load(f)
    today = datetime.now().date()
    todays_events = []
    for event in data.get("events", []):
        start_dt = datetime.fromisoformat(event["start"])
        if start_dt.date() == today:
            todays_events.append({
                "title": event["title"],
                "start": start_dt,
                "end": datetime.fromisoformat(event["end"]),
                "location": event["location"],
            })
    return sorted(todays_events, key=lambda e: e["start"])
