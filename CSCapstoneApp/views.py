"""CSCapstone Views

Created by Harris Christiansen on 9/18/16.
"""
from django.shortcuts import render

def getIndex(request):
	if request.user.is_authenticated():
		return render(request, 'index.html', {
			'auth': 'true',
		})
	else:
		return render(request, 'index.html', {
			'auth' : 'false'
		})

def getTable(request):
	return render(request, 'table.html')

def getForm(request):
	return render(request, 'form.html')