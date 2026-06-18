from datetime import datetime
from services.weather_service import get_hourly_weather
from services.calendar_service import get_todays_events
from services.advice_engine import generate_advice

def main():
    """Entry point for Nova."""
    day = datetime.now().strftime("%A, %B %d")
    print(f"\n☀️  Nova | Your Daily Briefing — {day}\n")
    try:
        weather = get_hourly_weather()
    except Exception as e:
        print(f"⚠️  Could not fetch weather: {e}")
        weather = [{"hour": 12, "temp_c": 25, "rain_pct": 0}]
    try:
        events = get_todays_events()
    except Exception as e:
        print(f"⚠️  Could not read calendar: {e}")
        events = []
    advice = generate_advice(events, weather)
    print("📋 Today's Advice:")
    for tip in advice:
        print(f"   • {tip}")
    print("\nHave a great day! 🌟\n")

if __name__ == "__main__":
    main()
