from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=64)
    register_number = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    deleted_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "company"
        constraints = [
            models.UniqueConstraint(
                fields=["company_name", "register_number"],
                name="company_name_register_number_unique"
            )
        ]

    def __str__(self):
        return f"{self.company_name}"
