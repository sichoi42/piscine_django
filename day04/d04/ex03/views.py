from django.shortcuts import render

# Create your views here.

def coloring(request):
	interval = 5
	shade = [i * interval for i in range(50)]
	context = {'shade': shade, }
	return render(request, 'color.html', context)
