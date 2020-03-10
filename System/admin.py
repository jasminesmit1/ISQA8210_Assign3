from django.contrib import admin
from .models import *


@admin.register(Area)
class AreaList(admin.ModelAdmin):
    list_display = ('area', 'floor')
    list_filter = ('area', 'floor')
    search_fields = ('area', 'floor' )
    ordering = ['id']


@admin.register(User)
class UserList(admin.ModelAdmin):
    list_display = ('employ_num', 'username', 'first_name', 'last_name')
    list_filter = ('employ_num', 'username', 'first_name', 'last_name')
    search_fields = ('employ_num', 'username', 'first_name', 'last_name', )
    ordering = ['id']


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(AssignedJob)
class JobList(admin.ModelAdmin):
    list_display = ('area', 'employee', 'date', 'completed')
    list_filter = ('area', 'employee', 'date', 'completed')
    search_fields = ('area', 'employee', 'completed')
    ordering = ['id']
    inlines = [
        TaskInline,
    ]