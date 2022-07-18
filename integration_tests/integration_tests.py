#!/usr/bin/python3
import argparse
import unittest
import requests


class IntegrationTest(unittest.TestCase):
    protocol = 'http'
    host = 'localhost'
    
    def __request(self, method, path, *args, **kwargs):
        url = f'{self.protocol}://{self.host}/{path}'
        kwargs['timeout'] = (2.0, 60)
        kwargs.setdefault('headers', {})['User-Agent'] = 'Integration Test'
        resp = requests.request(method, url, *args, **kwargs)
        return resp

    def __assert_ok(self, resp):
        self.assertTrue(resp.ok, f'FAILED {resp.status_code} {resp.url}, \nResponse:\n: {resp.content}')
        print(resp.status_code, resp.request.method, resp.url, '\nResponse:\n', resp.content[0:128])

    def get(self, path, *args, **kwargs):
        resp = self.__request('GET', path, *args, **kwargs)
        self.__assert_ok(resp)
        return resp

    def head(self, path, *args, **kwargs):
        resp = self.__request('HEAD', path, *args, **kwargs)
        self.__assert_ok(resp)
        return resp
    

class TestAPI(IntegrationTest):

    test_users_path = 'users'
    test_posts_path = 'posts'

    def test_get_users(self):
        self.head(self.test_users_path)
        self.get(self.test_posts_path)

    def test_get_posts(self):
        self.head(self.test_users_path)
        self.get(self.test_posts_path)


    # TODO: test other HTTP methods POST, DELETE    



def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAPI))
    return suite


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test Live API')
    parser.add_argument('--host', default=IntegrationTest.host)
    parser.add_argument('--protocol', default=IntegrationTest.protocol, choices=['http', 'https'])

    for k, v in vars(parser.parse_args()).items():
        setattr(IntegrationTest, k, v)
    
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
