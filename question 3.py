# models.py
# Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# Ansewer: Yes, by default django signals do run in the same database transaction as the caller.
# As we can see that the Book created by the signal is also rolled back, proving that Django signals run in the same transaction by default.

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

@receiver(post_save, sender=Author)
def create_book(sender, instance, **kwargs):
    print("Signal: Creating a book")
    Book.objects.create(title="Book for " + instance.name, author=instance)
    print("Signal: Book created")

def test_signal_and_transaction():
    try:
        with transaction.atomic():
            print("Creating author...")
            author = Author.objects.create(name="John Doe")
            print("Author created")
            raise Exception("Oops! Something went wrong")

    except Exception as e:
        print("Error: ", e)

    print("Books:", Book.objects.all())
