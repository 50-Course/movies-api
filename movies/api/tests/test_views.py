from django.http import request, response
from django.shortcuts import reverse
from rest_framework.test import APITestCase
import json
from api.models import Movie

class TestMovieAPIView(APITestCase):

    # Initialixation
    def setUp(self):
        self.movie = Movie(name="John Wick is coming", year_of_release=2022)
        self.movie.save()

    # TODO: CRUD Tests
    # Update 1: Written the Create Test
    # Update 2: Wrote the Read Test
    # Update 3: Wrote the Delete Test
    def test_movie_read(self):
        response = self.client.get(reverse('movies'), format=json)
        self.assertEqual(len(response.data), 1)
        

    def test_movie_create(self):
        context = {
            "name": 'Say Ragnarok',
            "year_of_release": 2019
        }
        response = self.client.post(reverse('movies'), context)

        # new movie added, check for the status code returned
        self.assertEqual(Movie.objects.count(), 2)
        self.assertEqual(201, response.status_code)
        
        # should return a success request
        print(f'{0}' + "added successfully. STATUS_CODE", response.status_code)


    # def test_movie_delete(self):
    #     response = self.client.delete(reverse('movie_detail', kwargs={'pk': 1}))

        # validate status code for error 204 on request
        # self.assertEqual(204, response.status_code)
        

    def test_movie_update(self):
        pass

