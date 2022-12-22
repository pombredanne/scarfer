import unittest

CAIRO_REPORT="example-data/scancode/no-format/cairo-1.16.0-scan.json"

from scarfer.format.factory import FormatFactory
from scarfer.scan_interface import ScanReportReader


class TestScancodeReader(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestScancodeReader, self).__init__(*args, **kwargs)

    def test_reader(self):
        reader = ScanReportReader(CAIRO_REPORT)
        self.assertIsNotNone(reader)

    def test_formatter(self):
        formatter = FormatFactory.formatter("json")
        self.assertIsNotNone(formatter)
        formatter = FormatFactory.formatter("JSON")
        self.assertIsNotNone(formatter)

if __name__ == '__main__':
    unittest.main()
