from django.contrib import admin
from .models import YourModelName
class YourModelNameAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')

admin.site.register(YourModelName, YourModelNameAdmin)
# Register your models here.
