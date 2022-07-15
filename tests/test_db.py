import pytest
from django.core.management import call_command
from django.conf import settings

@pytest.mark.django_db
class TestDB:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_db(self):
        for k in settings.DATABASES.keys():
            print('\nTesting Database:', k)
            call_command('check', '--database', k, verbosity=3)