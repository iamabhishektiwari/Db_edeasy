from django.contrib import admin
from .models import Topic, Level, McqQuestion,RelatedExam
# Register your models here.
admin.site.register(Topic)
admin.site.register(Level)
admin.site.register(McqQuestion)
admin.site.register(RelatedExam)
