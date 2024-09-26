from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from accounts.forms import UserProfileForm
from accounts.models import UserProfile
from menu.models import Category, FoodItem
from .models import Vendor
from .forms import VendorForm
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.views import check_role_vendor 


def get_vendor(request):
    vendor = Vendor.objects.get(user=request.user)
    return vendor

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
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

        

   

    context = {
        'profile_form': profile_form,
        'vendor_form': vendor_form,
        'profile': profile,
        'vendor': vendor,
    }
    return render(request, 'vendor/vprofile.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def menu_builder(request):
    vendor = get_vendor(request)
    categories = Category.objects.filter(vendor=vendor)
    context = {
        'categories': categories,

    }
    return render(request, 'vendor/menu_builder.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def fooditems_by_category(request, pk = None):
    vendor = get_vendor(request)
    category = get_object_or_404(Category, pk = pk)
    fooditems = FoodItem.objects.filter(vendor=vendor, category=category)
    context = {
        'fooditems': fooditems,
        'category': category,
    }
    return render(request, 'vendor/fooditems_by_category.html', context)