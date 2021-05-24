from http import HTTPStatus

from django.test import TestCase


class Test(TestCase):
    def test_index_page_are_loading(self):
        resp = self.client.get('/')
        self.assertTemplateUsed(resp, 'create_celebrity.html')

    def test_can_create_celebrity(self):
        data = {
            'first_name': 'Руслан',
            'second_name': 'Обрамович',
            'middle_name': 'Петрович',
            'country': 'UA',
        }
        resp = self.client.post('/', data=data, follow=True)

        self.assertEqual(resp.status_code, HTTPStatus.OK)
        for d in data.values():
            self.assertContains(resp, d)
