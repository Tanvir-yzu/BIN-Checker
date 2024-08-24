import requests
from django.shortcuts import render
from django.http import HttpResponse,FileResponse

def capture_screenshot(request):
    if request.method == "POST":
        website_url = request.POST.get('website_url')
        url = f"https://api.apilayer.com/screenshot?url={website_url}&full=true"
        headers = {
            "apikey": "xyT0w6LeD8L1IjvSEtoYzKBE3uuCXTIT"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            screenshot_data = response.json()
            screenshot_url = screenshot_data.get("screenshot_url")
            return render(request, 'screenshot.html', {'screenshot_url': screenshot_url, 'website_url': website_url})
        else:
            return HttpResponse(f"Error: {response.status_code} - {response.text}")
    else:
        return render(request, 'screenshot.html')
    
    
def download_screenshot(request):
    screenshot_url = request.GET.get('url')
    if screenshot_url:
        response = requests.get(screenshot_url)
        if response.status_code == 200:
            # The screenshot filename can be inferred from the URL or you can set it explicitly
            filename = "screenshot.png"
            response = HttpResponse(response.content, content_type="image/png")
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    return HttpResponse("Screenshot could not be downloaded.")    
