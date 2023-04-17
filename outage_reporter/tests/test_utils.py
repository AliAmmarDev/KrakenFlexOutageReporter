import unittest
from datetime import datetime as dt
import pytz
from outage_reporter.utils import convert_string_to_datetime
from outage_reporter.tests.mocks import MOCK_OUTAGE_START_TIME

class TestUtils(unittest.TestCase):
    """
    outage reporter utils tests.
    """
    def test_convert_string_to_datetime(self):

        # test invalid time
        string_time = MOCK_OUTAGE_START_TIME
        expected_response = dt(2022, 1, 1, 0, 0, 0, 0, pytz.UTC)

        response = convert_string_to_datetime(string_time)

        self.assertEqual(expected_response, response)

        # test invalid time
        string_time = "invalid_time"

        with self.assertRaises(Exception):
            response = convert_string_to_datetime(string_time)
