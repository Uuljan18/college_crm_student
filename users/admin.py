
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student


@admin.register(Student)
class StudentAdmin(UserAdmin):

    list_display = (
        'username',
        'last_name',
        'first_name',
        'group',
        'course',
        'status',
        'is_active',
    )

    search_fields = (
        'username',
        'first_name',
        'last_name',
        'middle_name',
        'student_id',
        'group',
    )

    list_filter = (
        'group',
        'course',
        'status',
    )

    ordering = ('last_name', 'first_name')

    fieldsets = UserAdmin.fieldsets + (
        ('Личные данные студента', {
            'fields': (
                'middle_name',
                'birth_date',
                'gender',
                'phone',
                'address',
                'photo',
            ),
        }),
        ('Информация об обучении', {
            'fields': (
                'student_id',
                'group',
                'specialty',
                'course',
                'admission_year',
                'education_form',
                'funding',
                'status',
            ),
        }),
        ('Даты', {
            'fields': (
                'created_at',
                'updated_at',
            ),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Данные студента', {
            'fields': (
                'first_name',
                'last_name',
                'middle_name',
                'gender',
                'student_id',
                'group',
                'specialty',
                'course',
                'admission_year',
                'education_form',
                'funding',
            ),
        }),
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

