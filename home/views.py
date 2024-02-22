import csv
import secrets
import string
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PasswordForm
from .models import Password
def password(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PasswordForm()

    return render(request, "pages/password_form.html", {'form': form})
def edit_password(request, password_id):
    password_instance = get_object_or_404(Password, id=password_id)

    if request.method == "POST":
        form = PasswordForm(request.POST, instance=password_instance)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PasswordForm(instance=password_instance)

    return render(request, "pages/edit_password.html", {'form': form, 'password': password_instance})
def delete_password(request, password_id):
    password_instance = get_object_or_404(Password, id=password_id)

    if request.method == "POST":
        password_instance.delete()
        return JsonResponse({'message': 'Password deleted successfully'})

    return JsonResponse({'message': 'Invalid request'}, status=400)

def tables(request):
  passwords = Password.objects.all()
  return render(request, "pages/index.html", {"passwords" : passwords})