#!/usr/bin/env python3

"""
Cosmic Data - Interactive Test Runner
Run this file to test your exercises interactively.
Usage: python3 cosmic_data.py
"""


# ----------------------------------------------------------------------------
#  Import
# ----------------------------------------------------------------------------

import os
import sys
import random
from enum import Enum
from typing import Dict
from datetime import datetime
from pydantic import ValidationError


# ----------------------------------------------------------------------------
#  Standard ANSI Color codes
# ----------------------------------------------------------------------------

def color(code: int, text: str) -> str:
    """A function making strings of text colorful."""
    colors: Dict[int, str] = {
            0: "\033[0m",     # Reset
            1: "\033[1;91m",  # Red
            2: "\033[1;92m",  # Green
            3: "\033[1;93m",  # Yellow
            4: "\033[1;94m",  # Blue
            5: "\033[1;95m",  # Magenta
            6: "\033[1;96m",  # Cyan
            7: "\033[1;97m"   # White
        }

    if code < 7:
        color = colors[code]
    else:
        color = colors[7]

    return f'{color}{text}{colors[0]}'


# ----------------------------------------------------------------------------
#  Find folders
# ----------------------------------------------------------------------------

def add_exercise_folder_to_path(folder_name: str) -> None:
    """Adds the specified exercise folder to the Python path."""
    folder_path = os.path.join(os.path.dirname(__file__), folder_name)
    if folder_path not in sys.path:
        sys.path.insert(0, folder_path)


# ----------------------------------------------------------------------------
#  Data Enums
# ----------------------------------------------------------------------------

class Stations(Enum):
    SN1 = ('ISS', 'International Space Station')
    SN2 = ('LGW', 'Lunar Gateway')
    SN3 = ('MOP', 'Mars Orbital Platform')
    SN4 = ('ERS', 'Europa Research Station')
    SN5 = ('TMO', 'Titan Mining Outpost')
    SN6 = ('ABR', 'Asteroid Belt Relay')
    SN7 = ('DSO', 'Deep Space Observatory')
    SN8 = ('SWM', 'Solar Wind Monitor')
    SN9 = ('QCH', 'Quantum Communications Hub')


# ----------------------------------------------------------------------------
#  Interactive tester UI
# ---------------------------------------------------------------------------

class CosmicData:

    def cosmic_data(self) -> None:
        """Interactive UI fro choice."""
        print()
        print(" " + "-" * 60)
        print(color(3, ' 💫 WELCOME TO COSMIC DATA!'))
        print(" " + "-" * 60)
        print(" This program will help you test the exercises of this module.")
        print(" Which exercise would you like to test?")
        print()

        print(color(7, f" {'n.':<5}{'Exercise':<30}{'Description'}"))
        print(" " + "-" * 60)
        print(f" {'0':<5}{'Space Station Data':<30}"
              "Basic Pydantic")
        print(f" {'1':<5}{'Alien Contact Logs':<30}"
              "Custom validation")
        print(f" {'2':<5}{'Space Crew Management':<30}"
              "Nested Pydantic")
        print()

        choice = input(color(3, ' 💫 Enter your choice (0/1/2): '))

        if choice == "0":
            self.space_station_data()
        elif choice == "1":
            self.alien_contact_logs()
        elif choice == "2":
            self.space_crew_management()
        else:
            print(color(5, ' ERROR! Invalid choice! Please enter 0, 1, or 2'))

    # ----------------------------------------------------------------------------
    #  Exercise 0: Space Station Data
    # ----------------------------------------------------------------------------

    def space_station_data(self) -> None:

        try:
            add_exercise_folder_to_path("ex0")
            from space_station import (SpaceStation)

            print()
            print(" " + "-" * 60)
            print(color(7, ' 💫 Exercise 0: Space Station Data'))
            print(" " + "-" * 60)

            # --- Testing valid station
            try:
                station = random.choice(list(Stations)).value
                station_number = random.randint(1, 100)
                v = SpaceStation(
                    station_id=f'{station[0]}{station_number:03d}',
                    name=station[1],
                    crew_size=random.randint(1, 20),
                    power_level=random.uniform(0.0, 100.0),
                    oxygen_level=random.uniform(0.0, 100.0),
                    last_maintenance=datetime.now(),
                    is_operational=random.choice([True, False])
                    )

                print()
                print(color(6, ' Testing VALID Station'))
                print(" " + "-" * 60)
                print(f' {color(7, "ID"):<20}{v.station_id}')
                print(f' {color(7, "Name"):<20}{v.name}')
                print(f' {color(7, "Crew"):<20}{v.crew_size} people')
                print(f' {color(7, "Power"):<20}{v.power_level:.1f}%')
                print(f' {color(7, "Oxygen"):<20}{v.oxygen_level:.1f}%')

                if v.is_operational:
                    status = color(2, 'Operational')
                else:
                    status = color(3, 'Maintenance')

                print(f' {color(7, "Status"):<20}{status}')
                print()

            except ValidationError as e:
                for error in e.errors():
                    print(color(5, ' ERROR!') + f' {error["msg"]}')
                print()

            # --- Testing less than minimum values
            try:
                print(color(5, ' Testing INVALID Station (min edge cases)'))
                print(" " + "-" * 60)

                SpaceStation(
                    station_id=('.' * 2),
                    name='',
                    crew_size=0,
                    power_level=-1.0,
                    oxygen_level=-1.0,
                    last_maintenance=''
                )

            except ValidationError as e:
                for error in e.errors():
                    print(color(5, ' ERROR!') + f' {error["msg"]}')
                print()

            # --- Testing more than maximum values
            try:
                print(color(5, ' Testing INVALID Station (max edge cases)'))
                print(" " + "-" * 60)

                SpaceStation(
                    station_id=('.' * 11),
                    name=('.' * 51),
                    crew_size=21,
                    power_level=100.1,
                    oxygen_level=100.1,
                    last_maintenance=''
                )

            except ValidationError as e:
                for error in e.errors():
                    print(color(5, ' ERROR!') + f' {error["msg"]}')
                print()

        except ImportError as e:
            print(color(5, f' ERROR! Could not import Ex0 — {e}'))
        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    # ----------------------------------------------------------------------------
    #  Exercise 1: Alien Contact Logs
    # ----------------------------------------------------------------------------

    def alien_contact_logs(self) -> None:

        try:
            add_exercise_folder_to_path("ex0")
            from space_station import (AlienContact, ContactType)

        except ImportError as e:
            print(color(5, f' ERROR! Could not import Ex1 — {e}'))
        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    # ----------------------------------------------------------------------------
    #  Exercise 2: Space Crew Management
    # ----------------------------------------------------------------------------

    def space_crew_management(self) -> None:

        try:
            add_exercise_folder_to_path("ex2")

        except ImportError as e:
            print(color(5, f' ERROR! Could not import Ex2 — {e}'))
        except Exception as e:
            print(color(5, f' ERROR! {e}'))


if __name__ == "__main__":
    cd = CosmicData()
    cd.cosmic_data()
