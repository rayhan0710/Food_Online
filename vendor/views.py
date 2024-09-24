from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from accounts.forms import UserProfileForm
from accounts.models import UserProfile
from .models import Vendor
from .forms import VendorForm


# Create your views here.
def vprofile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    vendor = get_object_or_404(Vendor, user=request.user)
    profile_form = UserProfileForm(instance = profile)
    vendor_form = VendorForm(instance=vendor)
    print(vendor)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        vendor_form = VendorForm(request.POST, request.FILES, instance=vendor)
        print(vendor_form)
        if profile_form.is_valid() and vendor_form.is_valid():
            profile_form.save()
            vendor_form.save()
            messages.success(request, 'Changes updated successfuly')
            return redirect('vprofile')

        # print(vendor_form)
        # if vendor_form.is_valid():
        #     vendor_form.save()
            
        #     messages.success(request, 'Changes updated successfuly')
        #     return redirect('vprofile')



   

    context = {
        'profile_form': profile_form,
        'vendor_form': vendor_form,
        'profile': profile,
        'vendor': vendor,
    }
    return render(request, 'vendor/vprofile.html', context)