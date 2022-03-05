from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class AuthorViewTestCase(TestCase):

    def test_status_code_200(self):
        response = self.client.get(reverse('author_view'))
        self.assertEquals(response.status_code, 200)

    def test_template_usado(self):
        response = self.client.get(reverse('author_view'))
        self.assertTemplateUsed(response, 'author_view.html')