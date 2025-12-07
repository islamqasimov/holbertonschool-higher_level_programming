#!/usr/bin/python3
"""
Python function that generates personalized invitation files
from a template with placeholders and a list of objects
"""

import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template must be a string. Function terminated.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries. Function terminated.")
        return

    # Handle empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        filled_template = template

        # Replace placeholders with values or N/A
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder)
            value = value if value not in [None, ""] else "N/A"
            filled_template = filled_template.replace(f"{{{placeholder}}}", value)

        # Generate filename
        filename = f"output_{index}.txt"

        # Write to file
        try:
            with open(filename, "w") as file:
                file.write(filled_template)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
