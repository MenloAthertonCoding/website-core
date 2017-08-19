from django.test import TestCase
from django.db import IntegrityError

from .models import Member


class MemberModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Sets up required database information for running tests"""
        cls.member = Member.objects.create(
            first_name='Test',
            last_name='Case 0',
            email='example@example.com',
            website='www.djangoproject.com'
        )

    def test_add_duplicate_member(self):
        """Test whether a duplicate member will raise an IntegrityError"""
        with self.assertRaises(IntegrityError):
            Member.objects.create(
                first_name=self.member.first_name,
                last_name=self.member.last_name,
                email=self.member.email,
                website=self.member.website
            )

    def test_add_duplicate_member_name(self):
        """Test whether a member with a duplicate name will raise an IntegrityError"""
        with self.assertRaises(IntegrityError):
            Member.objects.create(
                first_name=self.member.first_name,
                last_name=self.member.last_name,
                email='example2@example.com',
                website='www.github.com'
            )

    def test_add_duplicate_member_email(self):
        """Test whether a member with a duplicate email will raise an IntegrityError"""
        with self.assertRaises(IntegrityError):
            Member.objects.create(
                first_name=self.member.first_name,
                last_name='Case 1',
                email=self.member.email,
                website='www.github.com'
            )

    def test_print_fullname(self):
        """Test whether we can print the proper full name"""
        self.assertEqual(self.member.full_name,
        '{0} {1}'.format(self.member.first_name, self.member.last_name))
