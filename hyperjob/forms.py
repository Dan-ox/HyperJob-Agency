from django import forms


class ResumeForm(forms.Form):
    description = forms.CharField(required=True,
                                  widget=
                                  forms.TextInput(attrs=
                                  {
                                      "placeholder": "Your description"
                                  }))


class VacancyForm(forms.Form):
    description = forms.CharField(required=True,
                                  widget=
                                  forms.TextInput(attrs=
                                  {
                                      "placeholder": "Your description"
                                  }))
