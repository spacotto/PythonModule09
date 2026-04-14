"""
Exercise 1: Alien Contact Logs

Master custom validation using @model_validator for
complex business rules.
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
    from typing import Optional, Self
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
#  Alien Contact Logs
# ----------------------------------------------------------------------------

class ContactType(Enum):
    RADIO = 'radio'
    VISUAL = 'visual'
    PHYSICAL = 'physical'
    TELEPATHIC = 'telepathic'


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType =Field (...)
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: : bool = Field(default=False)

    @model_validator(mode='after')
    def validate_cosmic_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC" Alien Contact')

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')

        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError('Telepathic contact requires at least 3 witnesses')

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError('Strong signals (>7.0) should include received messages')

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
        print(color(3, ' Space Station Data Validation'))
        print(' ' + '=' * 40)

        try:
            ac = AlienContact(
                    contact_id='AC_2024_001',
                    timestamp=datetime.now(),
                    location='Area 51, Nevada',
                    contact_type=radio,
                    signal_strength: float = Field(ge=0.0, le=10.0)
                    duration_minutes: int = Field(ge=1, le=1440)
                    witness_count: int = Field(ge=1, le=100)
                    message_received: Optional[str] = Field(default=None, max_length=500)
                    is_verified: : bool = Field(default=False)
                    )
        print(' ' + '=' * 40)

    print()


if __name__ == "__main__":
    main()
