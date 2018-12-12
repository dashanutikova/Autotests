import requests
import unittest
import json


class AutoTest(unittest.TestCase):

    def common_check(self, url, expected_status, expected_response=None):
        r = requests.get(url)
        data = json.loads(r.content)
        if expected_response is not None:
            assert data == expected_response
        assert r.status_code == expected_status

    def test_gender_male_request(self):
        expected_response = {"errorCode": 0, "errorMessage": None, "result": [33, 10, 911, 94], "success": True}
        url = 'https://dev.coolrocket.com/test/users?gender=male'
        self.common_check(url, 200, expected_response)

    def test_gender_female_request(self):
        url = 'https://dev.coolrocket.com/test/users?gender=female'
        expected_response = {"errorCode": 0, "errorMessage": None, "result": [16, 5, 300], "success": True}
        self.common_check(url, 200, expected_response)

    def test_gender_error(self):
        url = 'https://dev.coolrocket.com/test/users?gender=ff'
        self.common_check(url, 500)

    def test_id_exist(self):
        url = 'https://dev.coolrocket.com/test/user/10'
        expected_response = {"errorCode": 0, "errorMessage": None, "result": {"id": 10, "name": "Peter", "gender": "male","age": 26,"city": "Omsk","registrationDate": "2016-12-01T00:30:00"}, "success": True}
        self.common_check(url, 200, expected_response)

    def test_id_not_exist(self):
        url = 'https://dev.coolrocket.com/test/user/1'
        expected_response = {"errorCode": 0, "errorMessage": None, "result": None, "success": True}
        self.common_check(url, 200, expected_response)

    def test_id_negative(self):
        url = 'https://dev.coolrocket.com/test/user/fg'
        self.common_check(url, 400)


if __name__ == "__main__":
    unittest.main()
