import pytest
from api.models import Post
from django.contrib.auth.models import User


@pytest.fixture
def create_post():
    user_instance, _ = User.objects.get_or_create(username='jake')
    post_instance = Post(
        title='Web3: The hype and how it can transform the internet',
        body='As the internet has evolved, its influence on us has been profound, shaping everything ...',
        user=user_instance
    )
    post_instance.save()
    yield post_instance
    post_instance.delete()
