from django.contrib import admin
from polls.models import Choice, Question
# Import the UserProfile model individually.
from polls.models import UserProfile
from polls.models import Category, Page, Library, Book
admin.site.register(Category)
admin.site.register(Page)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class BookInline(admin.TabularInline):
    model = Book
    extra = 3

class LibraryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['library_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [BookInline]
    list_display = ('library_text', 'pub_date')
    list_display = ('library_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['library_text']
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserProfile)
admin.site.register(Library)
