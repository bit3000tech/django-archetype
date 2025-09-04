from django.test import TestCase
from django.urls import reverse
from .models import Person


class PersonModelTest(TestCase):
    """Test cases for the Person model"""
    
    def setUp(self):
        """Set up test data"""
        self.person = Person.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com"
        )
    
    def test_person_creation(self):
        """Test that a person can be created successfully"""
        self.assertEqual(self.person.first_name, "John")
        self.assertEqual(self.person.last_name, "Doe")
        self.assertEqual(self.person.email, "john.doe@example.com")
    
    def test_person_str_method(self):
        """Test the string representation of a person"""
        self.assertEqual(str(self.person), "John Doe")
    
    def test_person_full_name_property(self):
        """Test the full_name property"""
        self.assertEqual(self.person.full_name, "John Doe")
    
    def test_person_email_unique(self):
        """Test that email addresses must be unique"""
        with self.assertRaises(Exception):
            Person.objects.create(
                first_name="Jane",
                last_name="Smith",
                email="john.doe@example.com"  # Same email as setUp person
            )


class PersonViewTest(TestCase):
    """Test cases for Person views"""
    
    def setUp(self):
        """Set up test data"""
        self.person = Person.objects.create(
            first_name="Jane",
            last_name="Smith", 
            email="jane.smith@example.com"
        )
    
    def test_person_list_view(self):
        """Test the person list view"""
        url = reverse('sample:person_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Smith")
    
    def test_person_detail_view(self):
        """Test the person detail view"""
        url = reverse('sample:person_detail', kwargs={'pk': self.person.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Smith")
        self.assertContains(response, "jane.smith@example.com")
    
    def test_person_create_view_get(self):
        """Test the person create view (GET request)"""
        url = reverse('sample:person_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add Person")
    
    def test_person_create_view_post(self):
        """Test the person create view (POST request)"""
        url = reverse('sample:person_create')
        data = {
            'first_name': 'Bob',
            'last_name': 'Johnson',
            'email': 'bob.johnson@example.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Person.objects.filter(email='bob.johnson@example.com').exists())
