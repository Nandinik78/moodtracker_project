from django.db import models

class MoodEntry(models.Model):
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=20)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.mood}"
