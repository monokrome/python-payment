__all__ = ['Gateway', 'GatewayFactory',]

from exceptions import NotImplementedError, ImportError, NameError
import re

gateway_name_conversion_expression = '/^\s+|^\d+|[^\w\d]|\s$/'

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

class GatewayFactory(object):
    """ Used to recieve gateway objects based with directly importing. """

    @staticmethod
    def get_by_name(gateway_name):
        """ Gets a gateway object based on the gateway's real name. """
        gateway_classname = re.sub(gateway_name_conversion_expression, '',
            gateway_name.title() # CamelCased. That's right, fool.
        )

        # TODO: Figure out how to import this relative
        gateway_modulename = 'payment.gateways.%s' % gateway_classname.lower()

        gateway_module = __import__(
                   gateway_modulename,
                   globals(), locals(),
                   -1
        )

        if hasattr(gateway_module, gateway_classname):
            gateway_object = getattr(gateway_module, gateway_classname)

            return gateway_object
        else:
            raise NameError('Module %s for "%s" doesn''t define "%s"' %
                       (gateway_modulename, gateway_name, gateway_classname)
                           )

