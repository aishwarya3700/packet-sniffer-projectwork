import unittest
from unittest.mock import patch

from project_folder.packet_capture import capture_packets  # Assuming function location


class TestPacketCapture(unittest.TestCase):

    @patch('scapy.sniff')  # Patch the scapy.sniff function for controlled testing
    def test_capture_packets(self, mock_sniff):
        # Define expected captured packets (replace with your format)
        expected_packets = [
            {'source_ip': '10.0.0.2', 'destination_ip': '172.16.0.1'},
            {'source_ip': '8.8.8.8', 'destination_ip': '192.168.1.2'},
        ]

        # Mock the scapy.sniff behavior (replace with actual capture logic)
        mock_sniff.return_value = expected_packets

        # Call the capture_packets function
        captured_packets = capture_packets(timeout=1)  # Adjust timeout as needed

        # Assert that the captured packets match the expected ones
        self.assertEqual(captured_packets, expected_packets)


if __name__ == '__main__':
    unittest.main()
