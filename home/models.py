from django.db import models

# Create your models here.


class ToDo(models.Model):
    title=models.CharField(max_length=100)
    date_time=models.DateTimeField()
    Details=models.TextField()
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title