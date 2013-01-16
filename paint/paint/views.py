from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from paintapp.models import Image
def mainPage(request):
	if request.method=='GET':
		t = get_template('paint.html')
		html = t.render(Context({}))
		return HttpResponse(html)
	
def loadPage(request,fname):
	if request.method=='GET':
		data=Image.objects.filter(name=fname)
		t = get_template('paint.html')
		html = t.render(Context({}))
		if data:
			html="""<script>var data=JSON.parse(' """+data[0].data+""" ');</script>"""+html		
		else:
			html="""<script>alert("Image not found")</script>"""+html
		return HttpResponse(html)
	else:
		
		imgname=request.POST.get('pname')
		imgdata=request.POST.get('pdata')
		try:
  			p = Image.objects.get(name=imgname)
		except Image.DoesNotExist:
    			p=Image(name=imgname,data=imgdata)
			p.save()
		else:
    			p.data=imgdata
			p.save()

