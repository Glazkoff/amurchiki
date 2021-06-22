from django.contrib import admin
from .models import AnswersCounting, UserAnswer
# Register your models here.
class AnswersCountingAdmin(admin.ModelAdmin):
    """Подсчет ответов"""
    exclude = ('createdAt', 'updatedAt')
    # list_display=('',)
    # list_filter = ('',)
    # search_fields=('',)
    fieldsets = (
        (None, {
            'fields': ('date_time_counting','user',)
        }),
        ('Количество ответов', {
            'fields': ('answers_count1','answers_count2','answers_count3', 'answers_count4', 'answers_count5',)
        }),
    )
class UserAnswerAdmin(admin.ModelAdmin):
    """Ответ пользователя на вопрос"""
    exclude = ('createdAt', 'updatedAt')
    # list_display=('',)
    # list_filter = ('')
    search_fields=('answer',)
    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Вопросы', {
            'fields': ('question_with_scale','question_with_option',)
        }),
        ('Ответы', {
            'fields': ('answer','date_time_answer',)
        }),
    )
admin.site.register(AnswersCounting, AnswersCountingAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)