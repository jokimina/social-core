import json

from social_core.tests.backends.oauth import OAuth2Test


class AliyunOAuth2Test(OAuth2Test):
    backend_path = 'social_core.backends.aliyun.AliyunOAuth2'
    user_data_url = 'https://oauth.aliyun.com/v1/userinfo'
    expected_username = '付小东'
    access_token_body = json.dumps({
        "scope": "aliuid openid profile",
        "request_id": "2decd07f-c9e1-4116-90dd-e5d4b9931c3f",
        "access_token": "eyJhbGciOiJSUzI1NiIsImsyaWQiOiJlNE92NnVOUDhsMEY2RmVUMVhvek5wb1NBcVZLblNGRyIsImtpZCI6IkpDOXd4enJocUowZ3RhQ0V0MlFMVWZldkVVSXdsdEZodWk0TzFiaDY3dFUifQ.dnFMTkV6S2VFOHZPbEhEanQ4dldIMldzNW45cFBOSWdNRDh0QU9hVmZDMzdVY29qMEJmUTZTWGl3SE9LcHBiZkorUGdvclh5Ry8xTDYyN1JmU3ZPVWdabU1YZUZSVG80dU0rUVFKdDFSY2VRM3F2OWtSM1ZQLzRUdGhLZ1lsaHVLdlpaMzZoTzYvcmtxdHVDU3VqVUJJWlVnU1I2RmFBb0d3eHdWMW5SUEo2UnN0THpwVU1pVHN1ZFhNUTJaeFViVVloSVkvNm83d1lSeENTQittWlh4NkhFU09EYjJ1TlRSS0NROTJHL3h5R1Q3NjlpQXc9PQ.FAN3vIgNiSLEg6OnGLLipCuEAHyWpX5DxF2offBVZSpsqtDPYwUdQfx-lc3pQZfGpzWgBil39sVcaerXbUJdN531vxUTqDeJJ9Jg_JNf-mxhd8PylR3DICoV1ZwrAQ4tdnjdvWIbjx9cmcHrb_d92AjOEXFsoyjOBoKaROt3wH1gvrMjh5bY7zDpcMsUIIFYDjvrHmKHKNd2A1cI25PktfMKyM-6nck3tQwTeIHAXpe__wUTY4297Cdz2fVMOsvSHj5m994hOE6eVK-kNV9b6EAqsFlp4_f0TwM2VLZPt1cy9Jlm0TqTPhWCc8YjiSKeOVTJVfrESNXFVcloPnbXbQ",
        "token_type": "Bearer",
        "refresh_token": "xgbWZdMpS25CM6Z1",
        "id_token": "eyJraWQiOiJKQzl3eHpyaHFKMGd0YUNFdDJRTFVmZXZFVUl3bHRGaHVpNE8xYmg2N3RVIiwiYWxnIjoiUlMyNTYifQ.eyJhdWQiOiI0NDM0NDQwNTU3ODIzODQ2MjU3Iiwic3ViIjoicjMwbVpYNmU0clRIM215bHlIN0FFajZ1IiwidWlkIjoiMjkwMzY4NDY3Njk0MDY4NTgzIiwidXBuIjoiZnV4aWFvZG9uZ0BjYXNoYnVzLm9uYWxpeXVuLmNvbSIsImlzcyI6Imh0dHBzOlwvXC9vYXV0aC5hbGl5dW4uY29tIiwibmFtZSI6IuS7mOWwj-S4nCIsImV4cCI6MTU1ODkzMjQ4OCwiYmlkIjoiMjY4NDIiLCJpYXQiOjE1NTg5Mjg4ODgsImFpZCI6IjE3MjY3MDgyNzk1ODkyNjkifQ.aI1PD4QjdM_B4u3Oga1fNcr_GwpAkOHng7HGqr5BHj96_JJGB5EIWtE05EEvS5mmp5XV203_yYPFWZMvH4Edq7o7a-KbtVOOiwTR8T7qw6KMgm9vPvanHl6j5-Ds_godyhxkYUdwTj_IpEugiphMppdHsNzZlMfxoLhX4t0MzzWeWb0iAugYwIwOhhRm5daEm0BUewnaqGRDwLFsTs8NVt1k6xpf668rPjltxg4b9T3CslG0w-3kHMeFvEw0jqAwbk6feulmXWau9Dy1p1xQ4INIXJkg6-JW1n5kwo1ZDsLxGABsAeoVOZadCodZZAvaMzMOYfBdJxEZUKUsLdTqjQ",
        "additional_information": {
            "refresh_token_id": 976405
        },
        "expires_in": "3599"
    })
    user_data_body = json.dumps({
        "sub": "r30mZX6e4rTH3mylyH7AEj6u",
        "uid": "290368467694068583",
        "upn": "fuxiaodong@cashbus.onaliyun.com",
        "requestid": "1cd0de60-5883-4291-bba0-416063f6277e",
        "name": "付小东",
        "bid": "26842",
        "aid": "1726708279589269"
    })

    def runTest(self):
        return

    def test_login(self):
        self.do_login()

    def test_partial_pipeline(self):
        self.do_partial_pipeline()


if __name__ == '__main__':
    t = AliyunOAuth2Test()
    t.test_login()

