from django.shortcuts import render

def indexpage(request):
    return render(request, "index.html")

def submitquery(request):
    q = request.GET.get('query', None)
    if q is not None:
        try:
            ans = eval(q)
            mydict = {
                "q": q,
                "ans": ans,
                "error": False,
                "result": True
            }
        except Exception as e:
            mydict = {
                "error": True,
                "result": False
            }
    else:
        mydict = {
            "error": True,
            "result": False
        }

    return render(request, "index.html", context=mydict)
