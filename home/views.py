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
def tables(request):
  passwords = Password.objects.all()
  return render(request, "pages/index.html", {"passwords" : passwords})