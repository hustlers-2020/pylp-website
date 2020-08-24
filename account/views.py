from dal import autocomplete
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.forms import BaseModelFormSet, formset_factory, modelformset_factory
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import (
    force_bytes,
    force_text
)
from django.urls import reverse
from django.utils.html import format_html, strip_tags
from account.models import (
    CommunityActivity,
    EducationalBackground,
    MembershipOrganization,
    Profile,
    School
)
from django.views import View
from content.models import ContactUsEmail, SignUpInstructions
from account.forms import (
    CommunityActivityForm,
    EducationalBackgroundForm,
    LogInForm,
    MembershipOrganizationForm,
    PersonalInformationForm,
    PhotoSignatureForm,
    SignupForm
)
from account.utils import token_generator
from dal import autocomplete
from django.db.models.signals import post_save
from django.dispatch import receiver


class RequiredFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


class SignupView(View):

    EducationalBackgroundFormSet = modelformset_factory(EducationalBackground,
                                                        form=EducationalBackgroundForm, formset=RequiredFormSet, extra=1, max_num=4)
    MembershipOrganizationFormSet = modelformset_factory(MembershipOrganization,
                                                         form=MembershipOrganizationForm, formset=RequiredFormSet, extra=1)
    CommunityActivityFormSet = modelformset_factory(CommunityActivity,
                                                    form=CommunityActivityForm, formset=RequiredFormSet, extra=1)

    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('index')

        education_formset = self.EducationalBackgroundFormSet(queryset=EducationalBackground.objects.none(),
                                                              prefix='education'
                                                              )
        membership_formset = self.MembershipOrganizationFormSet(queryset=MembershipOrganization.objects.none(),
                                                                prefix='membership'
                                                                )
        activity_formset = self.CommunityActivityFormSet(queryset=MembershipOrganization.objects.none(),
                                                         prefix='activity'
                                                         )
        return render(request, 'signup.html',
                      {'UserForm': SignupForm,
                       'InformationForm': PersonalInformationForm,
                       'EducationForm': education_formset,
                       'MembershipForm': membership_formset,
                       'CommunityForm': activity_formset})

    def post(self, request, *args, **kwargs):
        user_form = SignupForm(request.POST)
        personal_information_form = PersonalInformationForm(request.POST)
        education_formset = self.EducationalBackgroundFormSet(
            request.POST, prefix='education')
        membership_formset = self.MembershipOrganizationFormSet(
            request.POST, prefix='membership')
        activity_formset = self.CommunityActivityFormSet(
            request.POST, prefix='activity')
        if user_form.is_valid() and personal_information_form.is_valid() and education_formset.is_valid() and membership_formset.is_valid() and activity_formset.is_valid():
            userform = User.objects.create_user(
                username=user_form.cleaned_data['username'],
                first_name=personal_information_form.cleaned_data['first_name'],
                last_name=personal_information_form.cleaned_data['last_name'],
                email=user_form.cleaned_data['email'])
            userform.set_password(
                user_form.cleaned_data['password1']
            )
            userform.is_active = False
            userform.save()
            profile = personal_information_form.save(user=userform)
            for education_form in education_formset:
                education_form.save(profile=profile)
            for membership_form in membership_formset:
                membership_form.save(profile=profile)
            for activity_form in activity_formset:
                activity_form.save(profile=profile)

            email_subject = "PYLP Registration Email Confirmation"
            uidb64 = urlsafe_base64_encode(force_bytes(userform.pk))
            token = token_generator.make_token(userform)
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={
                'uidb64': uidb64, 'token': token})
            activate_url = f'http://{domain}{link}'
            instruction = SignUpInstructions.objects.last()
            content = format_html(instruction.content)
            content_value = strip_tags(content)
            email_body = f"Thank you for registering at PYLP Alumni Association, Inc.\n\nTo get started, activate your account by clicking the link below.\n{activate_url}\n\n{content_value}"
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@pylp.com',
                [user_form.cleaned_data['email']],
            )
            email.send(fail_silently=False)
            profile_pk = urlsafe_base64_encode(force_bytes(profile.pk))
            return redirect(reverse('photo-sig', kwargs={'pk': profile_pk}))
        else:
            return render(request, 'signup.html', {
                'UserForm': user_form,
                'InformationForm': personal_information_form,
                'EducationForm': education_formset,
                'MembershipForm': membership_formset,
                'CommunityForm': activity_formset})


class PhotoSignatureView(View):
    def get(self, request, pk, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('index')
        try:
            pk = force_text(urlsafe_base64_decode(pk))
            Profile.objects.get(pk=pk)
            return render(request, 'submit_photo_signature.html', {'photoSignatureForm': PhotoSignatureForm})
        except:
            return redirect('index')

    def post(self, request, pk, *args, **kwargs):
        photo_sig_form = PhotoSignatureForm(request.POST, request.FILES)
        if photo_sig_form.is_valid():
            pk = force_text(urlsafe_base64_decode(pk))
            profile = Profile.objects.get(pk=pk)
            if photo_sig_form.cleaned_data['photo']:
                profile.photo = photo_sig_form.cleaned_data['photo']
            if photo_sig_form.cleaned_data['e_sig']:
                profile.electronic_signature = photo_sig_form.cleaned_data['e_sig']
            profile.save()
        instruction = SignUpInstructions.objects.last()
        content = format_html(instruction.content)
        return render(request, 'activate_account.html', {'header': "How To Activate Your Account", 'instruction_content': content})


class VerificationView(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uidb64 = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uidb64)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and token_generator.check_token(user, token):
            # activate user and login:
            user.is_active = True
            account = Profile.objects.get(user=user)
            account.is_verified = True
            user.save()
            account.save()

        messages.success(request, "Account Activated successfully. You may log in now.",
                         extra_tags='register')
        return redirect('login')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('index')
        return render(request, 'login.html', {'loginForm': LogInForm})

    def post(self, request, *args, **kwargs):
        login_form = LogInForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data['user_name'],
                password=login_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                not_active = User.objects.get(
                    username=login_form.cleaned_data['user_name'])
                if(not_active):
                    if(not_active.is_active == False):
                        instruction = SignUpInstructions.objects.last()
                        content = format_html(instruction.content)
                        return render(request, 'activate_account.html', {'header': "Your Account Isn't Activated Yet.",
                                                                         'instruction': instruction,
                                                                         'instruction_content': content})
                    else:
                        messages.error(request, "Incorrect credentials.")
                        return render(request, 'login.html', {
                            'loginForm': login_form,
                        })
                else:
                    messages.error(request, "Incorrect credentials.")
                    return render(request, 'login.html', {
                        'loginForm': login_form,
                    })
        else:
            return render(request, 'login.html', {
                'loginForm': login_form,
            })


class ProfileView(View):

    EducationalBackgroundFormSet = modelformset_factory(EducationalBackground, formset=RequiredFormSet,
                                                        form=EducationalBackgroundForm, extra=0, max_num=4)
    MembershipOrganizationFormSet = modelformset_factory(MembershipOrganization,
                                                         form=MembershipOrganizationForm, formset=RequiredFormSet, extra=0)
    CommunityActivityFormSet = modelformset_factory(CommunityActivity,
                                                    form=CommunityActivityForm, formset=RequiredFormSet, extra=0)

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')
        try:
            profile = Profile.objects.get(user=request.user)
            educ = EducationalBackground.objects.filter(profile=profile)
            membership = MembershipOrganization.objects.filter(profile=profile)
            activity = CommunityActivity.objects.filter(profile=profile)
            education_formset = self.EducationalBackgroundFormSet(
                queryset=educ, prefix="education")
            membership_formset = self.MembershipOrganizationFormSet(
                queryset=membership, prefix='membership')
            activity_formset = self.CommunityActivityFormSet(
                queryset=activity, prefix='activity')
            updateProfileForm = PersonalInformationForm(instance=profile)
            return render(request, 'profile.html',
                          {'photoSignatureForm': PhotoSignatureForm,
                           'updateProfileForm': updateProfileForm,
                           'EducationForm': education_formset,
                           'MembershipForm': membership_formset,
                           'CommunityForm': activity_formset,
                           'profile': profile})
        except:
            print("Logged in user has no associated profile!")
            return redirect('index')

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        personal_information_form = PersonalInformationForm(
            request.POST, instance=profile)
        education_formset = self.EducationalBackgroundFormSet(
            request.POST, prefix='education')
        membership_formset = self.MembershipOrganizationFormSet(
            request.POST, prefix='membership')
        activity_formset = self.CommunityActivityFormSet(
            request.POST, prefix='activity')
        photo_sig_form = PhotoSignatureForm(request.POST, request.FILES)
        if personal_information_form.is_valid() and education_formset.is_valid() and membership_formset.is_valid() and activity_formset.is_valid() and photo_sig_form.is_valid():
            personal_information_form.save(user=request.user)
            for education_form in education_formset:
                education_form.save(profile=profile)
            for membership_form in membership_formset:
                membership_form.save(profile=profile)
            for activity_form in activity_formset:
                activity_form.save(profile=profile)
            clear_photo = request.POST['clearphoto']
            clear_sig = request.POST['clearsig']
            if clear_photo == "1":
                profile.photo.delete(save=False)
            if clear_sig == "1":
                profile.electronic_signature.delete(save=False)
            if photo_sig_form.cleaned_data['photo'] and clear_photo == "0":
                profile.photo = photo_sig_form.cleaned_data['photo']
            if photo_sig_form.cleaned_data['e_sig'] and clear_sig == "0":
                profile.electronic_signature = photo_sig_form.cleaned_data['e_sig']
            profile.save()
            return redirect('profile')
        else:
            print(education_formset.errors)
            return render(request, 'profile.html',
                          {'photoSignatureForm': photo_sig_form,
                           'updateProfileForm': personal_information_form,
                           'EducationForm': education_formset,
                           'MembershipForm': membership_formset,
                           'CommunityForm': activity_formset,
                           'profile': profile})


def send_email(photo=None, e_sig=None):
    subject = ""
    body = ""
    contact_email = ""
    try:
        contact_email = ContactUsEmail.objects.first().email
    except:
        contact_email = ""
    if photo and e_sig:
        subject = "[Photo & E-Signature Update]"
        body = f"Updated Photo: {photo} \n\n Updated E-Signature: {e_sig}"
    elif photo:
        subject = "[Photo Update]"
        body = f"Updated Photo: {photo}"
    elif e_sig:
        subject = "[E-Signature Update]"
        body = f"Updated E-Signature: {e_sig}"

    email = EmailMessage(
        subject,
        body,
        'noreply@pylp.com',
        [contact_email],
    )
    email.send(fail_silently=False)


@ receiver(post_save, sender=Profile)
def email_handler(sender, instance, **kwargs):
    if instance.is_dirty():
        dirty = instance.get_dirty_fields()
        try:
            if 'photo' in dirty and 'electronic_signature' in dirty:
                photo = "User removed photo"
                e_sig = "User removed photo"
                if instance.photo:
                    photo = instance.photo.url
                if instance.electronic_signature:
                    e_sig = instance.electronic_signature.url
                send_email(photo=photo, e_sig=e_sig)
            elif 'photo' in dirty:
                photo = "User removed photo"
                if instance.photo:
                    photo = instance.photo.url
                send_email(photo=photo)
            elif 'electronic_signature' in dirty:
                e_sig = "User removed photo"
                if instance.electronic_signature:
                    e_sig = instance.electronic_signature.url
                send_email(e_sig=e_sig)
        except:
            pass


class school_autocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = School.objects.all()
        if self.q:
            qs = qs.filter(school_name__istartswith=self.q)
        return qs
