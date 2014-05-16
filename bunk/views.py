from django.views import generic
from django.shortcuts import render
from django.utils import timezone
from bunk.models import Bunk
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def bunkFeed(request):
    bunk_list = Bunk.objects.order_by('-bunkTime')
    return render(request, 'bunk/feed.html', {
        'bunk_list': bunk_list
    })


# /bunk/1
def personalBunkFeed(request, user_id):

    ## if post:
    ##      do one thing
    ## else:
    ## default=True

    bunk_list = Bunk.objects.order_by('-bunkTime')
    user = User.objects.get(pk=user_id)
    return render(request, 'bunk/personalFeed.html', {
        'bunk_list': bunk_list,
        'user': user
    })


# /add/1 => /bunk/1
def bunkem(request, user_id):
    b = Bunk(
        bunkFrom=request.user,
        bunkTo=User.objects.get(pk=user_id),
    )
    b.save()

    return HttpResponseRedirect(
        reverse(
            'bunk:personalFeed',
            args=(User.objects.get(pk=user_id).id,)
        )
    )
