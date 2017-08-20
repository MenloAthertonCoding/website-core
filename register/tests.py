from random import randint

from django.test import TestCase
from django.db import IntegrityError

from .models import Team, Contestant

class TeamModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Sets up required database information for running tests"""
        cls.team = Team.objects.create(name='Test Team')
    
    def test_add_duplicate_team(self):
        """Test whether a duplicate team will raise an IntegrityError"""
        with self.assertRaises(IntegrityError):
            Team.objects.create(name=self.team.name)

class ContestantModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Sets up required database information for running tests"""
        cls.team = Team.objects.create(name='Test Team') # team declared above is destroyed

        cls.contestant = Contestant.objects.create(
            first_name='Test',
            last_name='Case 0',
            email='example@example.com',
            team=cls.team
        )


    def test_add_duplicate_contestant(self):
        """Test whether a duplicate contestant will raise an IntegrityError"""
        with self.assertRaises(IntegrityError):
            Contestant.objects.create(
                first_name=self.contestant.first_name,
                last_name=self.contestant.last_name,
                email=self.contestant.email,
                team=self.contestant.team
            )

    def test_add_duplicate_contestant_name(self):
        """Test whether a contestant with a duplicate name will raise an IntegrityError"""
        with self.assertRaises(IntegrityError):
            Contestant.objects.create(
                first_name=self.contestant.first_name,
                last_name=self.contestant.last_name,
                email='example1@example.com'
            )

    def test_add_duplicate_contestant_email(self):
        """Test whether a contestant with a duplicate email will raise an IntegrityError"""
        with self.assertRaises(IntegrityError):
            Contestant.objects.create(
                first_name=self.contestant.first_name,
                last_name='Case 1',
                email=self.contestant.email,
                team=self.contestant.team
            )

    def test_add_multiple_users_to_team(self):
        """Test whether multiple contestants can be in a single team"""
        rnum = randint(1, 100)
        for i in range(1, rnum):
            Contestant.objects.create(
                first_name=self.contestant.first_name,
                last_name='Case {0}'.format(str(i)),
                email='example{0}@example.com'.format(str(i)),
                team=self.contestant.team
            )

        self.assertIn(
            Contestant.objects.get(pk=randint(1, rnum)),
            self.team.contestant_set.all()
        )
    

    def test_print_fullname(self):
        """Test whether we can print the proper full name"""
        self.assertEqual(self.contestant.full_name,
        '{0} {1}'.format(self.contestant.first_name, self.contestant.last_name))
