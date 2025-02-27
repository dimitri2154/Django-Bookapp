from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image = models.ImageField(upload_to='book_covers/')

    def __str__(self):
        return self.title  # Or something like f"{self.title} by {self.author}"

    class Meta:
        db_table = 'book'