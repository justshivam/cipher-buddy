from django.shortcuts import render


def peer(request):
    return render(request, 'datatransfer/peer.html')


def recText(request):
    return render(request, 'datatransfer/receive.html')


def sendText(request):
    return render(request, 'datatransfer/send.html')
