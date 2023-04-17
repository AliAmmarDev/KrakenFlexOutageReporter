import unittest

from outage_reporter.outage_reporter import OutageReporter


class TestReporterEndToEnd(unittest.TestCase):
    """
    OutageReporter end to end tests.
    """
    def test_process(self):
        start_time = "2022-01-01T00:00:00.000Z"
        site_id = "norwich-pear-tree"
        outage_reporter = OutageReporter()

        response = outage_reporter.process(site_id, start_time)

        self.assertEqual(response, {})
