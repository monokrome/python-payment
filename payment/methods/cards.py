import re

CARD_TYPES: dict[str, str] = {
    "visa": r"^4\d{12}(\d{3})?$",
    "mastercard": r"^(5[1-5]\d{4}|677189)\d{10}$",
    "amex": r"^3[47][0-9]{13}$",
    "dinersclub": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
    "discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
    "jcb": r"^(?:2131|1800|35\d{3})\d{11}$",
}

CARD_VALIDATION_EXPRESSION = (
    r"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}"
    r"|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}"
    r"|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$"
)


class Card:
    type: str | None
    validated: bool
    cvv: str | None
    expiration: str | None
    _number: int | None

    def __init__(self) -> None:
        self.type = None
        self.validated = False
        self.cvv = None
        self.expiration = None
        self._number = None

    def guess_type(self, detection: bool = True) -> str | bool | None:
        if detection is True:
            for card_type in CARD_TYPES:
                if re.match(CARD_TYPES[card_type], str(self.number)):
                    self.type = card_type
                    self.validated = True
                    return card_type

        self.type = None

        if re.match(CARD_VALIDATION_EXPRESSION, str(self.number)):
            self.validated = True
        else:
            self.validated = False

        return self.validated

    def set_number(self, number: int) -> None:
        self._number = number
        self.guess_type()

    def get_number(self) -> int | None:
        return self._number

    number: int | None = property(get_number, set_number)  # type: ignore[assignment]

    def get_last_digits(self, count: int = 4, replacement_char: str | None = "X") -> str:
        final_result = str(self.number)[-count:]

        if replacement_char is not None:
            final_result = (((replacement_char * 4) + "-") * 3) + final_result

        return final_result

    def __str__(self) -> str:
        return self.get_last_digits()
