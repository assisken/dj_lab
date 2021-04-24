import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .models import EurovisionCelebrities
from .forms import CelebritiesForm

from redis import Redis

redis = Redis(host='localhost', port=6379)


class CelebrityCreateView(View):
    def get(self, request):
        celebs = EurovisionCelebrities.objects.all()
        form = CelebritiesForm()

        return render(request, 'create_celebrity.html', {
            'form': form.as_p(),
            'celebs': celebs,
        })

    def post(self, request):
        form = CelebritiesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')


class CelebrityEditView(View):
    def get(self, request, pk):
        cached_celeb = redis.get(pk)
        if cached_celeb is not None:
            celeb = EurovisionCelebrities.from_dict(json.loads(cached_celeb))
        else:
            celeb = EurovisionCelebrities.objects.get(pk=pk)
            redis.set(pk, json.dumps(celeb.as_dict()))

        form = CelebritiesForm(instance=celeb)

        return render(request, 'edit_celebrity.html', {
            'form': form.as_p(),
        })

    def post(self, request, pk):
        celeb = EurovisionCelebrities.objects.get(pk=pk)
        form = CelebritiesForm(request.POST, instance=celeb)

        if form.is_valid():
            form.save()
            redis.delete(pk)
            return HttpResponseRedirect('/')


class CelebrityDeleteView(View):
    def post(self, request, pk):
        celeb = EurovisionCelebrities.objects.get(pk=pk)
        celeb.delete()
        redis.delete(pk)
        return HttpResponseRedirect('/')
