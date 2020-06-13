from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

class TokenManager:

    def __init__(self, client_id: str, client_secret: str):
        self.__access_token = ""
        self.__client_id = client_id
        self.__client_secret = client_secret
    
    def is_token_valid(self):
        """The API does not provide for checking token validity"""
        return False
    
    async def fetch_access_token(self):
        auth = HTTPBasicAuth(self.__client_id, self.__client_secret)
        client = BackendApplicationClient(client_id=self.__client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url='https://api.srgssr.ch/oauth/v1/accesstoken?grant_type=client_credentials', auth=auth)
        self.__access_token = token["access_token"]

    async def save_access_token(self):
        raise NotImplementedError
    
    def get_access_token(self) -> str:
        return self.__access_token