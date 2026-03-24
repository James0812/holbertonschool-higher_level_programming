#!/usr/bin/env python3
"""
Simple templating program to generate invitation files.
"""

import os


def generate_invitations(template, attendees):
    """Generate invitation files from template and attendees list"""

    # ✅ Vérification des types
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # ✅ Gestion des cas vides
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ✅ Traitement des participants
    for i, attendee in enumerate(attendees, start=1):

        # Récupération des valeurs avec "N/A" si manquant ou None
        name = attendee.get("name") if attendee.get("name") else "N/A"
        event_title = attendee.get("event_title") if attendee.get("event_title") else "N/A"
        event_date = attendee.get("event_date") if attendee.get("event_date") else "N/A"
        event_location = attendee.get("event_location") if attendee.get("event_location") else "N/A"

        # Remplacement des placeholders
        invitation = template
        invitation = invitation.replace("{name}", str(name))
        invitation = invitation.replace("{event_title}", str(event_title))
        invitation = invitation.replace("{event_date}", str(event_date))
        invitation = invitation.replace("{event_location}", str(event_location))

        # Nom du fichier
        filename = f"output_{i}.txt"

        try:
            # (optionnel) vérifier si le fichier existe déjà
            if os.path.exists(filename):
                os.remove(filename)

            # Écriture du fichier
            with open(filename, "w") as f:
                f.write(invitation)

        except Exception as e:
            print(f"Error writing file {filename}: {e}")
