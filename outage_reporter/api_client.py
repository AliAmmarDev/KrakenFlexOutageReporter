import json
import requests
from requests.adapters import HTTPAdapter, Retry

from outage_reporter.config import API_KEY, BASE_URL

class KrakenFlexAPI:
    """
    KrakenFlex API client
    """

    @property
    def headers(self):
        """
        Request HTTP headers
        """
        return {
            "Content-Type": "application/json",
            "x-api-key": API_KEY
        }
    
    @property
    def base_url(self):
        """
        Request base url
        """
        base_url = BASE_URL
        return base_url

    def __init__(self):
        """
        Initialises HTTP session
        """
        self.session = self._get_session()

    def _get_session(self) -> requests.sessions.Session:
        """
        Get persistent HTTP session

        Returns:
        session (requests.sessions.Session): HTTP session.

        """

        session = requests.Session()
        session.headers = self.headers
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[500])
        adapter = HTTPAdapter(max_retries=retries)
        session.mount('https://', adapter)
        return session
    
    def _get_request(self, url: str) -> dict:
        """
        Performs HTTP GET request

        Parameters:
        url (str): HTTP request url

        Returns:
        response (dict): GET response body json.

        """

        response = self._http_request("GET", url)
        return response

    def _post_request(self, url: str, data: str) -> dict:
        """
        Performs HTTP POST request

        Parameters:
        url (str): HTTP request url
        data (str)(optional): HTTP request data in json format

        Returns:
        response (dict): POST response body.

        """

        response = self._http_request("POST", url, data)
        return response
    
    def _http_request(self, method: str, url: str, data: str=None ) -> dict:
        """
        Performs HTTP request

        Parameters:
        method (str): HTTP request method.
        url (str): HTTP request url
        data (json)(optional): HTTP request data

        Returns:
        response (dict): HTTP response body in json format.

        """

        if method == "GET":
            response = self.session.get(url)
        elif method == "POST":
            response = self.session.post(url, data)

        if response.status_code != 200:
            raise Exception(
                f"API call failed. Response: {response.status_code} Message: {response.text}"
            )
        return response.json()
   
    def get_outages(self) -> dict:
        """
        Gets outages on the system from get outages endpoint.

        Returns:
        response (dict): get outages response body.

        """

        path = "outages"
        url = f"{self.base_url}/{path}"
        response = self._get_request(url)
        return response

    def get_site_info(self, site_id: str) -> dict:
        """
        Gets information for a specified site from get site info endpoint.

        Parameters:
        site_id (str): ID for a site.

        Returns:
        response (dict): get site info response body.

        """

        path = f"site-info/{site_id}"
        url = f"{self.base_url}/{path}"
        response = self._get_request(url)
        return response

    def post_site_outages(self, site_id: str, outages: list) -> dict:
        """
        Posts outages for a specified site to post site outages endpoint.

        Parameters:
        site_id (str): ID for a site.
        outages (list): List of outages.

        Returns:
        response (dict): post site outages response body.

        """

        path = f"site-outages/{site_id}"
        url = f"{self.base_url}/{path}"
        data = json.dumps(outages)
        response = self._post_request(url, data)
        return response
