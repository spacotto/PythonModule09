"""
Exercise 0: Space Station Data

Learn basic Pydantic model creation with BaseModel and
Field validation.
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
    from pydantic import BaseModel, Field, ValidationError
    from datetime import datetime
    from typing import Optional
    import sys

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
#  Space Station Data Validation
# ----------------------------------------------------------------------------

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():

    print()

    if sys.prefix == sys.base_prefix:
        print(color(5, ' ERROR! You must use a venv!'))
        print(' Help:')
        print(' python3 -m venv .venv')
        print(' source .venv/bin/activate')
        print(' pip install -r requirements.txt')

    else:
        print(color(3, ' Space Station Data Validation'))
        print(' ' + '=' * 40)

        try:
            # Create a valid space station instance
            v = SpaceStation(
                station_id='ISS001',
                name='International Space Station',
                crew_size=6,
                power_level=85.5,
                oxygen_level=92.3,
                last_maintenance='2026-04-13T12:00:00',
                )

            print(color(6, ' Valid station created!'))
            print()

            # Display the station information clearly
            print(f' {color(7, "ID"):<20}{v.station_id}')
            print(f' {color(7, "Name"):<20}{v.name}')
            print(f' {color(7, "Crew"):<20}{v.crew_size} people')
            print(f' {color(7, "Power"):<20}{v.power_level}%')
            print(f' {color(7, "Oxygen"):<20}{v.oxygen_level}%')

            if v.is_operational:
                status = color(2, 'Operational')
            else:
                status = color(1, 'Non-Operational')

            print(f' {color(7, "Status"):<20}{status}')

        except ValidationError as e:
            for error in e.errors():
                print(color(5, ' ERROR!' + f' {error["msg"]}'))

        print()
        print(' ' + '=' * 40)

        print(color(7, ' Expected validation error:'))

        # Attempt to create an invalid station
        try:
            SpaceStation(
                station_id="..",
                name=".",
                crew_size=25,
                power_level=-50.0,
                oxygen_level=-50.0,
                last_maintenance=datetime.now()
            )

        # Show the validation error message
        except ValidationError as e:
            for error in e.errors():
                print(color(5, ' ERROR!' + f' {error["msg"]}'))

    print()


if __name__ == "__main__":
    main()
