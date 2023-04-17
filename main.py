from outage_reporter import OutageReporter

if __name__ == "__main__":
    start_time = "2022-01-01T00:00:00.000Z"
    site_id = "norwich-pear-tree"
    outage_reporter = OutageReporter()
    outage_reporter.process(site_id, start_time)
