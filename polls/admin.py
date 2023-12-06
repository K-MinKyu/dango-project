from django.contrib import admin
from polls.models import Question, Choice


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_data', 'question_text']

    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_data'], 'classes': ['collapse']}),
    ]
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_data'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_data')
    list_filter = ['pub_data']
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
