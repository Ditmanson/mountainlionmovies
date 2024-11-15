from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Viewer


class ViewerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "profile_picture",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.profile_picture = self.cleaned_data["profile_picture"]
        if commit:
            user.save()
            # Create the Viewer instance associated with the User
            Viewer.objects.create(
                user=user,
                name=user.username,
                email=user.email,
                profile_picture=user.profile_picture,
            )
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Viewer
        fields = ["name", "email", "profile_picture"]
