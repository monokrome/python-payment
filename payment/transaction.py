class Transaction(object):
    gateways = []
    identifier = None
    success = None

    def charge(self):
        """ Starts the process of transfering the funds from our payment
            method through our gateway. """
        pass

    def authorize(self):
        """ An authorization is made in order to check whether the funds
            are available without actually charging the card. """
        pass

    def credit(self):
        """ Credits an amount of money back to the method of payment. """
        pass

    def void(self):
        """ Cancels a transactions.. """
        pass

