from .models import Settings



def get_context_process(request):
    data=Settings.objects.last()
    return {'settings_data':data}

