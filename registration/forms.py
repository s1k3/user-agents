from django import forms

class RegisterUserForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    username = forms.CharField(max_length = 50)
    email = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 50)
    confirm_password = forms.CharField(max_length = 50)



    def clean(self):
        cleaned_data = super(RegisterUserForm, self).clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password ')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("The two password fields must match.")
        return cleaned_data