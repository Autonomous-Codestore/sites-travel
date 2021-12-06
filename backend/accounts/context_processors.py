from .models import Index

def global_temp(request):
    try:
        temp = Index.objects.latest('last_updated')
    except:
        temp = ""
    return {
        "temp": temp
    }
        