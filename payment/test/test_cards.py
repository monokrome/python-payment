import unittest

from payment.methods import cards

ERROR_MESSAGES = {
    "validation_error": "Could not validate accurate {0} test number: {1}",
    "detection_error": "Could not detect accurate {0} test number: {1}",
    "invalid_card_error": "Inaccurate card number considered accurate: {0}",
    "wrong_last_digits": "Got last {0} digits of {1} as {2} instead of {3}.",
    "generic_validation_error": "Validating {0} failed without type detection.",
}

VALID_CARD_NUMBERS: dict[str, int] = {
    "visa": 4111111111111111,
    "mastercard": 5105105105105100,
    "amex": 378282246310005,
    "dinersclub": 30569309025904,
    "discover": 6011000990139424,
    "jcb": 3566002020360505,
}

INVALID_CARD_NUMBER = 1234567812345678


class TestCards(unittest.TestCase):
    def test_last_digits(self) -> None:
        card = cards.Card()
        card.number = 4111111111111111

        count = 4
        last_digits = card.get_last_digits(count=count, replacement_char="X")
        expected_digits = "XXXX-XXXX-XXXX-{0}".format(1111)

        self.assertEqual(
            last_digits,
            expected_digits,
            ERROR_MESSAGES["wrong_last_digits"].format(
                count, card.number, last_digits, expected_digits
            ),
        )

    def test_card_number_updating(self) -> None:
        card = cards.Card()
        card.number = VALID_CARD_NUMBERS["visa"]

        self.assertEqual(card.number, VALID_CARD_NUMBERS["visa"])

    def test_visa_validation(self) -> None:
        card = cards.Card()
        card.number = VALID_CARD_NUMBERS["visa"]

        self.assertTrue(
            card.validated,
            ERROR_MESSAGES["validation_error"].format("visa", card.number),
        )

        self.assertEqual(
            card.type,
            "visa",
            ERROR_MESSAGES["detection_error"].format("visa", card.number),
        )

    def test_mastercard_validation(self) -> None:
        card = cards.Card()
        card.number = VALID_CARD_NUMBERS["mastercard"]

        self.assertTrue(
            card.validated,
            ERROR_MESSAGES["validation_error"].format("mastercard", card.number),
        )

        self.assertEqual(
            card.type,
            "mastercard",
            ERROR_MESSAGES["detection_error"].format("mastercard", card.number),
        )

    def test_american_express_validation(self) -> None:
        card = cards.Card()
        card.number = VALID_CARD_NUMBERS["amex"]

        self.assertTrue(
            card.validated,
            ERROR_MESSAGES["validation_error"].format("amex", card.number),
        )

        self.assertEqual(
            card.type,
            "amex",
            ERROR_MESSAGES["detection_error"].format("amex", card.number),
        )

    def test_dinersclub_validation(self) -> None:
        card = cards.Card()
        card.number = VALID_CARD_NUMBERS["dinersclub"]

        self.assertTrue(
            card.validated,
            ERROR_MESSAGES["validation_error"].format("dinersclub", card.number),
        )

        self.assertEqual(
            card.type,
            "dinersclub",
            ERROR_MESSAGES["detection_error"].format("dinersclub", card.number),
        )

    def test_discover_validation(self) -> None:
        card = cards.Card()
        card.number = VALID_CARD_NUMBERS["discover"]

        self.assertTrue(
            card.validated,
            ERROR_MESSAGES["validation_error"].format("discover", card.number),
        )

        self.assertEqual(
            card.type,
            "discover",
            ERROR_MESSAGES["detection_error"].format("discover", card.number),
        )

    def test_jcb_validation(self) -> None:
        card = cards.Card()
        card.number = VALID_CARD_NUMBERS["jcb"]

        self.assertTrue(
            card.validated,
            ERROR_MESSAGES["validation_error"].format("jcb", card.number),
        )

        self.assertEqual(
            card.type,
            "jcb",
            ERROR_MESSAGES["detection_error"].format("jcb", card.number),
        )

    def test_invalid_card_number(self) -> None:
        card = cards.Card()
        card.number = 1234567812345678

        self.assertFalse(
            card.validated,
            ERROR_MESSAGES["invalid_card_error"].format(card.number),
        )

    def test_generic_validation(self) -> None:
        card = cards.Card()
        card.number = VALID_CARD_NUMBERS["visa"]
        self.assertTrue(
            card.guess_type(False),
            ERROR_MESSAGES["generic_validation_error"].format(card.number),
        )
