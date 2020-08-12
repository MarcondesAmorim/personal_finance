from django.db import models


class Year(models.Model):
    year = models.IntegerField()
    opened = models.BooleanField()

    def starting_year(self):
        pass

    def close_year(self):
        pass

    def is_opened(self):
        pass

