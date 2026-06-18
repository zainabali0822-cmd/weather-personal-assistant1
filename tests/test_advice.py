import unittest
from datetime import datetime
from services.advice_engine import generate_advice

def make_event(title, hour):
    return {
        "title": title,
        "start": datetime(2026, 6, 18, hour, 0),
        "end": datetime(2026, 6, 18, hour + 1, 0),
        "location": "Test Location",
    }

class TestAdviceEngine(unittest.TestCase):
    def test_rain_triggers_umbrella(self):
        events = [make_event("Team Meeting", 9)]
        weather = [{"hour": 9, "temp_c": 25, "rain_pct": 80}]
        advice = generate_advice(events, weather)
        self.assertTrue(any("umbrella" in tip for tip in advice))

    def test_cold_triggers_warmth(self):
        events = [make_event("Morning Run", 7)]
        weather = [{"hour": 7, "temp_c": 10, "rain_pct": 5}]
        advice = generate_advice(events, weather)
        self.assertTrue(any("warmly" in tip for tip in advice))

    def test_no_events_returns_clear_message(self):
        advice = generate_advice([], [])
        self.assertIn("Clear schedule", advice[0])

if __name__ == "__main__":
    unittest.main()
