# Model managers
from django.db import models


class CategoryManagerSet(models.QuerySet):

    def active(self):
        return self.filter(active=True)

    def main_categories(self):
        return self.filter(parent__isnull=True).order_by('name')   # return all where parent is NULL