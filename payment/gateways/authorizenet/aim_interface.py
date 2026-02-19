from payment.gateways.gateway import HTTPGateway


class AuthorizeNetAim(HTTPGateway):
    request_url: str | None = "authorize.net/gateway/transact.dll"
