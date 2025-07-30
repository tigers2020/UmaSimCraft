from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    """API 문서 페이지"""
    return render(request, 'restapi/index.html')

def character_list(request):
    """캐릭터 목록 API"""
    # TODO: 캐릭터 데이터 조회 로직 구현
    characters = [
        {'id': 1, 'name': '스페셜 위크', 'rarity': 'SSR'},
        {'id': 2, 'name': '골드시티', 'rarity': 'SSR'},
        {'id': 3, 'name': '사일런스 스즈카', 'rarity': 'SR'},
    ]
    return JsonResponse({'characters': characters})

def support_card_list(request):
    """서포트 카드 목록 API"""
    # TODO: 서포트 카드 데이터 조회 로직 구현
    support_cards = [
        {'id': 1, 'name': '스페셜 위크', 'rarity': 'SSR'},
        {'id': 2, 'name': '골드시티', 'rarity': 'SSR'},
        {'id': 3, 'name': '사일런스 스즈카', 'rarity': 'SR'},
    ]
    return JsonResponse({'support_cards': support_cards})

def skill_list(request):
    """스킬 목록 API"""
    # TODO: 스킬 데이터 조회 로직 구현
    skills = [
        {'id': 1, 'name': '스피드', 'type': '스피드'},
        {'id': 2, 'name': '스태미나', 'type': '스태미나'},
        {'id': 3, 'name': '파워', 'type': '파워'},
    ]
    return JsonResponse({'skills': skills})
