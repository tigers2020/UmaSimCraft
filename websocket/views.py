from django.shortcuts import render

# Create your views here.

def index(request):
    """WebSocket 테스트 페이지"""
    return render(request, 'websocket/index.html')
