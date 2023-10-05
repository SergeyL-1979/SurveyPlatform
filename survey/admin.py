from django.contrib import admin

from survey.models import Question, Answer, Choice, CheckQuestion, Favorites


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'visible',
        'max_points',
    )


class ChoiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'question',
        'points',
        'lock_other',
    )
    list_filter = ('question',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
    )
    list_filter = ('user',)


class CheckQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'survey_viewed',
    )


class FavoritesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'like_rating',
        'like_status',
    )


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(CheckQuestion, CheckQuestionAdmin)
admin.site.register(Favorites, FavoritesAdmin)
