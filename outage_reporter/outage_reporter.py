from datetime import datetime

from outage_reporter.api_client import KrakenFlexAPI
from outage_reporter.utils import convert_string_to_datetime


class OutageReporter:
    """
    Class used to report outages on kraken platform
    """

    def __init__(self):
        """
        Initialises API ression to the KrakenFlex API
        """

        self.kraken_flex_api = KrakenFlexAPI()

    def process(self, site_id, start_time):
        """
        Report outages for a specified site.

        Parameters:
        site_id (str): ID for a site.
        start_time (str): start time for filtering outages.

        Returns:
        outages_reported (list): List of outages that happened on
            a specific site from the specified time.

        """

        print(f"Reporting {site_id} outages beginning after {start_time} starting...")

        start_time = convert_string_to_datetime(start_time)

        outages = self.get_outages()

        site_info = self.get_site_info(site_id=site_id)

        site_outages = self.get_outages_for_site(outages, site_info)

        filtered_site_outages = self.filter_outages(site_outages, start_time)

        outages_reported = self.post_site_outages(site_id, filtered_site_outages)

        print(f"Reported {len(filtered_site_outages)} {site_id} outages.")

        return outages_reported

    def get_outages(self) -> list:
        """
        Gets all outages on the system.

        Returns:
        outages (list): List of outages on the system.

        """

        outages = self.kraken_flex_api.get_outages()
        return outages

    def get_site_info(self, site_id: str) -> dict:
        """
        Gets information for a specified site.

        Parameters:
        site_id (str): ID for a site.

        Returns:
        site_info (dict): Information for a specified site.

        """

        site_info = self.kraken_flex_api.get_site_info(site_id)
        return site_info
    
    def get_outages_for_site(self, outages: list, site_info: dict) -> list:
        """
        Filters outages happening on a specified site.

        Parameters:
        outages (list): List of outages.
        site_info (dict): Information for a site.

        Returns:
        site_outages (list): List of outages happening on a specified site.

        """

        devices = dict((device["id"], device["name"]) for device in site_info["devices"])
        site_outages = [
            dict(outage, **{"name":devices.get(outage["id"])}) for outage in outages if outage.get("id", "") in devices
        ]
        return site_outages

    def filter_outages(self, outages: list, start_time: datetime) -> list:
        """
        Filters outages beginning after a specified start time.

        Parameters:
        outages (list): List of outages.
        start_time (datetime): start time for filtering outages.

        Returns:
        filtered_outages (list): List of outages starting after specified start time.

        """

        filtered_outages = [
            outage for outage in outages if convert_string_to_datetime(outage["begin"]) >= start_time
        ]
        return filtered_outages

    def post_site_outages(self, site_id: str, outages: list) -> dict:
        """
        Posts outages for a specific site.

        Parameters:
        site_id (str): ID for a site.
        outages (list): List of outages.

        Returns:
        response (dict): post site outages response body.

        """

        response = self.kraken_flex_api.post_site_outages(site_id, outages)
        return response
