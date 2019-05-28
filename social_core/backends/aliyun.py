"""
Aliyun Ram OAuth2 backend, docs at:
    https://python-social-auth.readthedocs.io/en/latest/backends/amazon.html
"""
from .oauth import BaseOAuth2


class AliyunOAuth2(BaseOAuth2):
    name = 'aliyun'
    ID_KEY = 'user_id'
    AUTHORIZATION_URL = 'https://signin.aliyun.com/oauth2/v1/auth'
    ACCESS_TOKEN_URL = 'https://oauth.aliyun.com/v1/token'
    DEFAULT_SCOPE = ['openid', 'aliuid', 'profile']
    ACCESS_TOKEN_METHOD = 'POST'

    def get_user_details(self, response):
        return {
            'username': response['email'].split('@')[0],
            'email': response['email'],
            'fullname': response['name'],
        }

    def user_data(self, access_token, *args, **kwargs):
        """Grab user profile information from aliyun."""
        response = self.get_json('https://oauth.aliyun.com/v1/userinfo',
                                 params={'access_token': access_token})
        response = {
            'user_id': response['uid'],
            'name': response['name'],
            'email': response['upn']
        }
        return response
