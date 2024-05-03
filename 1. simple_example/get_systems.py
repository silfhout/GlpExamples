# get_systems.py
# Created by Mark van Silfhout at 03/05/2024
# Copyright Hewlett Packard Enterprise Labs ©2024

import requests
import json

from get_token import get_token


def get_systems():
    token = get_token()
    url = "https://us1.data.cloud.hpe.com/private-cloud-business/v1beta1/system-software-catalogs"
    query = {}
    # query = {
    #     "select": "string",
    #     "filter": "string",
    #     "limit" : "10"
    # }

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, params=query)
    print(json.dumps(response.json(), indent=4, sort_keys=True))


if __name__ == '__main__':
    get_systems()
