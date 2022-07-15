import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from api.models import Post


@pytest.mark.django_db
class TestPost:

    client: APIClient
    user: User


    def setup_method(self):
        self.client = APIClient()
        self.user, _ = User.objects.get_or_create(username='root')


    def teardown_method(self):
        self.user.delete()


    def test_post_create(self):

        form = {
            'title': 'Web3: The hype and how it can transform the internet',
            'body': 'As the internet has evolved, its influence on us has been profound, shaping everything ...',
            'user_id': self.user.id,
        }

        response = self.client.post('/posts/', data=form, format='json')
        post = Post.objects.get(id=response.data.get('id'))

        assert response.status_code == 201, "Incorrect Response Code"
        for key, value in form.items():
            assert getattr(post, key) == value, f'{getattr(post, key)} != {value}'
