from django import forms


class ArticleCheckerForm(forms.Form):
    #    username = forms.CharField(
        # label = "Username", max_length = "100", widget = forms.TextInput)
    #    url = forms.CharField(label="url", max_length="300")
    username = forms.CharField()
    url = forms.CharField()
