from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase


class Test(TestCase):
    def test_index_page_are_loading(self):
        resp = self.client.get('/')
        self.assertTemplateUsed(resp, 'create_instance.html')

    def test_can_create_anime(self):
        user = User.objects.create(username='foo')
        user.set_password('qwertyuiop')
        user.save()

        self.client.login(username='foo', password='qwertyuiop')
        data = {
            'anime_name': 'Fullmetal Alchemist',
            'rating': '10/10',
            'watching': 'Finished',
            'user': [user.pk],
        }
        resp = self.client.post('/', data=data, follow=True)
        self.assertEqual(resp.status_code, HTTPStatus.OK)

        # Can see user's username on page
        self.assertContains(resp, 'foo')

        # Can see foo's anime on page
        self.assertContains(resp, 'Fullmetal Alchemist')
        self.assertContains(resp, '10/10')
        self.assertContains(resp, 'Finished')
