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
#   Pathfinder
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
    SN0 = ('ISS', 'International Space Station')
    SN1 = ('LGW', 'Lunar Gateway')
    SN2 = ('MOP', 'Mars Orbital Platform')
    SN3 = ('ERS', 'Europa Research Station')
    SN4 = ('TMO', 'Titan Mining Outpost')
    SN5 = ('ABR', 'Asteroid Belt Relay')
    SN6 = ('DSO', 'Deep Space Observatory')
    SN7 = ('SWM', 'Solar Wind Monitor')
    SN8 = ('QCH', 'Quantum Communications Hub')


class Notes(Enum):
    NOMINAL = 'All systems operating within normal parameters.'
    RESUPPLY = 'Awaiting cargo resupply shuttle.'
    METEOROID = 'Minor hull scouring detected.'
    SOLAR_FLARE = 'Increased radiation levels.'
    GRAVITY_LEAK = 'Gravitational leak detected.'
    ALIEN_CONTACT = 'Unidentified signal pattern detected.'


class Locations(Enum):
    L0 = 'Area 51, Nevada'
    L1 = 'Roswell, New Mexico'
    L2 = 'SETI Institute, California'
    L3 = 'Arecibo Observatory, Puerto Rico'
    L4 = 'Atacama Desert, Chile'
    L5 = 'Antarctic Research Station'
    L6 = 'International Space Station'
    L7 = 'Mauna Kea Observatory, Hawaii'
    L8 = 'Very Large Array, New Mexico'


class Messages(Enum):
    M0 = 'Greetings from Zeta Reticuli'
    M1 = 'Mathematical sequence detected: prime numbers'
    M2 = 'Coordinates to star system received'
    M3 = 'Warning about solar flare activity'
    M4 = 'Request for peaceful contact'
    M5 = 'Unknown language pattern identified'


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
            print(color(3, ' 💫 Exercise 0: Space Station Data'))
            print(" " + "-" * 60)

            # --- Testing valid station
            try:
                station = random.choice(list(Stations)).value
                station_number = random.randint(1, 100)
                ss = SpaceStation(
                    station_id=f'{station[0]}{station_number:03d}',
                    name=station[1],
                    crew_size=random.randint(1, 20),
                    power_level=random.uniform(0.0, 100.0),
                    oxygen_level=random.uniform(0.0, 100.0),
                    last_maintenance=datetime.now(),
                    is_operational=random.choice([True, False]),
                    notes=(random.choice(list(Notes)).value),
                )

                print()
                print(color(6, ' Testing VALID Station'))
                print(" " + "-" * 60)

                for k, v in ss.model_dump().items():
                    label = k.replace('_', ' ').title()

                    if k == 'crew_size':
                        display_value = f'{v} people'
                    elif k == 'power_level' or k == 'oxygen_level':
                        display_value = f'{v:.1f}%'
                    elif k == 'last_maintenance':
                        display_value = v.strftime("%Y-%m-%d %H:%M:%S.%f")[:-5]
                    elif k == 'is_operational':
                        if v:
                            display_value = color(2, 'Operational')
                        else:
                            display_value = color(3, 'Maintenance')
                    else:
                        display_value = str(v)

                    print(f' {color(7, label):<30}{display_value}')


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
                    last_maintenance='',
                    is_operational='',
                    notes=-1,
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
                    last_maintenance=('1' * 1000),
                    is_operational='',
                    notes=('.' * 201),
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
            add_exercise_folder_to_path("ex1")
            from alien_contact import (AlienContact, ContactType)

            print()
            print(" " + "-" * 60)
            print(color(7, ' 👽 Exercise 1: Alien Contact Logs'))
            print(" " + "-" * 60)

            # --- Testing valid contact
            try:
                year = random.randint(1900, 2026)
                n = random.randint(1, 100)
                ac = AlienContact(
                    contact_id=f'AC_{year}_{n:03d}',
                    timestamp=datetime.now(),
                    location=random.choice(list(Locations)).value,
                    contact_type=random.choice(list(ContactType)),
                    signal_strength=random.uniform(0.0, 10.0),
                    duration_minutes=random.randint(1, 1440),
                    witness_count=random.randint(3, 100),
                    message_received=random.choice(list(Messages)).value,
                    is_verified=True
                    )

                print()
                print(color(6, ' Testing VALID Contact Report'))
                print(" " + "-" * 60)

                for k, v in ac.model_dump().items():
                    label = k.replace('_', ' ').title()

                    if k == 'timestamp':
                        display_value = v.strftime("%Y-%m-%d %H:%M:%S.%f")[:-5]
                    elif k == 'contact_type':
                        display_value = v.value
                    elif k == 'signal_strength':
                        display_value = f'{v:.1f}/10'
                    elif k == 'duration_minutes':
                        display_value = f'{v} minutes'
                    elif k == 'is_verified':
                        if v:
                            display_value = color(2, 'Verified')
                        else:
                            display_value = color(3, 'Unverified')
                    else:
                        display_value = str(v)

                    print(f' {color(7, label):<30}{display_value}')

                print()

            except ValidationError as e:
                for error in e.errors():
                    print(color(5, ' ERROR!') + f' {error["msg"]}')
                print()

            # --- Testing < min
            try:
                print(color(5, ' Testing INVALID contact (min edge cases)'))
                print(" " + "-" * 60)

                ac = AlienContact(
                    contact_id=('.' * 4),
                    timestamp='',
                    location=('.' * 2),
                    contact_type='',
                    signal_strength=-0.1,
                    duration_minutes=0,
                    witness_count=0,
                    message_received='',
                    is_verified=''
                    )

            except ValidationError as e:
                for error in e.errors():
                    print(color(5, ' ERROR!') + f' {error["msg"]}')
                print()

            # --- Testing > max
            try:
                print(color(5, ' Testing INVALID contact (max edge cases)'))
                print(" " + "-" * 60)

                ac = AlienContact(
                    contact_id=('.' * 16),
                    timestamp='',
                    location=('.' * 101),
                    contact_type='',
                    signal_strength=10.1,
                    duration_minutes=1441,
                    witness_count=101,
                    message_received=('.' * 501),
                    is_verified=''
                    )

            except ValidationError as e:
                for error in e.errors():
                    print(color(5, ' ERROR!') + f' {error["msg"]}')
                print()

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
