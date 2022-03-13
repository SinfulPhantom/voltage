from aiohttp import ClientResponse


class PyvoltException(Exception):
    """
    Base class for all Pyvolt exceptions. This could be used to catch all exceptions made from this library.
    """
    pass


class HTTPError(PyvoltException):
    """
    Exception that's raised when an HTTP request operation fails.

    Attributes
    ----------
    response: aiohttp.ClientResponse
        The response of the failed HTTP request. This is an
        instance of :class:`aiohttp.ClientResponse`.
    status: int
        The status code of the HTTP request.
    """

    def __init__(self, response: ClientResponse):
        self.response = response
        self.status: int = response.status
