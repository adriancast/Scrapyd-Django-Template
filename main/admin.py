from django.contrib import admin
from main.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', )

# Register your models here.
admin.site.register(Quote, QuoteAdmin)