import requests
from django.shortcuts import render
from .forms import PhoneNumberForm

def verify_phone_number(request):
    result = None
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            url = f"https://api.apilayer.com/number_verification/validate?number={phone_number}"
            headers = {
                "apikey": "xyT0w6LeD8L1IjvSEtoYzKBE3uuCXTIT"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                result = response.json()
    else:
        form = PhoneNumberForm()

    return render(request, 'verify.html', {'form': form, 'result': result})
