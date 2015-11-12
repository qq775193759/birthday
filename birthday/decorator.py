from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response


def show_message(request, msg):
    return render(request, "message.html",{'message':msg})

def method_required(mthd):
    def mthd_wrap(func):
        def wrap_func(request, *args, **kwargs):
            if not request.method == mthd:
                raise Http404
            return func(request, *args, **kwargs)
        return wrap_func
    return mthd_wrap