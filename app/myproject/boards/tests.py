from django.core.urlresolvers import reverse
from django.test import TestCase

class HomeTests(TestCase):
    def test_index_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(respone.status_code, 200)

    def test_index_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, index)
