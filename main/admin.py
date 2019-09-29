from django.contrib import admin

# Register your models here.
from main.models import Data_database

#admin panelini özelleştiriyoruz.
class  DatabaseAdmin(admin.ModelAdmin):
    list_display =['system_name','publishing_date','data1','data2','data3']
    list_display_links =['system_name']
    list_filter = ['publishing_date']
    search_fields =['system_name','title']

    class Meta:
        model = Data_database

admin.site.register(Data_database,DatabaseAdmin)