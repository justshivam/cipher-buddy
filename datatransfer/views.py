from django.shortcuts import render, redirect


def peer(request):
    if request.user.is_authenticated:
        return render(request, 'datatransfer/peer.html')
    else:
        return redirect('/')


def recText(request):
    if request.user.is_authenticated:
        return render(request, 'datatransfer/receive.html')
    else:
        return redirect('/')


def sendText(request):
    if request.user.is_authenticated:
        return render(request, 'datatransfer/send.html')
    else:
        return redirect('/')


def data(request):
    if request.user.is_authenticated:
        return render(request, 'datatransfer/data.html')
    else:
        return redirect('/')
