from django import forms


class DateInput(forms.DateInput):
    input_type="date"


class ClientForm(forms.Form):

    CHOICES = (
        ("M","Male"),
        ("F","Female")
    )

    dni = forms.CharField(label="DNI", max_length=8)
    name = forms.CharField(label="Name", max_length=200, required=True)
    last_name = forms.CharField(label="Lastname", max_length=200, required=True)
    email = forms.EmailField(label="Email", required=True)
    address = forms.CharField(label="Address", widget=forms.Textarea)
    phone = forms.CharField(label="Phone", max_length=20)
    gender = forms.ChoiceField(label="Sex", choices=CHOICES)
    birthdate = forms.DateField(label="Birthdate", input_formats=["%Y-%m-%d"], widget=DateInput)
    