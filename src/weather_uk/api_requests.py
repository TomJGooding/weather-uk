import requests

""" Met Office DataPoint API reference guide:
https://www.metoffice.gov.uk/services/data/datapoint/api-reference
"""

BASE_URL: str = "http://datapoint.metoffice.gov.uk/public/data"


def requests_adapter(url: str):
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(http_err)
    except requests.exceptions.ConnectionError as cxn_err:
        print(cxn_err)
    except requests.exceptions.Timeout as timeout_err:
        print(timeout_err)
    except requests.exceptions.RequestException as req_err:
        print(req_err)


def create_url_from_endpoint(endpoint: str, apikey: str) -> str:
    key_prefix: str = "&" if "?" in endpoint else "?"
    url: str = f"{BASE_URL}/{endpoint}{key_prefix}key={apikey}"
    return url


def create_forecast_endpoint(location_id: str, time_step: str) -> str:
    endpoint = f"val/wxfcs/all/json/{location_id}?res={time_step}"
    return endpoint


def get_data(endpoint: str, apikey: str, adapter=requests_adapter):
    url = create_url_from_endpoint(endpoint, apikey)
    return adapter(url)
