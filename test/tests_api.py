import unittest
from project_folder.web_app import app  # Assuming your project structure
from project_folder.api.models import PacketData  # Assuming models location


class TestPacketListAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_packets(self):
        # Simulate adding some test data
        PacketData.query.delete()  # Clear any existing data
        packet1 = PacketData(source_ip="192.168.1.1", destination_ip="8.8.8.8")
        packet2 = PacketData(source_ip="10.0.0.1", destination_ip="208.67.222.222")
        db.session.add(packet1)
        db.session.add(packet2)
        db.session.commit()

        # Send a GET request to the API endpoint
        response = self.app.get('/packets')

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Parse the response data (assuming JSON format)
        data = response.get_json()

        # Assert the number of returned packets
        self.assertEqual(len(data), 2)

        # Check some properties of the first packet
        self.assertEqual(data[0]["source_ip"], "192.168.1.1")
        self.assertEqual(data[0]["destination_ip"], "8.8.8.8")


if __name__ == '__main__':
    unittest.main()
