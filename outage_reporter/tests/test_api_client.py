import unittest
from unittest.mock import MagicMock

from outage_reporter.api_client import KrakenFlexAPI
from outage_reporter.config import BASE_URL


class TestAPIClient(unittest.TestCase):
    """
    API client unit tests
    """

    def test_base_url(self):
        api_client = KrakenFlexAPI()
        expected_response = BASE_URL

        response = api_client.base_url

        self.assertEqual(expected_response, response)

    def test_get_request(self):
        api_client = KrakenFlexAPI()
        api_client.session = MagicMock()
        api_client._http_request = MagicMock()

        api_client._get_request("test-url")

        api_client._http_request.assert_called_once()

    def test_post_request(self):
        api_client = KrakenFlexAPI()
        api_client.session = MagicMock()
        api_client._http_request = MagicMock()

        api_client._post_request("test-url", {})

        api_client._http_request.assert_called_once()

    def test_http_request(self):
        api_client = KrakenFlexAPI()
        api_client.session = MagicMock()
        api_client.session.get.return_value = MagicMock()
        api_client.session.post.return_value = MagicMock()
        api_client.session.get.status_code = 400
        api_client.session.post.status_code = 400

        with self.assertRaises(Exception):
            api_client._http_request("GET", "test-url")

        with self.assertRaises(Exception):
            api_client._http_request("POST", "test-url", {})
