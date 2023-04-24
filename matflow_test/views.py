from django.http import JsonResponse

def api_view(request):
    response = {'message': 'Hello, world!'}
    return JsonResponse(response)
