from django.contrib import admin

# Register your models here.
from .models import Questions


class QuestionsAdmin(admin.ModelAdmin):
        fields = [ 'question', 'content', 'answer_id', 'date' ]
admin.site.register(Questions, QuestionsAdmin)
