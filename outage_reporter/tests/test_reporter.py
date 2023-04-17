import unittest
from unittest.mock import MagicMock

from outage_reporter.outage_reporter import OutageReporter
from outage_reporter.utils import convert_string_to_datetime

from outage_reporter.tests.mocks import (
    MOCK_GET_OUTAGES_RESPONSE,
    MOCK_GET_SITE_INFO_RESPONSE,
    MOCK_FILTERED_OUTAGES,
    MOCK_SITE_OUTAGES,
    MOCK_OUTAGE_START_TIME
)


class TestReporter(unittest.TestCase):
    """
    OutageReporter unit tests.
    """

    def test_get_outages(self):
        outage_reporter = OutageReporter()
        outage_reporter.kraken_flex_api = MagicMock()
        expected_response = MOCK_GET_OUTAGES_RESPONSE
        outage_reporter.kraken_flex_api.get_outages.return_value = MOCK_GET_OUTAGES_RESPONSE

        response = outage_reporter.get_outages()

        self.assertEqual(expected_response, response)

    def test_get_site_info(self):
        outage_reporter = OutageReporter()
        outage_reporter.kraken_flex_api = MagicMock()
        expected_response = MOCK_GET_SITE_INFO_RESPONSE
        outage_reporter.kraken_flex_api.get_site_info.return_value = MOCK_GET_SITE_INFO_RESPONSE

        response = outage_reporter.get_site_info("test-site-id")

        self.assertEqual(expected_response, response)

    def test_post_site_outages(self):
        outage_reporter = OutageReporter()
        outage_reporter.kraken_flex_api = MagicMock()
        expected_response = {}
        outage_reporter.kraken_flex_api.post_site_outages.return_value = {}

        response = outage_reporter.post_site_outages("test-site-id", [])

        self.assertEqual(expected_response, response)

    def test_get_outages_for_site(self):
        outage_reporter = OutageReporter()
        outages = MOCK_GET_OUTAGES_RESPONSE
        site_info = MOCK_GET_SITE_INFO_RESPONSE

        site_outages = outage_reporter.get_outages_for_site(outages, site_info)

        self.assertCountEqual(site_outages, MOCK_SITE_OUTAGES)

    def test_filter_outages(self):
        outage_reporter = OutageReporter()
        outages = MOCK_SITE_OUTAGES
        start_time = convert_string_to_datetime(MOCK_OUTAGE_START_TIME)

        response = outage_reporter.filter_outages(outages, start_time)

        self.assertCountEqual(response, MOCK_FILTERED_OUTAGES)
