import requests

""" Met Office DataPoint API reference guide:
https://www.metoffice.gov.uk/services/data/datapoint/api-reference
"""

MET_OFFICE_BASE_URL: str = "http://datapoint.metoffice.gov.uk/public/data"
IP_INFO_URL: str = "http://ipinfo.io/json"


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


def get_ip_geo_data(adapter=requests_adapter):
    url = IP_INFO_URL
    return adapter(url)


def get_met_office_data(endpoint: str, apikey: str, adapter=requests_adapter):
    url = create_url_from_endpoint(endpoint, apikey)
    return adapter(url)


def create_url_from_endpoint(endpoint: str, apikey: str) -> str:
    key_prefix: str = "&" if "?" in endpoint else "?"
    url: str = f"{MET_OFFICE_BASE_URL}/{endpoint}{key_prefix}key={apikey}"
    return url


def create_forecast_endpoint(location_id: str, time_step: str) -> str:
    endpoint = f"val/wxfcs/all/json/{location_id}?res={time_step}"
    return endpoint


def locations_endpoint():
    endpoint = "val/wxfcs/all/json/sitelist"
    return endpoint
