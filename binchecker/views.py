import http.client
import json
from django.shortcuts import render
from django.http import JsonResponse

def check_bin(request):
    if request.method == 'POST':
        bin_number = json.loads(request.body).get('bin')

        conn = http.client.HTTPSConnection("bin-ip-checker.p.rapidapi.com")
        
        payload = json.dumps({"bin": bin_number})
        
        headers = {
            'x-rapidapi-key': "e1326a9c62msh4c90aa7db28b09fp13482cjsnbaa9986d5d44",
            'x-rapidapi-host': "bin-ip-checker.p.rapidapi.com",
            'Content-Type': "application/json"
        }

        conn.request("POST", f"/?bin={bin_number}", payload, headers)
        
        res = conn.getresponse()
        data = res.read()
        
        # Decode the response and convert it to a dictionary
        response_data = json.loads(data.decode("utf-8"))

        # Check if the response is successful
        if res.status == 200:
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Failed to retrieve data'}, status=res.status)
    
    # Render the template for GET requests
    return render(request, 'binchecker/index.html')
