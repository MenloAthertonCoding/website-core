from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    school = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Contestant(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    @property
    def full_name(self):
        """Returns the full name of a contestant"""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name

    class Meta:
        unique_together = (('first_name', 'last_name', 'team'),)
        ordering = ('first_name',)
