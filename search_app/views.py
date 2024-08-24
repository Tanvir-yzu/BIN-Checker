import requests
from django.shortcuts import render

def search_view(request):
    query = request.GET.get('q', '')
    results = None

    if query:
        url = f"https://api.apilayer.com/google_search?q={query}"
        headers = {
            "apikey": "xyT0w6LeD8L1IjvSEtoYzKBE3uuCXTIT"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            results = response.json()  # Assuming the API returns JSON

    return render(request, 'search.html', {'query': query, 'results': results})
