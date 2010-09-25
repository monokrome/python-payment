from exceptions import NotImplementedError

method_not_implemented_message = 'This gateway has not implemented the \"%s\" method.'

class Gateway(object):
    """ A generic interface that gateways should extend. """
    name = None

    def charge(self):
        """ Charges the account for the transaction. """
        raise NotImplementedError(method_not_implemented_message % 'charge')

    def authorize(self):
        """ Verifies that the funds are available to charge the
            transaction at a later time. """
        raise NotImplementedError(method_not_implemented_message % 'authorize')

    def credit(self):
        """ Credits a specified amount to the transaction. """
        raise NotImplementedError(method_not_implemented_message % 'credit')

    def void(self):
        """ Voids the transaction. """
        raise NotImplementedError(method_not_implemented_message % 'void')


