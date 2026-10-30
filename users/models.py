from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    REQUIRED_FIELDS = [
        'email',
        'student_id',
        'group',
        'specialty',
        'course',
        'admission_year',
        'gender',
        'education_form',
        'funding',
    ]

    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]

       
    COURSE_CHOICES = [
        (1, '1 курс'),
        (2, '2 курс'),
        (3, '3 курс'),
        (4, '4 курс'),
    ]

    EDUCATION_FORM_CHOICES = [
        ('full_time', 'Очная'),
        ('part_time', 'Заочная'),
        ('evening', 'Вечерняя'),
    ]

    FUNDING_CHOICES = [
        ('budget', 'Бюджет'),
        ('contract', 'Контракт'),
    ]

    STATUS_CHOICES = [
        ('studying', 'Обучается'),
        ('academic_leave', 'Академический отпуск'),
        ('expelled', 'Отчислен'),
        ('graduated', 'Выпускник'),
    ]

    middle_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Отчество'
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        verbose_name='Пол'
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Телефон'
    )

    address = models.TextField(
        blank=True,
        verbose_name='Адрес'
    )

    photo = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True,
        verbose_name='Фотография'
    )

    student_id = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Номер студенческого билета'
    )

    group = models.CharField(
        max_length=20,
        verbose_name='Группа'
    )

    specialty = models.CharField(
        max_length=150,
        verbose_name='Специальность'
    )

    course = models.PositiveSmallIntegerField(
        choices=COURSE_CHOICES,
        verbose_name='Курс'
    )

    admission_year = models.PositiveSmallIntegerField(
        verbose_name='Год поступления'
    )

    education_form = models.CharField(
        max_length=20,
        choices=EDUCATION_FORM_CHOICES,
        verbose_name='Форма обучения'
    )

    funding = models.CharField(
        max_length=20,
        choices=FUNDING_CHOICES,
        verbose_name='Основа обучения'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='studying',
        verbose_name='Статус'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'first_name']

    @property
    def full_name(self):
        return ' '.join(
            part for part in [
                self.last_name,
                self.first_name,
                self.middle_name
            ] if part
        )

    def __str__(self):
        return f'{self.full_name} — {self.group}'
