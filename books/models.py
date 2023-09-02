from django.db import models
from django.contrib.auth.models import User

# ORM -> Object Relational Mapper

# Create your models here.
class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    qty = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.book_name

    class Meta:
         db_table = 'book'


class Lease(models.Model):
    lease_id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book_id.book_name}-{self.user_id.username}"

    class Meta:
        db_table = 'lease'
