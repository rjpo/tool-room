from django.shortcuts import render

# Create your views here.
def data_list(request):
    return render(request, 'toolroom/data_list.html', {})