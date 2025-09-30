from django.shortcuts import render, redirect

def index_redirect(request):
    return redirect('mapa')

def mapa_view(request):
    # Valores por defecto (ejemplo: Lima)
    lat = -12.0464
    lng = -77.0428

    if request.method == "POST":
        try:
            lat = float(request.POST.get("lat", lat))
            lng = float(request.POST.get("lng", lng))
        except ValueError:
            pass  # Si meten basura, se queda con los valores por defecto

    context = {
        'lat': lat,
        'lng': lng
    }
    return render(request, 'mapa.html', context)


