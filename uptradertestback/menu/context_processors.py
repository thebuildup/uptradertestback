from django.urls import resolve


def active_menu(request):
    current_url = resolve(request.path_info)
    return {'current_url': current_url.namespace}
