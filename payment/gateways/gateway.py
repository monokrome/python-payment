from __future__ import annotations

from typing import Any
from urllib.parse import urlencode
from urllib.request import urlopen

METHOD_NOT_IMPLEMENTED_MESSAGE = 'This gateway has not implemented the "%s" method.'


class Gateway:
    name: str | None = None
    success: bool = False

    def charge(self, **kwargs: Any) -> Any:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED_MESSAGE % "charge")

    def authorize(self, **kwargs: Any) -> Any:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED_MESSAGE % "authorize")

    def credit(self, **kwargs: Any) -> Any:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED_MESSAGE % "credit")

    def void(self, **kwargs: Any) -> Any:
        raise NotImplementedError(METHOD_NOT_IMPLEMENTED_MESSAGE % "void")

    def create_transaction(self, response: Any) -> Any:
        pass


class HTTPGateway(Gateway):
    use_https: bool = True
    request_url: str | None = None

    def send_request(self, data: dict[str, Any], url: str | None = None) -> Any:
        if url is None:
            url = self.request_url

        response = urlopen(url, urlencode(data).encode())  # type: ignore[arg-type]
        return self.create_transaction(response)

    def get_request_url(self) -> str:
        request_url = self.request_url or ""

        if self.use_https is True:
            return "https://" + request_url
        else:
            return "http://" + request_url
