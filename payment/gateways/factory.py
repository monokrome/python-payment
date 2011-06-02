from exceptions import ImportError, NameError
import re

gateway_name_conversion_expression = '/^\d+|^\d+|[^\w\d]|\s$/'

class GatewayFactory(object):
    """ Used to recieve gateway objects easily without explicit importing. """

    def get_by_name(self, gateway_name):
        """ Gets a gateway object based on the gateway's real name. """
        gateway_classname = re.sub(gateway_name_conversion_expression, '',
            gateway_name.title()
        )

        return self.get_by_classname(gateway_classname)

    def get_by_classname(self, gateway_classname):
        """ Returns a gateway class based on the provided class name """
        module_name = self.get_module_name(gateway_classname)

        gateway_modulename = 'payment.gateways.%s' % self.get_module_name(gateway_classname)

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

    def get_module_name(self, class_name):
        """ Takes a classname and returns a module name for that class name """
        return class_name.lower()
