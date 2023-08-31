import requests
import json

RETRIES = 5


def fetch_data(url, request_data, headers=None):
    curr_try = 1
    errors = []
    while curr_try < RETRIES:
        response = requests.post(url=url, json=request_data, headers=headers)
        response.raise_for_status()
        resp_data = response.json()
        if resp_data["status_code"] == 200:
            return resp_data

        if 'errors' in resp_data:
            errors.append(resp_data["errors"])
        curr_try += 1

    raise Exception(
        "Couldn't fetch requested data: {}".format(json.dumps(errors)))
