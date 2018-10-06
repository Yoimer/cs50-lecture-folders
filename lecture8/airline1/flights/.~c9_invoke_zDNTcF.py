from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Airport, Flight

# Create your tests here.
class ModelsTestCase(TestCase):

    def setUp(self):
        # Create airports.
        Airport.objects.create(code="AAA", city="City A")
        Airport.objects.create(code="BBB", city="City B")


    def test_departures_count(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")

        # Create 3 flights departing from a1.
        for i in range(1, 4):
            Flight.objects.create(origin=a1, destination=a2, duration=100)

        self.assertEqual(a1.departures.count(), 3)


    def test_arrivals_count(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")

        # Create a flight arriving at a1.
        Flight.objects.create(origin=a2, destination=a1, duration=100)
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1)


    def test_invalid_destination(self):
        a = Airport.objects.get(code="AAA")
        with self.assertRaises(ValidationError):
            Flight.objects.create(origin=a, destination=a, duration=200)


    def test_zero_duration(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        with self.assertRaises(ValidationError):
            Flight.objects.create(origin=a1, destination=a2, duration=0)


    def test_negative_duration(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        with self.assertRaises(ValidationError):
            Flight.objects.create(origin=a1, destination=a2, duration=-100)