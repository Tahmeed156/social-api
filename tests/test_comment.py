import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from api.models import Comment


@pytest.mark.django_db
class Testcomment:

    client: APIClient
    user: User


    def setup_method(self):
        self.client = APIClient()
        self.user, _ = User.objects.get_or_create(username='root')


    def teardown_method(self):
        self.user.delete()
  
    
    def test_comment_create(self, create_post):

        post = create_post

        form = {
            'body': 'Very informative post!',
            'user_id': self.user.id
        }

        response = self.client.post(f'/posts/{post.id}/comments/', data=form, format='json')
        post = Comment.objects.get(id=response.data.get('id'))

        assert response.status_code == 201, "Incorrect Response Code"
        for key, value in form.items():
            assert getattr(post, key) == value, f'{getattr(post, key)} != {value}'
