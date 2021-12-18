from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from .models import *

User = get_user_model()

admin.site.site_header = 'Polling Administration'


class TextQuestionInline(admin.TabularInline):
    model = TextQuestion
    extra = 1
    exclude = ('answers', )


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [TextQuestionInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            self.readonly_fields = ('datetime_start', )
        else:
            self.readonly_fields = ()
        return super().get_readonly_fields(request, obj=None)


class ChoiceAnswerInline(admin.TabularInline):
    model = ChoiceAnswer
    extra = 1
    exclude = ('users', )


@admin.register(ChoiceQuestion)
class ChoiceQuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceAnswerInline]
    exclude = ('choices', )


admin.site.register(TextQuestion)
admin.site.register(ChoiceAnswer)
admin.site.register(TextAnswer)

admin.site.unregister(Group)
# admin.site.unregister(User)
