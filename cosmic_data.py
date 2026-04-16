#!/usr/bin/env python3

"""
Cosmic Data - Interactive Test Runner
Run this file to test your exercises interactively.
Usage: python3 cosmic_data.py
"""


# ----------------------------------------------------------------------------
#  Import
# ----------------------------------------------------------------------------

try:
    import os
    import sys
    import random
    from enum import Enum
    from typing import Dict, List
    from datetime import datetime
    from pydantic import ValidationError

except ModuleNotFoundError as e:
    print(f'\n \033[1;95mERROR!\033[0m {e}')
    print(' python3 -m venv .venv')
    print(' source .venv/bin/activate')
    print(' pip install -r requirements.txt\n')
    exit()


def pathfinder(folder_name: str) -> None:
    """Adds the specified exercise folder to the Python path."""
    folder_path = os.path.join(os.path.dirname(__file__), folder_name)
    if folder_path not in sys.path:
        sys.path.insert(0, folder_path)


FOLDERS: list = ['ex0', 'ex1', 'ex2']
for F in FOLDERS:
    try:
        pathfinder(F)
    except ImportError as e:
        print(f' ERROR! Could not import  {F} — {e}')

from space_station import (SpaceStation)  # noqa: E402
from alien_contact import (AlienContact, ContactType)  # noqa: E402
from space_crew import (SpaceMission, CrewMember, Rank)  # noqa: E402


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
    M4 = (f'M{random.randint(1926,2026)}_AB',
          'Asteroid Belt Research Mission', 'Asteroid Belt')
    M5 = (f'M{random.randint(1926,2026)}_JO',
          'Jupiter Orbital Colony Establishment', 'Jupiter Orbit')
    M6 = (f'M{random.randint(1926,2026)}_SR',
          'Saturn Rings Research Mission', 'Saturn Rings')
    M7 = (f'M{random.randint(1926,2026)}_DS',
          'Deep Space Colony Establishment', 'Deep Space')
    M8 = (f'M{random.randint(1926,2026)}_SO',
          'Solar Observatory Research Mission', 'Solar Observatory')


# ----------------------------------------------------------------------------
#  Exercise 0: Space Station Data
# ----------------------------------------------------------------------------

class SpaceStationData():

    def __init__(self) -> None:
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
            print(color(7, ' 💫 Exercise 0: Space Station Data'))
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

            print()
            print(color(3, ' Testing Station'))
            print(" " + "-" * 60)
            self._specific_test()
            # self.space_station_data()
            print(' Uncomment to use')
            print()

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def space_station_data(self) -> None:
        """Try to print the content of the class"""
        try:
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

        except ValidationError as e:
            for error in e.errors():
                print(color(5, ' ERROR!') + f' {error["msg"]}')

    def _valid_test(self) -> None:

        try:
            station = random.choice(list(Stations)).value
            self._station_id = f'{station[0]}{random.randint(1, 100):03d}'
            self._name = station[1]
            self._crew_size = random.randint(1, 20)
            self._power_level = random.uniform(0.0, 100.0)
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

            self._last_maintenance = None
            self._is_operational = None
            self._notes = ('.' * random.randint(201, 300))

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def _specific_test(self) -> None:
        self._station_id = None
        self._name = None
        self._crew_size = None
        self._power_level = None
        self._oxygen_level = None
        self._last_maintenance = None
        self._is_operational = None
        self._notes = None


# ----------------------------------------------------------------------------
#  Exercise 1: Alien Contact Logs
# ----------------------------------------------------------------------------

class AlienContactLogs():

    def __init__(self) -> None:
        self._contact_id: str = None
        self._timestamp: datetime = None
        self._location: str = None
        self._contact_type: ContactType = None
        self._signal_strength: float = None
        self._duration_minutes: int = None
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

            print()
            print(color(3, ' Testing Contact'))
            print(" " + "-" * 60)
            self._specific_test()
            # self.alien_contact_logs()
            print(' Uncomment to use')
            print()

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

        except ValidationError as e:
            for error in e.errors():
                print(color(5, ' ERROR!') + f' {error["msg"]}')

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
            self._is_verified = True

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def _invalid_test(self) -> None:

        try:
            if random.choice([True, False]):
                self._contact_id = ('.' * random.randint(0, 4))
            else:
                self._contact_id = ('.' * random.randint(16, 100))

            self._timestamp = None

            if random.choice([True, False]):
                self._location = ('.' * random.randint(0, 2))
            else:
                self._location = ('.' * random.randint(101, 200))

            self._contact_type = None

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
            self._is_verified = None

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def _specific_test(self) -> None:
        self._contact_id = None
        self._timestamp = None
        self._location = None
        self._contact_type = None
        self._signal_strength = None
        self._duration_minutes = None
        self._witness_count = None
        self._message_received = None
        self._is_verified = None


# ----------------------------------------------------------------------------
#  Exercise 2: Space Crew Management
# ----------------------------------------------------------------------------

class SpaceCrewManagement():

    def __init__(self) -> None:
        self._mission_id: str = None
        self._mission_name: str = None
        self._destination: str = None
        self._launch_date: datetime = None
        self._duration_days: int = None
        self._crew: List[CrewMember] = None
        self._mission_status: str = None
        self._budget_millions: float = None

    def run_test(self) -> None:
        """Run one valid test and one invalid test"""

        try:
            print()
            print(" " + "-" * 60)
            print(color(7, ' 🚀 Exercise 2: Space Crew Management'))
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

            print()
            print(color(3, ' Testing Mission'))
            print(" " + "-" * 60)
            self._specific_test()
            # self.space_crew_management()
            print(' Uncomment to use')
            print()

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def space_crew_management(self) -> None:
        """Try to print the content of the class"""
        try:

            sm = SpaceMission(
                mission_id=self._mission_id,
                mission_name=self._mission_name,
                destination=self._destination,
                launch_date=self._launch_date,
                duration_days=self._duration_days,
                crew=self._crew,
                mission_status=self._mission_status,
                budget_millions=self._budget_millions,
                )

            # --- Print General Mission Info
            for k, v in sm.model_dump().items():
                if k == 'crew':
                    continue

                label = k.replace('_', ' ').title()

                if k == 'launch_date':
                    display_value = v.strftime("%Y-%m-%d %H:%M:%S")
                elif k == 'duration_days':
                    display_value = f'{v} days'
                elif k == 'budget_millions':
                    display_value = f'${v:,.2f}M'
                else:
                    display_value = str(v)

                print(f' {color(7, label):<30}{display_value}')

            # Print Crew List last
            print(f'\n {color(6, "Crew Members"):<30}')
            for member in sm.crew:
                # Format: Name (Rank) - Specialization [Exp: X years]
                member_info = (
                    f'{member.name} ({color(4, member.rank.value)}) '
                    f'- {member.specialization} '
                    f'[{member.years_experience} yrs exp]'
                )
                print(f' - {member_info}')

        except ValidationError as e:
            for error in e.errors():
                print(color(5, ' ERROR!') + f' {error["msg"]}')

    def _valid_test(self) -> None:

        try:
            mission = random.choice(list(Missions)).value

            crew_size = random.randint(3, 8)

            self._mission_id = mission[0]
            self._mission_name = mission[1]
            self._destination = mission[2]
            self._launch_date = datetime.now()
            self._duration_days = random.randint(1, 3650)
            self._crew = self._create_crew(crew_size)
            self._mission_status = 'ongoing'
            self._budget_millions = random.uniform(1.0, 10000.0)

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def _invalid_test(self) -> None:

        try:
            self._mission_id = None
            self._mission_name = None
            self._destination = None
            self._duration_days = None
            self._crew = None
            self._budget_millions = None

        except Exception as e:
            print(color(5, f' ERROR! {e}'))

    def _specific_test(self) -> None:
        self._mission_id = None
        self._mission_name = None
        self._destination = None
        self._launch_date = None
        self._duration_days = None
        self._crew = None
        self._mission_status = None
        self._budget_millions = None

    def _create_crew(self, crew_size: int) -> CrewMember:
        """Create crew members."""
        crew: list = []

        first_name = random.choice(list(FirstNames)).value
        last_name = random.choice(list(LastNames)).value
        m_id = (first_name[0] + last_name[:9]).lower()

        crew_member = CrewMember(
            member_id=m_id,
            name=f'{first_name} {last_name}',
            rank=random.choice([Rank.COMMANDER, Rank.CAPTAIN]),
            age=random.randint(18, 80),
            specialization=random.choice(list(Specializations)),
            years_experience=random.randint(0, 50),
            is_active=True,
        )

        crew.append(crew_member)

        for _ in range(crew_size - 1):
            first_name = random.choice(list(FirstNames)).value
            last_name = random.choice(list(LastNames)).value
            m_id = (first_name[0] + last_name[:9]).lower()

            crew_member = CrewMember(
                member_id=m_id,
                name=f'{first_name} {last_name}',
                rank=random.choice(list(Rank)),
                age=random.randint(18, 80),
                specialization=random.choice(list(Specializations)),
                years_experience=random.randint(0, 50),
                is_active=True,
            )

            crew.append(crew_member)

        return crew


# ----------------------------------------------------------------------------
#  Tester entry point
# ---------------------------------------------------------------------------

def cosmic_data() -> None:
    """Interactive UI for choice."""

    if sys.prefix == sys.base_prefix:
        print(color(5, ' ERROR! You must use a venv!'))
        print(' python3 -m venv .venv')
        print(' source .venv/bin/activate')
        print(' pip install -r requirements.txt')

    else:
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
            SpaceStationData().run_test()
        elif choice == "1":
            AlienContactLogs().run_test()
        elif choice == "2":
            SpaceCrewManagement().run_test()
        else:
            print(color(5, ' ERROR! Invalid choice! Please enter 0, 1, or 2'))


if __name__ == "__main__":
    cosmic_data()
