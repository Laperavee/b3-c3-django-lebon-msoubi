import csv
import secrets
import string
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PasswordForm
from .models import Password