from __future__ import annotations

from typing import Any

from .errors import NoGatewayError
from .gateways.gateway import Gateway

NO_GATEWAY_ERROR_TEXT = "You must provide at least one gateway for processing"


class Transaction:
    gateways: list[Gateway]
    identifier: str | None
    success: bool | None

    def __init__(self) -> None:
        self.gateways = []
        self.identifier = None
        self.success = None

    def process(self, method: str = "") -> Any | None:
        if len(self.gateways) < 1:
            raise NoGatewayError(NO_GATEWAY_ERROR_TEXT)

        self.success = False

        for gateway in self.gateways:
            if hasattr(gateway, method):
                method_reference = getattr(gateway, method)
                gateway_transaction = method_reference(transaction=self)

                if gateway.success is True:
                    self.success = True
                    return gateway_transaction

        return None

    def charge(self) -> Any | None:
        return self.process(method="charge")

    def authorize(self) -> Any | None:
        return self.process(method="authorize")

    def credit(self) -> Any | None:
        return self.process(method="credit")

    def void(self) -> Any | None:
        return self.process(method="void")


class TransactionPool:
    transactions: list[Transaction]

    def __init__(self) -> None:
        self.transactions = []

    def process(self, method: str = "") -> None:
        for transaction in self.transactions:
            transaction.process(method)

    def charge(self) -> None:
        self.process("charge")

    def authorize(self) -> None:
        self.process("authorize")

    def credit(self) -> None:
        self.process("credit")

    def void(self) -> None:
        self.process("void")
