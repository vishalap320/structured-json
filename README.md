# Stream-of-Consciousness Journal Structuring

This task involves converting a freeform, stream-of-consciousness journal entry from a software developer into a **structured JSON format**. The goal is to organize thoughts under six predefined categories:

- **Health & Well-being**
- **Family & Relationships**
- **Work Stress**
- **Community & Meaningful Work**
- **Emotional State**
- **Habits & Patterns**

The output structure includes **entry numbers**, **titles**, and **categorized thoughts**.

---

##  Libraries Used

Only one standard library is used:

- It allows you to convert Python data (like lists and dictionaries) into a JSON string and vice versa.

>  No additional  libraries are used in this code.

## How to Use:

1. Run the Script
To pretty-print the structured data:
python main.py

3. Export to File
You can modify the script to save the JSON data to a file:

with open("structured_data.json", "w") as f:
    json.dump(structured_data, f, indent=2)

## Expected Errors:
Error 1: FileNotFoundError when trying to write JSON files
Cause: The target directory for saving JSON files doesn't exist yet.

Example:
FileNotFoundError: [Errno 2] No such file or directory: 'output/BurnedOutTechLead/entry_1.json'

Solution: Before writing the file, ensure the directory exists using
```sh
os.makedirs() with exist_ok=True:
os.makedirs(os.path.dirname(file_path), exist_ok=True)
```

Example:
TypeError: Object of type set is not JSON serializable

Solution: Ensure that only JSON-serializable types (dict, list, str, int, float, bool, None) are written:
```sh
json.dump(data, f, indent=2)  # Make sure `data` only contains serializable types
```
If you must convert non-serializable objects:
```sh
json.dump(list(my_set), f)  # Convert set to list before saving
```

---

## Use Cases

- Organizing stream-of-consciousness text into structured data
- Saving personal logs in a readable and machine-processable format
- Feeding structured data to front-end apps, dashboards, or AI tools

This script builds and prints a clean, categorized JSON structure from journal-like thoughts using only the built-in `json` library.



---



# Demo Code

```python
import json

# Structured data from a stream-of-consciousness journal
structured_data = [
    {
        "entry_number": 1,
        "title": "Balancing Work and Health",
        "categories": {
            "Health & Well-being": [
                "Feeling fatigued due to long screen time.",
                "Skipped lunch again — need to fix this habit."
            ],
            "Family & Relationships": [
                "Missed my sister's call — need to catch up."
            ],
            "Work Stress": [
                "Deadlines piling up.",
                "Code reviews are mentally draining."
            ],
            "Community & Meaningful Work": [
                "Haven't contributed to the open-source project in weeks."
            ],
            "Emotional State": [
                "Feeling overwhelmed but hopeful."
            ],
            "Habits & Patterns": [
                "Late-night coding sessions are becoming routine."
            ]
        }
    }
]

# Pretty-print the JSON structure
print(json.dumps(structured_data, indent=4))
```
## What Can This Code Do?

This code defines a structured JSON format that organizes a person's thoughts  into categories such as **health**, **family**, **work**, **emotions**, and more.

Then, it prints that data as a formatted  JSON string.

Training or evaluating structured LLM output systems

Testing JSON schema conformity

Emotional state tracking

Life journaling analysis

Pattern recognition in personal habits

-




