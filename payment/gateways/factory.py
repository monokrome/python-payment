from __future__ import annotations

import importlib
import re
from typing import Any

GATEWAY_NAME_CONVERSION_EXPRESSION = r"^\d+|\d+$|[^\w\d]|\s"


class GatewayFactory:
    def get_by_name(self, gateway_name: str) -> Any:
        gateway_classname = re.sub(
            GATEWAY_NAME_CONVERSION_EXPRESSION,
            "",
            gateway_name.title(),
        )

        return self.get_by_classname(gateway_classname)

    def get_by_classname(self, gateway_classname: str) -> Any:
        module_name = self.get_module_name(gateway_classname)
        gateway_modulename = "payment.gateways.%s" % module_name

        gateway_module = importlib.import_module(gateway_modulename)

        if hasattr(gateway_module, gateway_classname):
            return getattr(gateway_module, gateway_classname)
        else:
            raise NameError(
                'Module %s doesn\'t define "%s"'
                % (gateway_modulename, gateway_classname)
            )

    def get_module_name(self, class_name: str) -> str:
        return class_name.lower()
