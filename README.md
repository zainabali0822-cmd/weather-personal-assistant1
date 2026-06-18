# Nova — Weather-Aware Personal Assistant

A CLI assistant that cross-references your daily calendar with live
weather data and delivers actionable advice.

## How to Run
pip install requests
python main.py

## Run Tests
python -m pytest tests/ -v

## Project Structure
weather-personal-assistant/
├── main.py
├── calendar.json
├── specs/PRD.md
├── docs/rules.md
├── services/
│   ├── weather_service.py
│   ├── calendar_service.py
│   └── advice_engine.py
└── tests/
    └── test_advice.py

## Vibe Report

### Where did the AI's vibe drift?
The AI initially added print statements inside weather_service.py,
violating the separation of concerns rule in my PRD. I re-prompted
specifying zero print statements and data-only return values.

### When did I use the Builder Hammer?
The advice engine returned more than 3 bullets. I manually added
the [:3] slice at the end of generate_advice() to enforce the rule.

### Most successful steering prompt?
Referencing the PRD directly in every prompt forced the AI to follow
my architecture instead of improvising its own structure.
