from django.db import models
from django.contrib.auth.models import User

class CodeSnippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Untitled')
    code = models.TextField()
    language = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000, blank=True, null=True, default="No description provided")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.title} - {self.user.username}"


class SharedCodeSnippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_shared = models.CharField(max_length=100)  # Storing username as text instead of ForeignKey
    title = models.CharField(max_length=100, default='Untitled')
    code = models.TextField()
    language = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000, blank=True, null=True, default="No description provided")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.title} shared by {self.user.username} to {self.user_shared}"