import json

structured_data = [
    {
        "category": "Health & Well-being",
        "entries": [
            {
                "entry": 1,
                "title": "Morning Fatigue and Physical Discomfort",
                "thoughts": [
                    "Felt like I hadn’t slept at all despite waking at 5:30.",
                    "Shoulder's aching again—might have overdone code review.",
                    "Skipped dinner last night and now stomach’s rumbling.",
                    "Lungs feel heavy these days.",
                    "Another sleepless night feels inevitable."
                ]
            }
        ]
    },
    {
        "category": "Family & Relationships",
        "entries": [
            {
                "entry": 1,
                "title": "Connections and Commitments",
                "thoughts": [
                    "Should call Anya before she leaves for school.",
                    "Kids want me to read them a story tonight.",
                    "Love our drive to Auroville market — cherish these shared moments."
                ]
            }
        ]
    },
    {
        "category": "Work Stress",
        "entries": [
            {
                "entry": 1,
                "title": "Project Pressure and Mental Load",
                "thoughts": [
                    "Worried about the database migration promised by Friday.",
                    "Demo feels distant and unprepared.",
                    "Stayed up late fixing a bug.",
                    "Procrastinating journaling — probably due to overwhelm."
                ]
            }
        ]
    },
    {
        "category": "Community & Meaningful Work",
        "entries": [
            {
                "entry": 1,
                "title": "Split Priorities",
                "thoughts": [
                    "Community garden needs volunteers tomorrow morning.",
                    "Torn between writing new features and planting seedlings."
                ]
            }
        ]
    },
    {
        "category": "Emotional State",
        "entries": [
            {
                "entry": 1,
                "title": "Lingering Weight and Discontent",
                "thoughts": [
                    "Felt like I hadn’t slept — mental exhaustion.",
                    "Feels late already — rushed and unprepared.",
                    "Heart sinks thinking of sleepless nights.",
                    "Ugh — low motivation, mild frustration."
                ]
            }
        ]
    },
    {
        "category": "Habits & Patterns",
        "entries": [
            {
                "entry": 1,
                "title": "Recurring Routines",
                "thoughts": [
                    "Woke up at 5:30 — early pattern continues.",
                    "Skipped dinner to fix a bug — work eating into self-care.",
                    "Procrastinating journaling again.",
                    "Thought of jogging tomorrow — future hope not yet acted on."
                ]
            }
        ]
    }
]

# Pretty-print the JSON to console or save to file
print(json.dumps(structured_data, indent=2))
