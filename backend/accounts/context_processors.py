from .models import Index
from datetime import datetime

def global_temp(request):
    try:
        temp = Index.objects.latest('last_updated')
    except:
        Index.objects.create(about_us="A description of the sites safari website", about_image="", 
        address="Kampala, Uganda", tel_1="+256 414 347 443", tel_2="+256 414 347 443", 
        email="reservations@sitestravel-ug.com", facebook="facebook link", twitter="twitter link", youtube="youtube link", 
        instagram="instagram link", last_updated=datetime.now())
        temp = Index.objects.latest('last_updated')
    return {
        "temp": temp
    }
        