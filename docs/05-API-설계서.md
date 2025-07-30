# UmaSimCraft API 설계서

## 1. API 개요

### 1.1 API 버전 관리
- **현재 버전**: v1.0
- **기본 URL**: `https://api.umasimcraft.com/v1/`
- **로컬 개발**: `http://localhost:8000/api/v1/`

### 1.2 인증 방식
- **JWT 토큰**: Bearer 토큰 방식
- **API 키**: 개발자용 API 키 (선택사항)
- **Rate Limiting**: IP당 분당 1000 요청

### 1.3 응답 형식
모든 API 응답은 JSON 형식으로 통일:

```json
{
  "status": "success|error",
  "data": {
    // 실제 데이터
  },
  "meta": {
    "timestamp": "2025-01-27T10:30:00Z",
    "version": "1.0",
    "request_id": "uuid-string"
  },
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 100,
    "total_pages": 5
  }
}
```

## 2. REST API 엔드포인트

### 2.1 캐릭터 API

#### GET /api/v1/characters/
캐릭터 목록 조회

**Query Parameters:**
- `page` (int): 페이지 번호 (기본값: 1)
- `per_page` (int): 페이지당 항목 수 (기본값: 20, 최대: 100)
- `rarity` (string): 희귀도 필터 (SSR, SR, R)
- `search` (string): 이름 검색

**Response:**
```json
{
  "status": "success",
  "data": [
    {
      "id": 10001,
      "name": "스페셜월",
      "name_en": "Special Week",
      "rarity": "SSR",
      "initial_stats": {
        "speed": 100,
        "stamina": 80,
        "power": 90,
        "guts": 85,
        "intelligence": 75
      },
      "growth_rates": {
        "speed": 1.2,
        "stamina": 1.1,
        "power": 1.15,
        "guts": 1.05,
        "intelligence": 1.0
      },
      "image_url": "/static/img/characters/10001.png"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 150,
    "total_pages": 8
  }
}
```

#### GET /api/v1/characters/{id}/
캐릭터 상세 정보 조회

**Response:**
```json
{
  "status": "success",
  "data": {
    "id": 10001,
    "name": "스페셜월",
    "name_en": "Special Week",
    "rarity": "SSR",
    "initial_stats": {
      "speed": 100,
      "stamina": 80,
      "power": 90,
      "guts": 85,
      "intelligence": 75
    },
    "growth_rates": {
      "speed": 1.2,
      "stamina": 1.1,
      "power": 1.15,
      "guts": 1.05,
      "intelligence": 1.0
    },
    "max_stats": {
      "speed": 1200,
      "stamina": 1000,
      "power": 1100,
      "guts": 1050,
      "intelligence": 950
    },
    "skills": [
      {
        "id": 20001,
        "name": "스피드스타",
        "name_en": "Speed Star",
        "description": "스피드가 대폭 상승",
        "rarity": "SSR"
      }
    ],
    "image_url": "/static/img/characters/10001.png"
  }
}
```

#### GET /api/v1/characters/{id}/skills/
캐릭터 스킬 목록 조회

**Response:**
```json
{
  "status": "success",
  "data": [
    {
      "id": 20001,
      "name": "스피드스타",
      "name_en": "Speed Star",
      "description": "스피드가 대폭 상승",
      "skill_type": "speed",
      "activation_condition": {
        "position": "front",
        "distance": "short"
      },
      "effect_value": {
        "speed_bonus": 0.2
      },
      "rarity": "SSR",
      "unlock_level": 1
    }
  ]
}
```

### 2.2 서포트 카드 API

#### GET /api/v1/support-cards/
서포트 카드 목록 조회

**Query Parameters:**
- `page` (int): 페이지 번호
- `per_page` (int): 페이지당 항목 수
- `rarity` (string): 희귀도 필터
- `card_type` (string): 카드 타입 필터 (speed, stamina, power, guts, intelligence)
- `search` (string): 이름 검색

**Response:**
```json
{
  "status": "success",
  "data": [
    {
      "id": 30001,
      "name": "사이렌스스즈카",
      "name_en": "Silence Suzuka",
      "rarity": "SSR",
      "card_type": "speed",
      "stats_bonus": {
        "speed": 0.15,
        "stamina": 0.05
      },
      "friendship_bonus": {
        "speed_training": 0.1,
        "stamina_training": 0.05
      },
      "image_url": "/static/img/support_cards/30001.png"
    }
  ]
}
```

#### GET /api/v1/support-cards/{id}/
서포트 카드 상세 정보 조회

**Response:**
```json
{
  "status": "success",
  "data": {
    "id": 30001,
    "name": "사이렌스스즈카",
    "name_en": "Silence Suzuka",
    "rarity": "SSR",
    "card_type": "speed",
    "stats_bonus": {
      "speed": 0.15,
      "stamina": 0.05
    },
    "friendship_bonus": {
      "speed_training": 0.1,
      "stamina_training": 0.05
    },
    "skills": [
      {
        "id": 20002,
        "name": "스피드업",
        "name_en": "Speed Up",
        "description": "스피드가 상승",
        "unlock_level": 1
      }
    ],
    "image_url": "/static/img/support_cards/30001.png"
  }
}
```

### 2.3 스킬 API

#### GET /api/v1/skills/
스킬 목록 조회

**Query Parameters:**
- `page` (int): 페이지 번호
- `per_page` (int): 페이지당 항목 수
- `skill_type` (string): 스킬 타입 필터
- `rarity` (string): 희귀도 필터
- `search` (string): 이름/설명 검색

**Response:**
```json
{
  "status": "success",
  "data": [
    {
      "id": 20001,
      "name": "스피드스타",
      "name_en": "Speed Star",
      "description": "스피드가 대폭 상승",
      "skill_type": "speed",
      "activation_condition": {
        "position": "front",
        "distance": "short"
      },
      "effect_value": {
        "speed_bonus": 0.2
      },
      "rarity": "SSR"
    }
  ]
}
```

#### GET /api/v1/skills/{id}/
스킬 상세 정보 조회

**Response:**
```json
{
  "status": "success",
  "data": {
    "id": 20001,
    "name": "스피드스타",
    "name_en": "Speed Star",
    "description": "스피드가 대폭 상승",
    "skill_type": "speed",
    "activation_condition": {
      "position": "front",
      "distance": "short",
      "speed_threshold": 800
    },
    "effect_value": {
      "speed_bonus": 0.2,
      "duration": 3
    },
    "rarity": "SSR",
    "characters": [
      {
        "id": 10001,
        "name": "스페셜월",
        "unlock_level": 1
      }
    ],
    "support_cards": [
      {
        "id": 30001,
        "name": "사이렌스스즈카",
        "unlock_level": 1
      }
    ]
  }
}
```

#### GET /api/v1/skills/search/
스킬 검색

**Query Parameters:**
- `q` (string): 검색어 (필수)
- `skill_type` (string): 스킬 타입 필터
- `rarity` (string): 희귀도 필터

**Response:**
```json
{
  "status": "success",
  "data": [
    {
      "id": 20001,
      "name": "스피드스타",
      "name_en": "Speed Star",
      "description": "스피드가 대폭 상승",
      "skill_type": "speed",
      "rarity": "SSR",
      "relevance_score": 0.95
    }
  ]
}
```

### 2.4 시뮬레이션 API

#### POST /api/v1/simulate/
시뮬레이션 실행

**Request Body:**
```json
{
  "character_id": 10001,
  "support_cards": [30001, 30002, 30003, 30004, 30005],
  "target_stats": {
    "speed": 1000,
    "stamina": 800,
    "power": 900,
    "guts": 850,
    "intelligence": 750
  },
  "options": {
    "iterations": 1000,
    "training_focus": "speed",
    "race_strategy": "front",
    "monte_carlo": true
  }
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "session_id": "uuid-string",
    "status": "running",
    "estimated_duration": 30,
    "progress_url": "/api/v1/simulate/uuid-string/progress/"
  }
}
```

#### GET /api/v1/simulate/{session_id}/
시뮬레이션 결과 조회

**Response:**
```json
{
  "status": "success",
  "data": {
    "session_id": "uuid-string",
    "status": "completed",
    "character": {
      "id": 10001,
      "name": "스페셜월"
    },
    "support_cards": [
      {
        "id": 30001,
        "name": "사이렌스스즈카"
      }
    ],
    "target_stats": {
      "speed": 1000,
      "stamina": 800
    },
    "results": {
      "success_rate": 0.85,
      "average_final_stats": {
        "speed": 1050,
        "stamina": 820,
        "power": 910,
        "guts": 860,
        "intelligence": 760
      },
      "best_result": {
        "final_stats": {
          "speed": 1100,
          "stamina": 850
        },
        "training_path": [
          {
            "turn": 1,
            "action": "speed_training",
            "stat_changes": {"speed": 15}
          }
        ]
      },
      "recommended_actions": [
        {
          "turn": 1,
          "action": "speed_training",
          "confidence": 0.95
        }
      ]
    },
    "created_at": "2025-01-27T10:30:00Z",
    "completed_at": "2025-01-27T10:30:30Z"
  }
}
```

#### GET /api/v1/simulate/{session_id}/progress/
시뮬레이션 진행률 조회 (WebSocket 대안)

**Response:**
```json
{
  "status": "success",
  "data": {
    "session_id": "uuid-string",
    "progress": 0.65,
    "current_iteration": 650,
    "total_iterations": 1000,
    "estimated_remaining_time": 10,
    "current_best_result": {
      "final_stats": {
        "speed": 1080,
        "stamina": 830
      }
    }
  }
}
```

### 2.5 통계 API

#### GET /api/v1/stats/characters/
캐릭터 통계

**Response:**
```json
{
  "status": "success",
  "data": {
    "total_characters": 150,
    "by_rarity": {
      "SSR": 30,
      "SR": 50,
      "R": 70
    },
    "most_popular": [
      {
        "id": 10001,
        "name": "스페셜월",
        "simulation_count": 1500
      }
    ]
  }
}
```

#### GET /api/v1/stats/support-cards/
서포트 카드 통계

**Response:**
```json
{
  "status": "success",
  "data": {
    "total_support_cards": 200,
    "by_type": {
      "speed": 40,
      "stamina": 35,
      "power": 30,
      "guts": 25,
      "intelligence": 20
    },
    "most_used": [
      {
        "id": 30001,
        "name": "사이렌스스즈카",
        "usage_count": 2500
      }
    ]
  }
}
```

## 3. WebSocket API

### 3.1 WebSocket 연결

**URL**: `ws://localhost:8000/ws/simulate/{session_id}/`

**연결 예시:**
```javascript
const socket = new WebSocket(`ws://localhost:8000/ws/simulate/${sessionId}/`);

socket.onopen = function(event) {
    console.log('WebSocket connected');
};

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    console.log('Received:', data);
};

socket.onclose = function(event) {
    console.log('WebSocket disconnected');
};
```

### 3.2 메시지 형식

#### 시뮬레이션 진행률 메시지
```json
{
  "type": "simulation.progress",
  "data": {
    "session_id": "uuid-string",
    "progress": 0.45,
    "current_iteration": 450,
    "total_iterations": 1000,
    "estimated_remaining_time": 15,
    "current_best_result": {
      "final_stats": {
        "speed": 1050,
        "stamina": 820
      }
    }
  }
}
```

#### 시뮬레이션 완료 메시지
```json
{
  "type": "simulation.completed",
  "data": {
    "session_id": "uuid-string",
    "results": {
      "success_rate": 0.85,
      "average_final_stats": {
        "speed": 1050,
        "stamina": 820
      }
    }
  }
}
```

#### 에러 메시지
```json
{
  "type": "error",
  "data": {
    "code": "SIMULATION_ERROR",
    "message": "Invalid character ID",
    "details": {
      "character_id": 99999
    }
  }
}
```

## 4. 에러 처리

### 4.1 에러 응답 형식
```json
{
  "status": "error",
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "character_id": ["This field is required."],
      "support_cards": ["Must select exactly 5 support cards."]
    }
  },
  "meta": {
    "timestamp": "2025-01-27T10:30:00Z",
    "version": "1.0",
    "request_id": "uuid-string"
  }
}
```

### 4.2 에러 코드 목록
| 코드 | HTTP 상태 | 설명 |
|------|-----------|------|
| `VALIDATION_ERROR` | 400 | 입력 데이터 검증 실패 |
| `NOT_FOUND` | 404 | 리소스를 찾을 수 없음 |
| `RATE_LIMIT_EXCEEDED` | 429 | 요청 제한 초과 |
| `SIMULATION_ERROR` | 500 | 시뮬레이션 실행 오류 |
| `DATABASE_ERROR` | 500 | 데이터베이스 오류 |

## 5. 인증 및 보안

### 5.1 JWT 토큰 인증
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

### 5.2 Rate Limiting
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1000/minute',
        'user': '5000/minute',
        'simulation': '100/minute'
    }
}
```

### 5.3 CORS 설정
```python
# settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://umasimcraft.com",
]

CORS_ALLOW_CREDENTIALS = True
```

## 6. API 문서화

### 6.1 Swagger/OpenAPI
```python
# urls.py
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
```

### 6.2 API 버전 관리
```python
# views.py
from rest_framework.versioning import URLPathVersioning

class CharacterViewSet(viewsets.ModelViewSet):
    versioning_class = URLPathVersioning
    
    def get_queryset(self):
        if self.request.version == '1.0':
            return Character.objects.all()
        elif self.request.version == '2.0':
            return Character.objects.select_related('skills')
```

## 7. 성능 최적화

### 7.1 캐싱 전략
```python
# views.py
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class CharacterViewSet(viewsets.ModelViewSet):
    @method_decorator(cache_page(60 * 15))  # 15분 캐시
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
```

### 7.2 데이터베이스 최적화
```python
# views.py
class CharacterViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Character.objects.select_related().prefetch_related('skills')
```

### 7.3 페이지네이션
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'MAX_PAGE_SIZE': 100,
}
```

---

**문서 버전**: v1.0  
**최종 업데이트**: 2025-01-27  
**작성자**: API 개발팀 