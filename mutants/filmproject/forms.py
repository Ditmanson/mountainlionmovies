
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


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

    def xǁViewerRegistrationFormǁsave__mutmut_orig(self, commit=True):
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

    def xǁViewerRegistrationFormǁsave__mutmut_1(self, commit=False):
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

    def xǁViewerRegistrationFormǁsave__mutmut_2(self, commit=True):
        user = super().save(commit=True)
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

    def xǁViewerRegistrationFormǁsave__mutmut_3(self, commit=True):
        user = None
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

    def xǁViewerRegistrationFormǁsave__mutmut_4(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["XXemailXX"]
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

    def xǁViewerRegistrationFormǁsave__mutmut_5(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data[None]
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

    def xǁViewerRegistrationFormǁsave__mutmut_6(self, commit=True):
        user = super().save(commit=False)
        user.email = None
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

    def xǁViewerRegistrationFormǁsave__mutmut_7(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.profile_picture = self.cleaned_data["XXprofile_pictureXX"]
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

    def xǁViewerRegistrationFormǁsave__mutmut_8(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.profile_picture = self.cleaned_data[None]
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

    def xǁViewerRegistrationFormǁsave__mutmut_9(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.profile_picture = None
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

    def xǁViewerRegistrationFormǁsave__mutmut_10(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.profile_picture = self.cleaned_data["profile_picture"]
        if commit:
            user.save()
            # Create the Viewer instance associated with the User
            Viewer.objects.create(
                user=None,
                name=user.username,
                email=user.email,
                profile_picture=user.profile_picture,
            )
        return user

    def xǁViewerRegistrationFormǁsave__mutmut_11(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.profile_picture = self.cleaned_data["profile_picture"]
        if commit:
            user.save()
            # Create the Viewer instance associated with the User
            Viewer.objects.create(
                name=user.username,
                email=user.email,
                profile_picture=user.profile_picture,
            )
        return user

    def xǁViewerRegistrationFormǁsave__mutmut_12(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.profile_picture = self.cleaned_data["profile_picture"]
        if commit:
            user.save()
            # Create the Viewer instance associated with the User
            Viewer.objects.create(
                user=user,
                email=user.email,
                profile_picture=user.profile_picture,
            )
        return user

    def xǁViewerRegistrationFormǁsave__mutmut_13(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.profile_picture = self.cleaned_data["profile_picture"]
        if commit:
            user.save()
            # Create the Viewer instance associated with the User
            Viewer.objects.create(
                user=user,
                name=user.username,
                profile_picture=user.profile_picture,
            )
        return user

    def xǁViewerRegistrationFormǁsave__mutmut_14(self, commit=True):
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
            )
        return user

    xǁViewerRegistrationFormǁsave__mutmut_mutants = {
    'xǁViewerRegistrationFormǁsave__mutmut_1': xǁViewerRegistrationFormǁsave__mutmut_1, 
        'xǁViewerRegistrationFormǁsave__mutmut_2': xǁViewerRegistrationFormǁsave__mutmut_2, 
        'xǁViewerRegistrationFormǁsave__mutmut_3': xǁViewerRegistrationFormǁsave__mutmut_3, 
        'xǁViewerRegistrationFormǁsave__mutmut_4': xǁViewerRegistrationFormǁsave__mutmut_4, 
        'xǁViewerRegistrationFormǁsave__mutmut_5': xǁViewerRegistrationFormǁsave__mutmut_5, 
        'xǁViewerRegistrationFormǁsave__mutmut_6': xǁViewerRegistrationFormǁsave__mutmut_6, 
        'xǁViewerRegistrationFormǁsave__mutmut_7': xǁViewerRegistrationFormǁsave__mutmut_7, 
        'xǁViewerRegistrationFormǁsave__mutmut_8': xǁViewerRegistrationFormǁsave__mutmut_8, 
        'xǁViewerRegistrationFormǁsave__mutmut_9': xǁViewerRegistrationFormǁsave__mutmut_9, 
        'xǁViewerRegistrationFormǁsave__mutmut_10': xǁViewerRegistrationFormǁsave__mutmut_10, 
        'xǁViewerRegistrationFormǁsave__mutmut_11': xǁViewerRegistrationFormǁsave__mutmut_11, 
        'xǁViewerRegistrationFormǁsave__mutmut_12': xǁViewerRegistrationFormǁsave__mutmut_12, 
        'xǁViewerRegistrationFormǁsave__mutmut_13': xǁViewerRegistrationFormǁsave__mutmut_13, 
        'xǁViewerRegistrationFormǁsave__mutmut_14': xǁViewerRegistrationFormǁsave__mutmut_14
    }

    def save(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁViewerRegistrationFormǁsave__mutmut_orig"), object.__getattribute__(self, "xǁViewerRegistrationFormǁsave__mutmut_mutants"), *args, **kwargs)
        return result 

    save.__signature__ = _mutmut_signature(xǁViewerRegistrationFormǁsave__mutmut_orig)
    xǁViewerRegistrationFormǁsave__mutmut_orig.__name__ = 'xǁViewerRegistrationFormǁsave'




class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Viewer
        fields = ["name", "email", "profile_picture"]
