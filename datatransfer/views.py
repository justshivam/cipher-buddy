from django.shortcuts import render


def peer(request):
    return render(request, 'datatransfer/peer.html')
