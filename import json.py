import json
import re
from typing import List, Dict
from collections import defaultdict

# Define categories and relevant keywords
CATEGORY_KEYWORDS = {
    "Health & Well-being": ["ache", "pain", "tired", "sleep", "energy", "sick", "stomach", "lungs", "fatigue", "stretch"],
    "Family & Relationships": ["kids", "anya", "wife", "husband", "partner", "mom", "dad", "school", "story", "dinner", "family"],
    "Work Stress": ["code", "demo", "deadline", "bug", "meeting", "review", "client", "task", "sprint", "migration"],
    "Community & Meaningful Work": ["community", "garden", "volunteer", "auroville", "help", "give back", "seedlings"],
    "Emotional State": ["ugh", "happy", "sad", "angry", "worried", "afraid", "love", "frustrated", "heart", "motivation", "procrastinate"],
    "Habits & Patterns": ["woke up", "jog", "routine", "pattern", "again", "skip", "procrastinate", "tomorrow"]
}

def categorize_thought(thought: str) -> List[str]:
    """Return all categories that match keywords in the given thought."""
    categories = []
    lower_thought = thought.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in lower_thought for kw in keywords):
            categories.append(category)
    return categories

def generate_structured_json(journal_text: str, entry_id: int = 1, title: str = "Untitled Entry") -> List[Dict]:
    # Split input into thoughts by punctuation (simulate stream of thought)
    raw_thoughts = re.split(r'[.!?]\s*', journal_text.strip())
    raw_thoughts = [t.strip() for t in raw_thoughts if t.strip()]

    categorized = defaultdict(list)

    for thought in raw_thoughts:
        matched_categories = categorize_thought(thought)
        if not matched_categories:
            continue
        for category in matched_categories:
            categorized[category].append(thought)

    # Build final JSON structure
    structured_output = []
    for category in CATEGORY_KEYWORDS.keys():
        if category in categorized:
            structured_output.append({
                "category": category,
                "entries": [
                    {
                        "entry": entry_id,
                        "title": title,
                        "thoughts": categorized[category]
                    }
                ]
            })
    return structured_output

# Example usage
if __name__ == "__main__":
    journal_input = """
    I woke up at 5:30 but felt like I hadn’t slept at all. My shoulder’s aching again—did I push too hard on yesterday’s code review? 
    I keep thinking of the database migration I promised the client by Friday and that demo feels so far away. 
    I should call Anya before she leaves for school, but the email from community garden says they need volunteers tomorrow morning. 
    Why am I always torn between writing new features and planting seedlings? 
    Last night I skipped dinner to fix that bug, and now my stomach’s rumbling but any food sounds bland. 
    I should stretch, but I’m already late. The kids want me to read them a story tonight—will I have energy? 
    I love our drive to Auroville market, but my lungs feel heavy these days. My heart sinks when I think of another sleepless night. 
    Ugh, I’m procrastinating journaling again. Maybe tomorrow I’ll finally jog.
    """

    structured = generate_structured_json(journal_input, entry_id=1, title="Morning Reflections")
    print(json.dumps(structured, indent=2))
