# UmaSimCraft - Data Cards Django 앱 개발서

**개발 기간**: 4주 (1개월)  
**목표**: 우마무스메 데이터베이스(캐릭터·서포트 카드·스킬)를 "카드(Grid) → 팝카드(Modal)" UI로 탐색·검색할 수 있는 독립 Django 앱

---

## 1. 범위(Scope)

### 1.1 포함 사항

- 캐릭터·서포트·스킬 **읽기 전용** 리스트 & 상세 보기
- Tailwind + Django Template 카드 UI
- 키워드·태그·필터·정렬 기능
- HTMX/Alpine.js 기반 Modal(PopCard)

### 1.2 제외 사항

- CRUD(신규 작성·수정·삭제) - 읽기 전용만
- 관리자 전용 페이지 (Django Admin으로 대신)
- 모바일 전용 네이티브 앱
- OAuth·복잡한 인증

---

## 2. 기술 스택 / 아키텍처

### 2.1 기술 스택

| 계층     | 선택 기술 · 라이브러리                                | 비고                             |
| -------- | ----------------------------------------------------- | -------------------------------- |
| 백엔드   | Django 5.2.4 · Django REST Framework 3.16.0           | 기존 프로젝트와 동일 버전 유지   |
| 프론트   | Django Templates + TailwindCSS 4.2.0 + HTMX/Alpine.js | 전면 SPA 대신 MPA+HTMX 경량 구현 |
| 컴포넌트 | daisyUI v5 모달 컴포넌트                              | 팝카드 전용                      |
| 테스트   | Pytest-django · Playwright(e2e)                       | Grid 및 Modal 동작 검증          |
| 배포     | GitHub Actions → Heroku(Docker) staging               | 기존 CI 파이프라인 재사용        |

### 2.2 아키텍처

```
┌───────────── Browser ─────────────┐
│  Tailwind + daisyUI + HTMX       │
│  Grid Cards → Modal Popup        │
└───────▲──────────┬───────────▲────┘
        │ REST     │ WS        │ Static
┌───────┴──────────┴───────────┴────┐
│          Django 서버 (ASGI)       │
│  • cards/ 앱 (새로 추가)          │
│  • DRF API (기존)                 │
│  • HTMX + Alpine.js               │
└────────┬──────────┬───────────┬───┘
         │          │           │
         │  Redis   │           │
┌────────▼──────────┴───────────▼───┐
│              MariaDB 11           │
│   기존 simulator/ 모델 재사용      │
└───────────────────────────────────┘
```

---

## 3. 일정(한눈에 보기)

| 주차                 | 핵심 산출물(Milestone)                                         | 주요 작업                                                                                                               |
| -------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **W1 (설계)**        | ▸ 요구사항 명세서 v1<br>▸ 정보구조(IA) & UI wireframe          | - 페이지 플로우·URL·라우팅 정의<br>- 카드 컴포넌트 base 디자인<br>- Modal 인터랙션 패턴 결정                            |
| **W2 (백엔드 API)**  | ▸ `/api/cards/characters/…` `/supports/…` `/skills/…` 읽기 API | - Serializer·ViewSet·URLConf 작성<br>- 페이지네이션·검색(이름·ID·태그) 필터<br>- unit 테스트·OpenAPI schema             |
| **W3 (프론트 UI)**   | ▸ Grid 카드 리스트 화면<br>▸ 팝카드(Modal) 상세                | - Tailwind 카드 컴포넌트 구현<br>- HTMX `hx-get` 로 Modal lazy-load<br>- 리스트 필터 UI (select, search box)            |
| **W4 (품질 & 배포)** | ▸ e2e 테스트 통과<br>▸ Staging 배포 릴리스 v0.1                | - Lighthouse 95+ (접근성·성능)<br>- Playwright 시나리오 작성<br>- GitHub Actions 파이프라인 확장<br>- Release note 작성 |

---

## 4. 세부 작업 분해(Work Breakdown Structure)

### 4.1 설계 Phase (W1)

| #   | Task                                  | Owner         | Est. |
| --- | ------------------------------------- | ------------- | ---- |
| 1   | 비즈니스 요구 재확인 & 스펙 확정      | PO + Dev Lead | 0.5d |
| 2   | 엔드포인트 목록·데이터 모델 매핑 시트 | BE            | 0.5d |
| 3   | **Wireframe** (Figma) 카드/Modal      | FE            | 1d   |
| 4   | URL & 네비게이션 설계 (`cards/`)      | BE + FE       | 0.5d |
| 5   | Definition of Done & 테스트 기준 설정 | QA            | 0.5d |

### 4.2 백엔드 Phase (W2)

| #   | Task                                        | Est.  | Notes                             |
| --- | ------------------------------------------- | ----- | --------------------------------- |
| 1   | App scaffolding `cards/` (settings 등록)    | 0.25d | `python manage.py startapp cards` |
| 2   | Serializer 작성 (Character, Support, Skill) | 0.5d  | 필드 subset 선택                  |
| 3   | Generic ViewSet + Router 등록               | 0.5d  | DRF ModelViewSet                  |
| 4   | 필터/검색 (django-filter)                   | 0.5d  | name\_\_icontains, types          |
| 5   | Pagination (PageNumber, 20/page)            | 0.25d |                                   |
| 6   | 단위 테스트 (pytest)                        | 0.5d  | 90% 커버리지 목표                 |
| 7   | Swagger / Redoc 문서                        | 0.25d | drf-spectacular                   |

### 4.3 프론트 Phase (W3)

| #   | Task                             | Est.  | Notes                        |
| --- | -------------------------------- | ----- | ---------------------------- |
| 1   | Tailwind card 컴포넌트 구축      | 0.75d | Reuse in 3 types             |
| 2   | Grid 레이아웃 + pagination UI    | 0.5d  | 3 cols (desktop) / 2 / 1     |
| 3   | 검색·필터 폼 (GET param)         | 0.5d  | Turbo-link 유지              |
| 4   | Modal 팝카드 (HTMX)              | 1d    | hx-get=`/cards/{id}/partial` |
| 5   | 반응형 & a11y 개선               | 0.5d  | aria-label, sr-only          |
| 6   | Vue/React 고려? → MVP에서는 HTMX | —     | 후속 스프린트 전환 여지      |

### 4.4 품질·배포 Phase (W4)

| #   | Task                            | Est.  | Notes              |
| --- | ------------------------------- | ----- | ------------------ |
| 1   | Playwright e2e (목록→Modal)     | 1d    | GitHub Action 병행 |
| 2   | Lighthouse 최적화 & 이미지 lazy | 0.5d  | Score 95+          |
| 3   | Staging Dockerfile & Procfile   | 0.25d | Heroku container   |
| 4   | CI workflow 수정 & CD trigger   | 0.5d  | PR → auto deploy   |
| 5   | 버전 태그 (v0.1.0) & Docs       | 0.25d | CHANGELOG, README  |

---

## 5. 데이터 모델 설계

### 5.1 기존 모델 재사용

```python
# apps/simulator/models/character.py (기존)
class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    # ... 기존 필드들

# apps/simulator/models/support_card.py (기존)
class SupportCard(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    rarity = models.CharField(max_length=20)
    card_type = models.CharField(max_length=50)
    # ... 기존 필드들

# apps/simulator/models/skill.py (기존)
class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    description = models.TextField()
    skill_type = models.CharField(max_length=50)
    # ... 기존 필드들
```

### 5.2 cards 앱 모델 (선택적)

```python
# apps/cards/models.py (새로 추가)
class CardView(models.Model):
    """카드 조회 히스토리 (선택적)"""
    card_type = models.CharField(max_length=20)  # character, support, skill
    card_id = models.IntegerField()
    viewed_at = models.DateTimeField(auto_now_add=True)
    user_session = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'card_views'
        indexes = [
            models.Index(fields=['card_type', 'card_id']),
            models.Index(fields=['viewed_at']),
        ]
```

---

## 6. API 설계

### 6.1 REST API 엔드포인트

```python
# apps/cards/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'characters', views.CharacterViewSet, basename='character')
router.register(r'supports', views.SupportCardViewSet, basename='support')
router.register(r'skills', views.SkillViewSet, basename='skill')

urlpatterns = [
    path('api/cards/', include(router.urls)),
    path('cards/', views.CardListView.as_view(), name='card-list'),
    path('cards/<str:card_type>/<int:pk>/', views.CardDetailView.as_view(), name='card-detail'),
    path('cards/<str:card_type>/<int:pk>/partial/', views.CardPartialView.as_view(), name='card-partial'),
]
```

### 6.2 Serializer 설계

```python
# apps/cards/serializers.py
from rest_framework import serializers
from apps.simulator.models import Character, SupportCard, Skill

class CharacterListSerializer(serializers.ModelSerializer):
    """캐릭터 리스트용 (간소화된 필드)"""
    class Meta:
        model = Character
        fields = ['id', 'name', 'name_en', 'rarity', 'initial_stats']

class CharacterDetailSerializer(serializers.ModelSerializer):
    """캐릭터 상세용 (전체 필드)"""
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = '__all__'

    def get_skills(self, obj):
        return [{'id': skill.id, 'name': skill.name} for skill in obj.skills.all()]

class SupportCardListSerializer(serializers.ModelSerializer):
    """서포트 카드 리스트용"""
    class Meta:
        model = SupportCard
        fields = ['id', 'name', 'name_en', 'rarity', 'card_type']

class SupportCardDetailSerializer(serializers.ModelSerializer):
    """서포트 카드 상세용"""
    skills = serializers.SerializerMethodField()

    class Meta:
        model = SupportCard
        fields = '__all__'

    def get_skills(self, obj):
        return [{'id': skill.id, 'name': skill.name} for skill in obj.skills.all()]

class SkillListSerializer(serializers.ModelSerializer):
    """스킬 리스트용"""
    class Meta:
        model = Skill
        fields = ['id', 'name', 'name_en', 'skill_type']

class SkillDetailSerializer(serializers.ModelSerializer):
    """스킬 상세용"""
    class Meta:
        model = Skill
        fields = '__all__'
```

### 6.3 ViewSet 설계

```python
# apps/cards/views.py
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.simulator.models import Character, SupportCard, Skill
from .serializers import *

class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    """캐릭터 API (읽기 전용)"""
    queryset = Character.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rarity']
    search_fields = ['name', 'name_en']
    ordering_fields = ['name', 'rarity', 'id']
    ordering = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return CharacterListSerializer
        return CharacterDetailSerializer

class SupportCardViewSet(viewsets.ReadOnlyModelViewSet):
    """서포트 카드 API (읽기 전용)"""
    queryset = SupportCard.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rarity', 'card_type']
    search_fields = ['name', 'name_en']
    ordering_fields = ['name', 'rarity', 'card_type', 'id']
    ordering = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return SupportCardListSerializer
        return SupportCardDetailSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """스킬 API (읽기 전용)"""
    queryset = Skill.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['skill_type']
    search_fields = ['name', 'name_en', 'description']
    ordering_fields = ['name', 'skill_type', 'id']
    ordering = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return SkillListSerializer
        return SkillDetailSerializer
```

---

## 7. 프론트엔드 설계

### 7.1 URL 구조

```python
# apps/cards/urls.py (템플릿 뷰)
urlpatterns = [
    path('cards/', views.CardListView.as_view(), name='card-list'),
    path('cards/characters/', views.CharacterListView.as_view(), name='character-list'),
    path('cards/supports/', views.SupportCardListView.as_view(), name='support-list'),
    path('cards/skills/', views.SkillListView.as_view(), name='skill-list'),
    path('cards/<str:card_type>/<int:pk>/', views.CardDetailView.as_view(), name='card-detail'),
    path('cards/<str:card_type>/<int:pk>/partial/', views.CardPartialView.as_view(), name='card-partial'),
]
```

### 7.2 템플릿 구조

```
templates/
├── cards/
│   ├── base.html              # 카드 앱 기본 레이아웃
│   ├── list.html              # 카드 그리드 리스트
│   ├── detail.html            # 카드 상세 페이지
│   ├── partial.html           # HTMX 모달용 부분 템플릿
│   └── components/
│       ├── card_grid.html     # 카드 그리드 컴포넌트
│       ├── card_item.html     # 개별 카드 컴포넌트
│       ├── modal.html         # 모달 컴포넌트
│       ├── filter_form.html   # 필터 폼 컴포넌트
│       └── pagination.html    # 페이지네이션 컴포넌트
```

### 7.3 카드 컴포넌트 설계

```html
<!-- templates/cards/components/card_item.html -->
<div
  class="card bg-base-100 shadow-xl hover:shadow-2xl transition-shadow cursor-pointer"
  hx-get="{% url 'card-partial' card_type=card_type pk=card.id %}"
  hx-target="#modal-content"
  hx-trigger="click"
  _="on click add .modal-open to #card-modal"
>
  <figure class="px-4 pt-4">
    <img
      src="{{ card.image_url|default:'/static/img/default-card.png' }}"
      alt="{{ card.name }}"
      class="rounded-xl h-32 w-24 object-cover"
    />
  </figure>
  <div class="card-body p-4">
    <h2 class="card-title text-sm">{{ card.name }}</h2>
    <div class="badge badge-{{ card.rarity|lower }}">{{ card.rarity }}</div>
    {% if card.card_type %}
    <div class="badge badge-outline">{{ card.card_type }}</div>
    {% endif %}
  </div>
</div>
```

### 7.4 모달 컴포넌트 설계

```html
<!-- templates/cards/components/modal.html -->
<div id="card-modal" class="modal">
  <div class="modal-box w-11/12 max-w-5xl">
    <div id="modal-content" class="p-4">
      <!-- HTMX로 동적 로드 -->
      <div class="loading loading-spinner loading-lg"></div>
    </div>
    <div class="modal-action">
      <button class="btn" onclick="closeModal()">닫기</button>
    </div>
  </div>
</div>

<script>
  function closeModal() {
    document.getElementById("card-modal").classList.remove("modal-open");
  }
</script>
```

---

## 8. 리스크 & 대응

| 리스크                          | 대응 방안                                               |
| ------------------------------- | ------------------------------------------------------- |
| DB 레코드 대량 → 최초 로딩 느림 | 서버 pagination + Skeleton UI + lazy Modal              |
| 모바일 해상도 카드 UX           | Tailwind breakpoint 검증, 디자인 QA                     |
| 향후 CRUD 확장시 인증 필요      | 초기엔 읽기 전용, 차기 스프린트에서 JWT/OAuth 도입 검토 |

---

## 9. 성공 지표(Definition of Done)

### 9.1 기능적 요구사항

- [ ] 캐릭터/서포트/스킬 3종 데이터 모두 Grid 렌더링
- [ ] Modal 세부 정보 표시
- [ ] 검색 및 필터 기능
- [ ] 페이지네이션
- [ ] 반응형 디자인

### 9.2 품질 요구사항

- [ ] Lighthouse ≥ 95 (접근성·성능)
- [ ] Playwright e2e 전부 pass
- [ ] < 2초 내 첫 콘텐츠풀 페인트 (FCP) @ 3G Slow
- [ ] 90%+ 테스트 커버리지

### 9.3 문서화 요구사항

- [ ] README + API Swagger
- [ ] 배포 가이드 포함
- [ ] 사용자 매뉴얼

---

## 10. 이후 로드맵(후속 2개월 제안)

| 스프린트 | 내용                                                                 |
| -------- | -------------------------------------------------------------------- |
| **M2**   | 즐겨찾기(Star) · 태그 편집(유저 CRUD) · Infinite Scroll              |
| **M3**   | Vue.js 혹은 React Refactor · 다국어(I18N) 지원 · 캐릭터/스킬 비교 툴 |

---

## 11. 개발 환경 설정

### 11.1 의존성 추가

```bash
# requirements.txt에 추가
django-filter==24.1
drf-spectacular==0.27.1
playwright==1.42.0
```

### 11.2 앱 생성

```bash
python manage.py startapp cards apps/
```

### 11.3 설정 파일 업데이트

```python
# umasimcraft/settings.py
INSTALLED_APPS = [
    # ... 기존 앱들
    'apps.cards',
    'django_filters',
    'drf_spectacular',
]

# REST Framework 설정
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
```

---

**문서 버전**: 1.0  
**작성일**: 2024년 4월 1일  
**검토일**: 주간  
**다음 업데이트**: 2024년 5월 1일
