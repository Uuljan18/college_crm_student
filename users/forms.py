
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import Student


class StudentForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput,
        required=False,
        help_text='Введите пароль при создании студента.'
    )

    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = Student

        fields = [
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'birth_date',
            'gender',
            'phone',
            'address',
            'photo',
            'student_id',
            'group',
            'specialty',
            'course',
            'admission_year',
            'education_form',
            'funding',
            'status',
        ]

        widgets = {
            'birth_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'address': forms.Textarea(
                attrs={'rows': 3}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['birth_date'].input_formats = [
            '%Y-%m-%d'
        ]

        if self.instance.pk:
            self.fields['password1'].help_text = (
                'Оставьте пустым, чтобы не менять пароль.'
            )

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not self.instance.pk and not password1:
            self.add_error(
                'password1',
                'Введите пароль студента.'
            )

        if password1:
            if password1 != password2:
                self.add_error(
                    'password2',
                    'Пароли не совпадают.'
                )
            else:
                try:
                    validate_password(
                        password1,
                        self.instance
                    )
                except ValidationError as error:
                    self.add_error(
                        'password1',
                        error
                    )

        return cleaned_data

    def save(self, commit=True):
        student = super().save(commit=False)

        password = self.cleaned_data.get('password1')

        if password:
            student.set_password(password)

        if commit:
            student.save()
            self.save_m2m()

        return student
