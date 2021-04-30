from django.db import models


class JobOffer(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField(blank=False)
    salary = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.job_title

