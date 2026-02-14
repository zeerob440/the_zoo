from django import forms
#creates form for user login at zoo_entrance

class userLoginForm(forms.Form):
    username = forms.CharField(
        max_length = 25,
        label = 'Enter your name'
    )

    # given no password protected login for expediency and simplicity, logins will be written as lower-case only.
    def clean_username(self):
        username =self.cleaned_data['username']
        return username.strip().lower()