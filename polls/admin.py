from django.contrib import admin
from .models import Poll, Question, Choice

class PollAdmin(admin.ModelAdmin):
    fields = ['name', 'start_date', 'expiration_date', 'description']
    list_display = ['name', 'start_date', 'expiration_date',]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['start_date']
        else:
            return []

admin.site.register(Poll, PollAdmin)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ['poll', 'text', 'answer_type']
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
