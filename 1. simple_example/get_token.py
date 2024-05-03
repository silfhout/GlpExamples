# get_token.py
# Created by Mark van Silfhout at 03/05/2024
# Copyright Hewlett Packard Enterprise Labs ©2024

from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session


def get_token() -> str:
    client = BackendApplicationClient('e21f3028-8097-4a4f-b491-a49b1d102d4a')
    oauth = OAuth2Session(client=client)
    auth = HTTPBasicAuth('e21f3028-8097-4a4f-b491-a49b1d102d4a', '05656940014f11ef9946a2408e898685')
    token = oauth.fetch_token(token_url='https://sso.common.cloud.hpe.com/as/token.oauth2', auth=auth)
    return token["access_token"]
