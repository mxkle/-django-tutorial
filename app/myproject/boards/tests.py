from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import boards

class BoardsTests(TestCase):
    def test_boards_view_status_code(self):
        url = reverse('boards')
        response = self.client.get(url)
        self.assertEquals(respone.status_code, 200)

    def test_index_url_resolves_home_view(self):
        view = resolve('/boards')
        self.assertEquals(view.func, boards)
