import time
import unittest

from outage_reporter.outage_reporter import OutageReporter
from outage_reporter.utils import convert_string_to_datetime

from outage_reporter.tests.mocks import (
    MOCK_GET_SITE_INFO_RESPONSE, 
    MOCK_OUTAGE_START_TIME, 
    generate_outages
)


class TestReporterPerformance(unittest.TestCase):
    """
    OutageReporter local performance tests.
    """

    def test_get_outages_for_site_performance(self):
        
        outage_reporter = OutageReporter()
        one_million_outages = 1000000
        outages = generate_outages(one_million_outages)
        site_info = MOCK_GET_SITE_INFO_RESPONSE

        start = time.time()
        response = outage_reporter.get_outages_for_site(outages, site_info)
        end = time.time()
        time_taken = end - start

        self.assertEqual(len(response), one_million_outages)
        # assert time taken less than 1 second
        self.assertLess(time_taken, 1)

    def test_filter_outages_performance(self):
        outage_reporter = OutageReporter()
        one_million_outages = 1000000
        outages = generate_outages(one_million_outages)

        start_time = convert_string_to_datetime(MOCK_OUTAGE_START_TIME)
        start = time.time()
        response = outage_reporter.filter_outages(outages, start_time)
        end = time.time()
        time_taken = end - start

        self.assertEqual(len(response), one_million_outages)
        # assert time taken less than 1 second
        self.assertLess(time_taken, 1)
