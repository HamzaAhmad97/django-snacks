from django.test import TestCase
from django.urls import reverse

class TestSnacks(TestCase):
    def test_home_status_code(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_status_code(self):
        url = reverse("about")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'snacks/home.html')

    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'snacks/about.html')