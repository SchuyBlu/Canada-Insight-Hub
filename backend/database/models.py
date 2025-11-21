from django.db import models


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "student"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
