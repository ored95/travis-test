from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    try:
        result = ""
        triplet = ""
    
        if request.method == 'POST':
            triplet = '(' + request.POST.get('x-value') + ', ' + request.POST.get('y-value') + ', ' + request.POST.get('z-value') + ')'
            x = float(request.POST.get('x-value'))
            y = float(request.POST.get('y-value'))
            z = float(request.POST.get('z-value'))
        

            array = [abs(x), abs(y), abs(z)]
            array.sort()
            err = array[0] ** 2 + array[1] ** 2 - array[2] ** 2
            extendCaption = "A "
            if abs(err) > 1E-16:
                extendCaption += "non-"
            result = extendCaption + "Pythagore's triplet"

        return render(request, 'index.html', { 'triplet': triplet, 'result': result })
    except:
        return HttpResponse(status=404)