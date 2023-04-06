from django import forms
import re


class userdata(forms.Form):
    username = forms.CharField(label="Enter Username: ")
    mail = forms.EmailField(label="Enter Mail: ")
    password = forms.CharField(widget=forms.PasswordInput, label="Enter Password: ")
    mobile = forms.IntegerField(label="Enter mobile: ")
    address = forms.CharField(widget=forms.Textarea, label="Enter Address: ")

    def clean_username(self):
        data = self.cleaned_data['username']
        if data.isalpha():
            return data
        else:
            raise forms.ValidationError("Username should contain only Alphabets")

    def clean_password(self):
        data = self.cleaned_data['password']
        if not (re.search('[A-Z]+', data)):
            raise forms.ValidationError("Password Should Contain One Capital Letter")
        if not (re.search('[a-z]+', data)):
            raise forms.ValidationError("Password Should Contain One Small Letter ")
        if not (re.search('[0-9]+', data)):
            raise forms.ValidationError("Password Should Contain Alteast one Number")
        if not (re.search('[^A-Za-z0-9]+', data)):
            raise forms.ValidationError("Password Should Contain one Special Character")
        return data

    def clean_mobile(self):
        data = self.cleaned_data['mobile']
        if len(str(data)) != 10:
            raise forms.ValidationError("Mobile should have 10 digits")
        else:
            return data


class loginform(forms.Form):
    username = forms.CharField(label="Enter Username: ")
    password = forms.CharField(widget=forms.PasswordInput, label="Enter Password: ")
