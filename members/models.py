from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='base/profiles/') # Requires Pillow (PIL fork)
    website = models.SlugField(blank=True) # not required

    @property
    def full_name(self):
        """Returns the full name of a member"""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name

    class Meta:
        unique_together = (('first_name', 'last_name'),)
