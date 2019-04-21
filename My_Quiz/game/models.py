from django.db import models

# Create your models here.

class Questions(models.Model):
    question = models.CharField(max_length = 255, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    answer_id = models.BigIntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str___(self):
        return ('%s, %s, %s, %s') % self.question, self.answer_id, self.content, self.date
