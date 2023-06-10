from django.shortcuts import render

def index(request):
    return render(request, 'C:\\Users\\HP\\Desktop\\piyush django\\mysite\\polls1\\templates\\index.html', {'title': 'Hello World!'})
