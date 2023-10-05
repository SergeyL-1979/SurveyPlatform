from django.core import mail
from rest_framework import status
from rest_framework.test import APITestCase


class EmailVerificationTest(APITestCase):
    # endpoints needed
    register_url = "/users/"
    activate_url = "/users/activation/"

    user_data = {
        "email": "test@example.com",
        "first_name": "test_user",
        "last_name": "test_last",
        "password": "verysecret"
    }
    login_data = {
        "email": "test@example.com",
        "password": "verysecret"
    }

    def test_register_with_email_verification(self):
        # register the new user
        response = self.client.post(self.register_url, self.user_data, format="json")
        # expected response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # expected one email to be send
        self.assertEqual(len(mail.outbox), 1)

        # parse email to get uid and token
        email_lines = mail.outbox[0].body.splitlines()
        # you can print email to check it
        # print(mail.outbox[0].subject)
        # print(mail.outbox[0].body, "BODY")
        activation_link = [l for l in email_lines if "/activation/" in l][0]
        uid, token = activation_link.split("/")[-2:]

        # verify email
        data = {"uid": uid, "token": token}
        response = self.client.post(self.activate_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

