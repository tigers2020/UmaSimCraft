from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    """시뮬레이션 메인 페이지"""
    return render(request, 'simulation/index.html')

def start_simulation(request):
    """시뮬레이션 시작"""
    if request.method == 'POST':
        # TODO: 시뮬레이션 로직 구현
        return JsonResponse({'status': 'success', 'message': '시뮬레이션이 시작되었습니다.'})
    return JsonResponse({'status': 'error', 'message': '잘못된 요청입니다.'})

def simulation_result(request, simulation_id):
    """시뮬레이션 결과 페이지"""
    # TODO: 시뮬레이션 결과 조회 로직 구현
    context = {
        'simulation_id': simulation_id,
    }
    return render(request, 'simulation/result.html', context)
