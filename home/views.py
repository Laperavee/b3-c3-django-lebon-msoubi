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
def import_passwords_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']

        # Ensure the uploaded file is a CSV file
        if not csv_file.name.endswith('.csv'):
            return render(request, 'error.html', {'error': 'File is not a CSV'})

        # Process the CSV file
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.reader(decoded_file)
        next(csv_reader)  # Skip the header row

        for row in csv_reader:
            _, created = Password.objects.get_or_create(
                site=row[0],
                name_site=row[1],
                username=row[2],
                password=row[3]
            )

        return render(request, 'pages/success.html', {'message': 'Passwords imported successfully'})

    return render(request, 'pages/import_passwords.html')
def delete_password(request, password_id):
    password_instance = get_object_or_404(Password, id=password_id)

    if request.method == "POST":
        password_instance.delete()
        return JsonResponse({'message': 'Password deleted successfully'})

    return JsonResponse({'message': 'Invalid request'}, status=400)
def export_passwords_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="passwords.csv"'

    writer = csv.writer(response)
    writer.writerow(['site', 'name_site', 'username', 'password'])

    passwords = Password.objects.all()
    for password in passwords:
        writer.writerow([password.site, password.name_site, password.username, password.password])

    return response
def tables(request):
  passwords = Password.objects.all()
  return render(request, "pages/index.html", {"passwords" : passwords})