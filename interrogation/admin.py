from django.contrib import admin
from .models import Interrogation, Question, Answer, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Question._meta.fields]
    list_filter = ('text', 'type')
    search_fields = ('text', 'type')
    inlines = [ChoiceInline]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


@admin.register(Interrogation)
class InterrogationAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_active', 'start', 'stop']
    list_filter = ('description', 'is_active', 'start', 'stop')
    search_fields = ('description', 'is_active', 'start', 'stop')
    readonly_fields = (
        'start',
    )
    list_display_links = ('title', 'description')
    list_editable = ['is_active']
    inlines = [QuestionInline]




@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
    )
    list_filter = ('user',)