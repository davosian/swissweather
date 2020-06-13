from aiohttp import ClientSession

from .AbstractAuth import AbstractAuth
from .TokenManager import TokenManager


class Auth(AbstractAuth):
    def __init__(self, websession: ClientSession, host: str, token_manager: TokenManager):
        """Initialize the auth."""
        super().__init__(websession, host)
        self.token_manager = token_manager

    async def async_get_access_token(self) -> str:
        """Return a valid access token."""
        if self.token_manager.is_token_valid():
            return self.token_manager.get_access_token()

        await self.token_manager.fetch_access_token()
        # await self.token_manager.save_access_token()

        return self.token_manager.get_access_token()