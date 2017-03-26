from django.test import TestCase
from .models import Member

#Could be an example of singleton
class MemberTestCase(TestCase):
	def setUp(self):
		Member.objects.create(name='Jhon', last_name='Beltrán',
                              phone=123123123, email='j@gmail.com',
                              address='Calle falsa 123',
                              personal_skills='Obstinated',
                              team_skills='Good Speaker',
                              weakness='Obsesive', illness='None',
                              under_presure='Good worker',
                              )

	def test_members_have_email(self):
		member = Member.objects.get(name="Jhon")

		self.assertEqual(member.email, 'j@gmail.com')
