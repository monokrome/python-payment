from errors import NoGatewayError

no_gateway_error_text = 'You must provide at least one gateway for processing'

class Transaction(object):
    gateways = []
    identifier = None
    success = None

    def process(self, method=None):
        """ Performs an arbitrary type of processing through the gateway(s). """
        if len(self.gateways) < 1:
            raise NoGatewayError(no_gateway_error_text)

        self.success = False

        for gateway in self.gateways:
            if hasattr(gateway, method):
                method_reference = getattr(gateway, method)
                gateway_transaction = method_reference(transaction=self)

                if gateway.success == True:
                    self.success = True
                    return gateway_transaction

    def charge(self, gateway=None):
        """ Starts the process of transfering the funds from our payment
            method through our gateway. """
        return self.process(gateway=gateway, method='charge')

    def authorize(self, gateway=None):
        """ An authorization is made in order to check whether the funds
            are available without actually charging the card. """
        return self.process(gateway=gateway, method='authorize')

    def credit(self):
        """ Credits an amount of money back to the method of payment. """
        return self.process(gateway=gateway, method='credit')

    def void(self):
        """ Cancels a transactions.. """
        return self.process(gateway=gateway, method='void')

class TransactionPool(object):
    """ Manages a list of transactions that need to be processed in the same way. """
    transactions = []

    def process(self, method=None):
        for transaction in transactions:
            transaction.process(self, method)

    def charge(self, gateway=None):
        return self.process('charge')

    def authorize(self, gateway=None):
        return self.process('authorize')

    def credit(self, gateway=None):
        return self.process('credit')

    def void(self, gateway=None):
        return self.process('void')

