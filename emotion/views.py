import requests
from django.shortcuts import render
from django.http import JsonResponse

def emotion_analysis(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        url = "https://api.apilayer.com/text_to_emotion"
        payload = text.encode("utf-8")
        headers = {
            "apikey": "xyT0w6LeD8L1IjvSEtoYzKBE3uuCXTIT"
        }

        try:
            response = requests.post(url, headers=headers, data=payload)
            status_code = response.status_code
            
            if status_code == 200:
                result = response.json()
                return JsonResponse(result)
            elif status_code == 400:
                return JsonResponse({'error': 'Bad request. Please check your input.'}, status=400)
            elif status_code == 401:
                return JsonResponse({'error': 'Unauthorized. Please check your API key.'}, status=401)
            elif status_code == 403:
                return JsonResponse({'error': 'Forbidden. You do not have access to this API.'}, status=403)
            elif status_code == 404:
                return JsonResponse({'error': 'Not found. Please check the API endpoint.'}, status=404)
            elif status_code == 500:
                return JsonResponse({'error': 'Internal server error. Please try again later.'}, status=500)
            else:
                return JsonResponse({'error': f'Unexpected error occurred. Status code: {status_code}'}, status=status_code)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    return render(request, 'emotion_form.html')
