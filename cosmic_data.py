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


class FirstNames(Enum):
    SARAH = 'Sarah'
    JOHN = 'John'
    ALICE = 'Alice'
    MICHAEL = 'Michael'
    EMMA = 'Emma'
    DAVID = 'David'
    LISA = 'Lisa'
    ROBERT = 'Robert'
    MARIA = 'Maria'
    JAMES = 'James'
    ANNA = 'Anna'
    WILLIAM = 'William'
    ELENA = 'Elena'
    THOMAS = 'Thomas'
    SOFIA = 'Sofia'
    DANIEL = 'Daniel'


class LastNames(Enum):
    CONNOR = 'Connor'
    SMITH = 'Smith'
    JOHNSON = 'Johnson'
    WILLIAMS = 'Williams'
    BROWN = 'Brown'
    JONES = 'Jones'
    GARCIA = 'Garcia'
    MILLER = 'Miller'
    DAVIS = 'Davis'
    RODRIGUEZ = 'Rodriguez'
    MARTINEZ = 'Martinez'
    HERNANDEZ = 'Hernandez'
    LOPEZ = 'Lopez'
    GONZALEZ = 'Gonzalez'


class Specializations(Enum):
    MISSION_COMMAND = 'Mission Command'
    NAVIGATION = 'Navigation'
    ENGINEERING = 'Engineering'
    LIFE_SUPPORT = 'Life Support'
    COMMUNICATIONS = 'Communications'
    MEDICAL_OFFICER = 'Medical Officer'
    PILOT = 'Pilot'
    SCIENCE_OFFICER = 'Science Officer'
    MAINTENANCE = 'Maintenance'
    SECURITY = 'Security'
    RESEARCH = 'Research'
    SYSTEMS_ANALYSIS = 'Systems Analysis'


class Missions(Enum):
    M0 = (f'M{random.randint(1926,2026)}_MARS',
          'Mars Colony Establishment', 'Mars')
    M1 = (f'M{random.randint(1926,2026)}_MOON',
          'Moon Research Mission', 'Moon')
    M2 = (f'M{random.randint(1926,2026)}_EUROPA',
          'Europa Research Mission', 'Europa')
    M3 = (f'M{random.randint(1926,2026)}_TITAN',
          'Titan Colony Establishment', 'Titan')
    M4 = (f'M{random.randint(1926,2026)}_ASTEROID_BELT',
          'Asteroid Belt Research Mission', 'Asteroid Belt')
    M5 = (f'M{random.randint(1926,2026)}_JUPITER_ORBIT',
          'Jupiter Orbital Colony Establishment', 'Jupiter Orbit')
    M6 = (f'M{random.randint(1926,2026)}_SATURN_RINGS',
          'Saturn Rings Research Mission', 'Saturn Rings')
    M7 = (f'M{random.randint(1926,2026)}_DEEP_SPACE',
          'Deep Space Colony Establishment', 'Deep Space')
    M8 = (f'M{random.randint(1926,2026)}_SOLAR_OBSERVATORY',
          'Solar Observatory Research Mission', 'Solar Observatory')


# ----------------------------------------------------------------------------
#  Exercise 0: Space Station Data
# ----------------------------------------------------------------------------

class SpaceStationData():

    def __init__(self) -> None:

        try:
            add_exercise_folder_to_path("ex0")
            from space_station import (SpaceStation)

        except ImportError as e:
            print(color(5, f' ERROR! Could not import Ex0 — {e}'))
        except Exception as e:
            print(color(5, f' ERROR! {e}'))

        self._station_id: str = None
        self._name: str = None
        self._crew_size: int = None
        self._power_level: float = None
        self._oxygen_level: float = None
        self._last_maintenance: datetime = None
        self._is_operational: bool = None
        self._notes: str = None

    def run_test(self) -> None:
        """Run one valid test and one invalid test"""
        try:

            print()
            print(" " + "-" * 60)
            print(color(3, ' 💫 Exercise 0: Space Station Data'))
            print(" " + "-" * 60)

            print()
            print(color(6, ' Testing Valid Station'))
            print(" " + "-" * 60)
            self._valid_test()
            self.space_station_data()

            print()
            print(color(5, ' Testing Invalid Station'))
            print(" " + "-" * 60)
            self._invalid_test()
            self.space_station_data()

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def space_station_data(self) -> None:
        """Try to print the content of the class"""
        try:
            station_number = random.randint(1, 100)
            ss = SpaceStation(
                station_id=self._station_id,
                name=self._name,
                crew_size=self._crew_size,
                power_level=self._power_level,
                oxygen_level=self._oxygen_level,
                last_maintenance=self._last_maintenance,
                is_operational=self._is_operational,
                notes=self._notes,
            )

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

    def _valid_test(self) -> None:

        try:
            station = random.choice(list(Stations)).value
            self._station_id = f'{station[0]}{random.randint(1, 100):03d}'
            self._name = station[1]
            self._crew_size = random.randint(1, 20)
            self._power_level = random.uniform(0.0,1 100.0)
            self._oxygen_level = random.uniform(0.0, 100.0)
            self._last_maintenance = datetime.now()
            self._is_operational = random.choice([True, False])
            self._notes = (random.choice(list(Notes)).value)

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def _invalid_test(self) -> None:

        try:
            if random.choice([True, False]):
                self._station_id = ('.' * random.randint(0, 2))
            else:
                self._station_id = ('.' * random.randint(11, 100))

            if random.choice([True, False]):
                self._name = ''
            else:
                self._name = ('.' * random.randint(51, 100))

            if random.choice([True, False]):
                self._crew_size = random.randint(-100, 0)
            else:
                self._crew_size = random.randint(21, 100)

            if random.choice([True, False]):
                self._power_level = random.uniform(-100.0, -0.1)
            else:
                self._power_level = random.uniform(100.1, 200.0)

            if random.choice([True, False]):
                self._oxygen_level = random.uniform(-100.0, -0.1)
            else:
                self._oxygen_level = random.uniform(100.1, 200.0)

            self._notes = random.randint('.' * random.randint(201, 300))

        except Exception as e:
            print(color(5, f' ERROR! {e}'))


# ----------------------------------------------------------------------------
#  Exercise 1: Alien Contact Logs
# ----------------------------------------------------------------------------

class AlienContactLogs():

    def __init__(self) -> None:

        try:
            add_exercise_folder_to_path("ex1")
            from alien_contact import (AlienContact, ContactType)

        except ImportError as e:
            print(color(5, f' ERROR! Could not import Ex1 — {e}'))
        except Exception as e:
            print(color(5, f' ERROR! {e}'))

        self._contact_id: str = None
        self._timestamp: datetime = None
        self._location: str = None
        self._contact_type: ContactType = None
        self._signal_strength: float = None
        self._duration_minutes: int = None)
        self._witness_count: int = None
        self._message_received: str = None
        self._is_verified: bool = None

    def run_test(self) -> None:
        """Run one valid test and one invalid test"""

        try:
            print()
            print(" " + "-" * 60)
            print(color(7, ' 👽 Exercise 1: Alien Contact Logs'))
            print(" " + "-" * 60)

            print()
            print(color(6, ' Testing Valid Contact'))
            print(" " + "-" * 60)
            self._valid_test()
            self.alien_contact_logs()

            print()
            print(color(5, ' Testing Invalid Contact'))
            print(" " + "-" * 60)
            self._invalid_test()
            self.alien_contact_logs()

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def alien_contact_logs(self) -> None:
        """Try to print the content of the class"""
        try:
            ac = AlienContact(
                contact_id=self._contact_id,
                timestamp=self._timestamp,
                location=self._location,
                contact_type=self._contact_type,
                signal_strength=self._signal_strength,
                duration_minutes=self._duration_minutes,
                witness_count=self._witness_count,
                message_received=self._message_received,
                is_verified=self._is_verified,
            )

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

    def _valid_test(self) -> None:

        try:
            self._contact_id = (f'AC_{random.randint(1900, 2026)}_'
                               f'{random.randint(1, 100):03d}')
            self._timestamp = datetime.now()
            self._location = random.choice(list(Locations)).value
            self._contact_type = random.choice(list(ContactType))
            self._signal_strength = random.uniform(0.0, 10.0)
            self._duration_minutes = random.randint(1, 1440)
            self._witness_count = random.randint(3, 100)
            self._message_received = random.choice(list(Messages)).value
            self._is_verified = is_verified=True

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def _invalid_test(self) -> None:

        try:
            if random.choice([True, False]):
                self._contact_id = ('.' * random.randint(0, 4))
            else:
                self._contact_id = ('.' * random.randint(16, 100))

            if random.choice([True, False]):
                self._location = ('.' * random.randint(0, 2))
            else:
                self._location = ('.' * random.randint(101, 200))

            if random.choice([True, False]):
                self._signal_strength = random.uniform(-100.0, -0.1)
            else:
                self._signal_strength = random.uniform(10.1, 100.0)

            if random.choice([True, False]):
                self._duration_minutes = random.randint(101, 200)
            else:
                self._duration_minutes = random.randint(1441, 1500)

            if random.choice([True, False]):
                self._witness_count = random.randint(-100, 0)
            else:
                self._witness_count = random.randint(101, 200)

            self._message_received = ('.' * random.randint(501, 600))

        except Exception as e:
            print(color(5, f' ERROR! {e}'))


# ----------------------------------------------------------------------------
#  Exercise 2: Space Crew Management
# ----------------------------------------------------------------------------

class SpaceCrewManagement():

    def __init__(self) -> None:

        try:
            add_exercise_folder_to_path("ex2")
            from space_crew import (SpaceMission, CrewMember, Rank)

        except ImportError as e:
            print(color(5, f' ERROR! Could not import Ex2 — {e}'))
        except Exception as e:
            print(color(5, f' ERROR! {e}'))

            mission_id: str = None
            mission_name: str = None
            destination: str = None
            launch_date: datetime = None
            duration_days: int = None
            crew: List[CrewMember] = None
            mission_status: str = None
            budget_millions: float = None

    def run_test(self) -> None:
        """Run one valid test and one invalid test"""

        try:
            print()
            print(" " + "-" * 60)
            print(color(4, ' 🚀 Exercise 2: Space Crew Management'))
            print(" " + "-" * 60)

            print()
            print(color(6, ' Testing Valid Mission'))
            print(" " + "-" * 60)
            self._valid_test()
            self.space_crew_management()

            print()
            print(color(5, ' Testing Invalid Mission'))
            print(" " + "-" * 60)
            self._invalid_test()
            self.space_crew_management()

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def space_crew_management(self) -> None:

        try:

            print()
            print(" " + "-" * 60)
            print(color(4, ' 🚀 Exercise 2: Space Crew Management'))
            print(" " + "-" * 60)

            try:

                mission = random.choice(list(Missions))

                crew_size = random.randint(3, 8)
                crew: list = []

                has_commander = False
                for j in range(crew_size):
                    member_id = f"CM{str(i*10 + j + 1).zfill(3)}"
                    member = self.generate_crew_member(member_id)

                sm = SpaceMission(
                    mission_id=mission[0],
                    mission_name=mission[1],
                    destination=mission[2],
                    launch_date=datetime.now(),
                    duration_days=random.randint(1, 3650),
                    crew=crew_list,
                    mission_status='',
                    budget_millions=random.uniform(1.0, 10000.0),
                    )

            except ValidationError as e:
                for error in e.errors():
                    print(color(5, ' ERROR!') + f' {error["msg"]}')
                print()

        except ImportError as e:
            print(color(5, f' ERROR! Could not import Ex2 — {e}'))
        except Exception as e:
            print(color(5, f' ERROR! {e}'))


# ----------------------------------------------------------------------------
#  Tester entry point
# ---------------------------------------------------------------------------

class CosmicData:

    def cosmic_data(self) -> None:
        """Interactive UI fro choice."""

        ssd = SpaceStationData()
        acl = AlienContactLogs()
        scm = SpaceCrewManagement()

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
            ssd.space_station_data()
        elif choice == "1":
            acl.alien_contact_logs()
        elif choice == "2":
            scm.space_crew_management()
        else:
            print(color(5, ' ERROR! Invalid choice! Please enter 0, 1, or 2'))


if __name__ == "__main__":
    cd = CosmicData()
    cd.cosmic_data()
