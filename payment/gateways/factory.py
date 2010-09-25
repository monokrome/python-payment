from exceptions import ImportError, NameError
import re

gateway_name_conversion_expression = '/^\s+|^\d+|[^\w\d]|\s$/'

class GatewayFactory(object):
    """ Used to recieve gateway objects based with directly importing. """

    @staticmethod
    def get_by_name(gateway_name):
        """ Gets a gateway object based on the gateway's real name. """
        gateway_classname = re.sub(gateway_name_conversion_expression, '',
            gateway_name.title()
        )

        # TODO: Figure out how to import this relative
        gateway_modulename = 'payment.gateways.%s' % gateway_classname.lower()

        gateway_module = __import__(
                   gateway_modulename,
                   globals(), locals(),
                   gateway_classname, -1
        )

        if hasattr(gateway_module, gateway_classname):
            gateway_object = getattr(gateway_module, gateway_classname)

            return gateway_object
        else:
            raise NameError('Module %s for "%s" doesn''t define "%s"' %
                       (gateway_modulename, gateway_name, gateway_classname)
                           )

