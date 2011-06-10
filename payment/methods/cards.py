import re

# A few cards that we can auto-determine
card_types = {
    'visa': '^4\d{12}(\d{3})?$',
    'mastercard': '^(5[1-5]\d{4}|677189)\d{10}$',
    'amex': '^3[47][0-9]{13}$',
    'dinersclub':  '^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
    'discover': '^6(?:011|5[0-9]{2})[0-9]{12}$',
    'jcb': '^(?:2131|1800|35\d{3})\d{11}$',
}

card_validation_expression  = '^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$'

class Card(object):
    type = None
    validated = False
    cvv = None
    expiration = None
    _number = None

    """ Represents a card that a payment can be made with. """
    def guess_type(self):
        """ Tries to guess the type of the card that has been provided. """

        for type in card_types:
            if re.match(card_types[type], str(self.number)):
                self.type = type
                self.validated = True
                return type

        self.type = None

        if re.match(card_validation_expression, str(self.number)):
            self.validated = True
        else:
            self.validated = False

        return self.validated

    def set_number(self, number):
        self._number = number
        self.guess_type()

    def get_number(self):
        return self._number

    number = property(get_number, set_number)

    def get_last_digits(self, count=4, replacement_char='X'):
        final_result = str(self.number)[-count:]

        if replacement_char is not None:
            final_result = (((replacement_char*4)+"-")*3) + final_result

        return final_result

    def __str__(self):
        return self.get_last_digits()
