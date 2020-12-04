# from django.test import TestCase

# # Create your tests here.
# from rest_framework import status
# from rest_framework.test import APITestCase
# from . serializers import *
# from . models import *
# import json

# class StudentTestCase(APITestCase):

#     def setUp(self):
#         student = Student.objects.create(firstname="Vishnu", lastname="kumar", roll_no="60")
#         student.save()

#         self.valid_data = {
#             "firstname": "Vishnu", "lastname": "kumar", "roll_no": "60"
#         }

#         self.valid_data_put = {
#             "firstname": "Vikram", "lastname": "kumar", "roll_no": "90"
#         }

#         self.valid_data_patch = {
#             "firstname": "Marun", "lastname": "Kaka", "roll_no": "90"
#         }

#     def test_student(self):
#         # import ipdb; ipdb.set_trace()

#         url = "http://localhost:8000/api/student/"

#         # """POST METHOD"""
#         response = self.client.post(path=url, data=json.dumps(self.valid_data), content_type="application/json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         """PUT METHOD"""
#         put_id = str(response.data['id'])
#         put_url = url + put_id + "/"
#         response = self.client.put(path=put_url, data=json.dumps(self.valid_data_put), content_type="application/json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         """PATCH METHOD"""
#         patch_id = str(response.data['id'])
#         patch_url = url + patch_id + "/"
#         response = self.client.put(path=patch_url, data=json.dumps(self.valid_data_patch), content_type="application/json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         '''DELETE METHOD'''
#         delete_id = str(response.data['id'])
#         delete_url = url + delete_id + "/"
#         response = self.client.delete(path=delete_url, content_type="application/json")
#         # import ipdb; ipdb.set_trace()
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#         """GET METHOD"""
#         response = self.client.get(path=url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
