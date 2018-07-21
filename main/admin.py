from django.contrib import admin

from main.models import Choice
from main.models import Question


admin.site.register(Question)
admin.site.register(Choice)
