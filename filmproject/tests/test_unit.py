from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import *
from django.utils import timezone
from django.urls import reverse, resolve
from django.core import mail


# 1st test to make sure our testing environment is working
class SimpleTest(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

# Next lets check our urls
class URLTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.superuser = User.objects.create_superuser(username='yomama', password='385')
        self.superuser.save()
        self.regularuser = User.objects.create_user(username='yodaddy', password='123')
        self.regularuser.save()
        
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        
    def test_admin_authenticated(self):
        self.client.login(username='yomama', password='385')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        
    def test_admin_not_authenticated(self):
        self.client.login(username='yodaddy', password='123')
        response = self.client.get('/admin/')
        self.assertNotEqual(response.status_code, 200)
        
    def test_popular_movies(self):
        response = self.client.get(reverse('popular_movies'))
        self.assertEqual(response.status_code, 200)

    def test_search_movies(self):
        response = self.client.get(reverse('search_movies'))
        self.assertEqual(response.status_code, 200)
# Model tests next
class FilmModelTest(TestCase):
    def test_film_creation(self):
        film = Film.objects.create(
            adult = False,
            backdrop_path = 'https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg',
            belongs_to_collection = False,
            budget = 69420,
            homepage = 'https://www.google.com',
            imdb_id='1',
            original_title='Joker',
            overview='During the 1980s, a failed stand-up comedian is driven insane and turns to a life of crime and chaos in Gotham City while becoming an infamous psychopathic crime figure.',
            popularity=9.99,
            poster_path='https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg',
            release_date='2019-10-01',
            revenue=500000,
            runtime=120,
            status='Released',
            tagline='A test tagline',
            title='Joker',
            tmdb_id=475557,
            vote_average=8.152,
            vote_count=25372
            )
        # Assertions for each field
        self.assertEqual(film.adult, False)
        self.assertEqual(film.backdrop_path, 'https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg')
        self.assertEqual(film.belongs_to_collection, False)
        self.assertEqual(film.budget, 69420)
        self.assertEqual(film.homepage, 'https://www.google.com')
        self.assertEqual(film.imdb_id, '1')
        self.assertEqual(film.original_title, 'Joker')
        self.assertEqual(film.overview, 'During the 1980s, a failed stand-up comedian is driven insane and turns to a life of crime and chaos in Gotham City while becoming an infamous psychopathic crime figure.')
        self.assertEqual(film.popularity, 9.99)
        self.assertEqual(film.poster_path, 'https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg')
        self.assertEqual(film.release_date, '2019-10-01')
        self.assertEqual(film.revenue, 500000)
        self.assertEqual(film.runtime, 120)
        self.assertEqual(film.status, 'Released')
        self.assertEqual(film.tagline, 'A test tagline')
        self.assertEqual(film.title, 'Joker')
        self.assertEqual(film.tmdb_id, 475557)
        self.assertEqual(film.vote_average, 8.152)
        self.assertEqual(film.vote_count, 25372)
        self.assertEqual(str(film), 'Joker')


class GenreModelTest(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(
            tmdb_id=1,
            genre='Funny but a little sad'
        )

    def test_genre_creation(self):
        self.assertEqual(self.genre.genre, 'Funny but a little sad')
        self.assertEqual(self.genre.tmdb_id, 1)
        self.assertEqual(str(self.genre), 'Funny but a little sad')


class KeywordModelTest(TestCase):
    def setUp(self):
        self.keyword = Keyword.objects.create(
            tmdb_id=1,
            keyword='Car'
        )

    def test_keyword_creation(self):
        self.assertEqual(self.keyword.keyword, 'Car')
        self.assertEqual(self.keyword.tmdb_id, 1)
        self.assertEqual(str(self.keyword), 'Car')

class CountryModelTest(TestCase):
    def setUp(self):
        self.country = Country.objects.create(
            code='CA',
            country='Canada'
        )

    def test_country_creation(self):
        self.assertEqual(self.country.country, 'Canada')
        self.assertEqual(self.country.code, 'CA')
        self.assertEqual(str(self.country), 'Canada')

class CompanyModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            tmdb_id=1,
            company='Netflix can suck it'
        )

    def test_company_creation(self):
        self.assertEqual(self.company.company, 'Netflix can suck it')
        self.assertEqual(self.company.tmdb_id, 1)
        self.assertEqual(str(self.company), 'Netflix can suck it')

class LanguageModelTest(TestCase):
    def setUp(self):
        self.language = Language.objects.create(
            code='EN',
            language='English'
        )
    def test_language_creation(self):
        self.assertEqual(self.language.language, 'English')
        self.assertEqual(self.language.code, 'EN')
        self.assertEqual(str(self.language), 'English')
        
class PersonModelTest(TestCase):
    def setUp(self):
        self.person = Person.objects.create(
            adult=True,
            gender=1,
            tmdb_id=1,
            known_for_department='Acting',
            name='Michael Keaton',
            popularity=9.5,
            profile_path='https://image.tmdb.org/t/p/w500/profile.jpg'
        )

    def test_person_creation(self):
        self.assertEqual(self.person.name, 'Michael Keaton')
        self.assertEqual(self.person.tmdb_id, 1)
        self.assertEqual(self.person.adult, True)
        self.assertEqual(self.person.gender, 1)
        self.assertEqual(self.person.known_for_department, 'Acting')
        self.assertEqual(self.person.popularity, 9.5)
        self.assertEqual(self.person.profile_path, 'https://image.tmdb.org/t/p/w500/profile.jpg')
        self.assertEqual(str(self.person), 'Michael Keaton')
 
class CollectionModelTest(TestCase):
    def setUp(self):
        self.collection = Collection.objects.create(
            tmdb_id=1,
            name='Alien Collection',
            poster_path='https://image.tmdb.org/t/p/w500/test.jpg',
            backdrop_path='https://image.tmdb.org/t/p/w500/test_backdrop.jpg'
        )

    def test_collection_creation(self):
        self.assertEqual(self.collection.name, 'Alien Collection')
        self.assertEqual(self.collection.tmdb_id, 1)
        self.assertEqual(self.collection.poster_path, 'https://image.tmdb.org/t/p/w500/test.jpg')
        self.assertEqual(self.collection.backdrop_path, 'https://image.tmdb.org/t/p/w500/test_backdrop.jpg')
        self.assertEqual(str(self.collection), 'Alien Collection')



class ViewerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='travis',
            email='tditmans@uccs.edu',
            password='password123'
        )
        self.viewer = Viewer.objects.create(
            user=self.user,  # Associate the user here
            name='travis ditmanson',
            email='tditmans@uccs.edu'
        )
    
    def test_viewer_creation(self):
        self.assertEqual(self.viewer.name, 'travis ditmanson')
        self.assertEqual(self.viewer.email, 'tditmans@uccs.edu')
        self.assertEqual(str(self.viewer), 'travis ditmanson')




class FriendRequestTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.viewer1 = Viewer.objects.create(user=self.user1, name='User 1')

        self.user2 = User.objects.create_user(username='user2', password='password')
        self.viewer2 = Viewer.objects.create(user=self.user2, name='User 2')

    def test_send_friend_request(self):
        friend_request = FriendRequest.objects.create(sender=self.viewer1, receiver=self.viewer2)
        self.assertEqual(friend_request.status, 'pending')

    def test_accept_friend_request(self):
        friend_request = FriendRequest.objects.create(sender=self.viewer1, receiver=self.viewer2)
        friend_request.accept()
        self.assertTrue(self.viewer1.is_friends_with(self.viewer2))
        self.assertEqual(friend_request.status, 'accepted')

    def test_reject_friend_request(self):
        friend_request = FriendRequest.objects.create(sender=self.viewer1, receiver=self.viewer2)
        friend_request.reject()
        self.assertFalse(self.viewer1.is_friends_with(self.viewer2))
        self.assertEqual(friend_request.status, 'rejected')

class UserRegistrationTest(TestCase):
    def test_registration(self):
        # Perform actions that should trigger email sending
        response = self.client.post("/register/", {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'PasswordTest123#@!',
            'password2': 'PasswordTest123#@!',
        })

        # Check if an email was sent
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]

        # Assert the email details
        self.assertEqual(email.subject, 'Activate your account.')
        self.assertEqual(email.to, ['testuser@example.com'])