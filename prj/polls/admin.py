from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from polls.models import Poll, Question

User = get_user_model()

admin.site.site_header = 'Polling Administration'


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Question)

admin.site.unregister(Group)
# admin.site.unregister(User)
