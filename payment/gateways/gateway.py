from exceptions import NotImplementedError
import urllib

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

    def create_transaction(response):
        """ Takes a gateway transaction response and converts it into a
            Transaction object containing response data. """

class HTTPGateway(Gateway):
    """ A gateway that is communicated with over the HTTP or HTTPS protocol. """
    use_https = True
    request_url = None

    def send_request(self, data, url=None):
        """ Send a requet to the gateway over HTTP. """
        if url is None:
             url = self.request_url

        response = urllib.urlopen(url, urllib.urlencode(data))
        return self.create_transaction(response)

    def get_request_url(self):
        """ Gets the URL that should be used to make a decision on this gateway. """
        request_url = self.request_url

        if self.use_https is False:
            request_url = 'https://' + request_url
        else:
            request_url = 'http://' + request_url

        return request_url

