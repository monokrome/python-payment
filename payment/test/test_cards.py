import unittest
from payment.methods import cards

error_messages = {
    'validation_error': 'Could not validate accurate {0} test number: {1}',
    'detection_error': 'Could not detect accurate {0} test number: {1}',
    'invalid_card_error': 'Inaccurate card number considered accurate: {0}',
}

# Maps card types to valid test numbers
valid_card_numbers = {
    'visa': 4111111111111111,
    'mastercard': 5105105105105100,
    'amex': 378282246310005,
    'dinersclub': 30569309025904,
    'discover': 6011000990139424,
    'jcb': 3566002020360505,
}

invalid_card_number = 1234567812345678

class TestCards(unittest.TestCase):

    def test_card_number_updating(self):
        """" Tests whether or not the card number property is working right.
        """

        card = cards.Card()
        card.number = valid_card_numbers['visa']

        self.assertEquals(card.number, valid_card_numbers['visa'])

    def test_visa_validation(self):
        """ Tests whether or not visa cards are properly detected.

        """

        card = cards.Card()

        card.number = valid_card_numbers['visa']

        # Tests whether or not the card number was accurately validated
        self.assertTrue(card.validated,
            error_messages['validation_error'].format('visa', card.number))

        # Tests whether or not the card type was properly detected
        self.assertEqual(card.type, 'visa',
            error_messages['detection_error'].format('visa', card.number))

    def test_mastercard_validation(self):
        """ Tests whether or not american express cards are properly detected.

        """

        card = cards.Card()
        card.number = valid_card_numbers['mastercard']

        self.assertTrue(card.validated,
            error_messages['validation_error'].format('mastercard',
                                                      card.number))

        self.assertEquals(card.type, 'mastercard',
            error_messages['detection_error'].format('mastercard',
                                                     card.number))

    def test_american_express_validation(self):
        """ Tests whether or not american express cards are properly detected.

        """

        card = cards.Card()
        card.number = valid_card_numbers['amex']

        self.assertTrue(card.validated,
            error_messages['validation_error'].format('amex', card.number))

        self.assertEqual(card.type, 'amex',
            error_messages['detection_error'].format('amex', card.number))

    def test_dinersclub_validation(self):
        """ Tests whether or not diner's club cards are properly detected.

        """

        card = cards.Card()
        card.number = valid_card_numbers['dinersclub']

        self.assertTrue(card.validated,
            error_messages['validation_error'].format('dinersclub',
                                                      card.number))

        self.assertEquals(card.type, 'dinersclub',
            error_messages['detection_error'].format('dinersclub',
                                                     card.number))

    def test_discover_validation(self):
        """ Tests whether or not discover cards are properly detected.

        """

        card = cards.Card()
        card.number = valid_card_numbers['discover']

        self.assertTrue(card.validated,
            error_messages['validation_error'].format('discover',
                                                      card.number))

        self.assertEquals(card.type, 'discover',
            error_messages['detection_error'].format('discover',
                                                     card.number))

    def test_jcb_validation(self):
        """ Tests whether or not jcb cards are properly detected.

        """

        card = cards.Card()
        card.number = valid_card_numbers['jcb']

        self.assertTrue(card.validated,
            error_messages['validation_error'].format('jcb', card.number))

        self.assertEquals(card.type, 'jcb',
            error_messages['detection_error'].format('jcb',
                                                     card.number))

    def test_invalid_card_number(self):
        """ Tests whether or not card validation fails properly.

        """

        card = cards.Card()
        card.number = 1234567812345678

        self.assertFalse(card.validated,
            error_messages['invalid_card_error'].format(card.number))

    # TODO How do I test that undetectable card types work? As far as I
    # know, all card types are detected. And if I find one that isn't, why
    # wouldn't I detect it?
