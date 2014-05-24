from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(response):
	context = RequestContext(response)

	contextDict = []

	return render_to_response('index.html', contextDict, context)
