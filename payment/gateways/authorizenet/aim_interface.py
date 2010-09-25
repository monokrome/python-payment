from payment.gateways import HTTPGateway

class AuthorizeNetAim(HTTPGateway):
    request_url = 'authorize.net/gateway/transact.dll'

