import unittest
from city_functions import get_location_name

class LocationTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    def test_city_country(self):
        location = get_location_name('santiago', 'chile', '500000')
        self.assertEqual(location, 'Santiago, Chile - Population 500000')

if __name__ == '__main__':
    unittest.main()

