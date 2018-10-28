from django.shortcuts import render

def index(request):
    triplet = []

    if request.method == 'POST':
        triplet.append(request.POST.get('x-value'))
        triplet.append(request.POST.get('y-value'))
        triplet.append(request.POST.get('z-value'))

    return render(request, 'index.html', { 'triplet': triplet })