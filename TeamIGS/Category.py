# Simple Category class, allows for sorting by category easily
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    # allows for alternate url that includes name of category when category is multiple words, requires implementation
    slug = models.SlugField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ('name',)


    # returns all categories
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
