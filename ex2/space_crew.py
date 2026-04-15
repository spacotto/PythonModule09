"""
Exercise 2: Space Crew Management

Master nested Pydantic models and complex data
relationships.
"""


# ----------------------------------------------------------------------------
#  Visual helpers
# ----------------------------------------------------------------------------

def color(code: int, text: str) -> str:
    """A function making strings of text colorful."""
    colors: dict = {
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
#  Imports
# ----------------------------------------------------------------------------

try:
    import sys
    from pydantic import BaseModel, Field, ValidationError, model_validator
    from datetime import datetime
    from typing import List, Optional, Self
    from enum import Enum

except ModuleNotFoundError as e:
    print()
    print(color(5, f' ERROR! {e}'))
    print(' Try the following commands:')
    print(' python3 -m venv .venv')
    print(' source .venv/bin/activate')
    print(' pip install -r requirements.txt')
    print()
    exit()


# ----------------------------------------------------------------------------
#  Space Mission Crew Validationw
# ----------------------------------------------------------------------------

class Rank(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> Self:

        # Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # Must have at least one Commander or Captain
        has_command = any(member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
                          for member in self.crew)

        if not has_command:
            raise ValueError('Mission must have at least one Commander or Captain')

        # Long missions (> 365 days) need 50% experienced crew (5+ years)
        if duration_days > 365:
            ec = sum(1 for member in self.crew if member.years_experience >= 5)
            if ec / len(self.crew) < 0.5:
                raise ValueError('Long missions (> 365 days) need '
                                 '50% experienced crew (5+ years)')

        # All crew members must be active
        for member in self.crew:
            if not member.is_active:
                raise ValueError(f'{member.name} is not active.'
                                 ' All crew members must be active')

        return self

def main() -> None:
    print()

    if sys.prefix == sys.base_prefix:
        print(color(5, ' ERROR! You must use a venv!'))
        print(' Help:')
        print(' python3 -m venv .venv')
        print(' source .venv/bin/activate')
        print(' pip install -r requirements.txt')

    else:
        print(color(3, ' Space Mission Crew Validation'))
        print(' ' + '=' * 40)

        try:
            sarah_connor = CrewMember(member_id='sconnor',
                                      name='Sarah Connor',
                                      rank=Rank.COMMANDER,
                                      age=19,
                                      specialization='Mission Command',
                                      years_experience=10,
                                      is_active=True)

            john_smith = CrewMember(member_id='jsmith',
                                    name='John Smith',
                                    rank=Rank.LIEUTENANT,
                                    age=30,
                                    specialization='Navigation',
                                    years_experience=5,
                                    is_active=True)

            alice_johnson = CrewMember(member_id='ajohnson',
                                       name='Alice Johnson',
                                       rank=Rank.OFFICER,
                                       age=20,
                                       specialization='Engineering',
                                       years_experience=3,
                                       is_active=True)

            crew_list: List[CrewMember] = [sarah_connor,
                                           john_smith,
                                           alice_johnson]

            sm = SpaceMission(
                    mission_id='M2024_MARS',
                    mission_name='Mars Colony Establishment',
                    destination='Mars',
                    launch_date=datetime.now(),
                    duration_day=900,
                    crew=crew_list,
                    mission_status='',
                    budget_millions=2500.0,
                    )

            print(color(6, ' Valid mission created!\n'))
            print(f' {color(7, "Mission"):<25}{sm.mission_name}')
            print(f' {color(7, "ID"):<25}{sm.mission_id}')
            print(f' {color(7, "Destination"):<25}{sm.destination}')
            print(f' {color(7, "Duration"):<25}{sm.duration_day}')
            print(f' {color(7, "Budget"):<25}{sm.budget_millions}')
            print(f' {color(7, "Crew size"):<25}{len(sm.crew)}')
            print(f' {color(7, "Crew members")}')

        except ValidationError as e:
            for error in e.errors():
                print(f' {error["msg"]}')

        print()
        print(' ' + '=' * 40)
        print(color(5, ' Expected validation error:'))

        try:

            crew_list: List[CrewMember] = [alice_johnson]

            SpaceMission(
                    mission_id='M2024_MARS',
                    mission_name='Mars Colony Establishment',
                    destination='Mars',
                    launch_date=datetime.now(),
                    duration_day=900,
                    crew=crew_list,
                    mission_status='',
                    budget_millions=2500.0,
                    )

        except ValidationError as e:
            for error in e.errors():
                print(f' {error["msg"]}')

    print()


if __name__ == "__main__":
    main()
