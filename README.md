# UmaSimCraft

우마무스메 육성 시뮬레이터 - 오프라인 환경에서 우마무스메 육성 시뮬레이션 및 최적화 추천 시스템

## 🏇 프로젝트 개요

UmaSimCraft는 우마무스메 프리티 더비 팬들을 위한 완전한 오프라인 육성 시뮬레이션 플랫폼입니다. 실시간 시뮬레이션, 데이터 분석, 최적화된 육성 전략 추천 기능을 제공합니다.

## ✨ 주요 기능

- **실시간 시뮬레이션**: 우마무스메 육성 과정을 실시간으로 시뮬레이션
- **데이터 분석**: 육성 결과 분석 및 최적화 전략 제안
- **오프라인 지원**: PWA를 통한 완전한 오프라인 기능
- **반응형 UI**: 모바일과 데스크톱에서 최적화된 사용자 경험
- **RESTful API**: 확장 가능한 API 구조

## 🛠 기술 스택

### Backend
- **Django 5.2.4**: 웹 프레임워크
- **Django REST Framework**: API 개발
- **Django Channels**: WebSocket 지원
- **MariaDB 11**: 메인 데이터베이스
- **Redis 7**: 캐싱 및 세션 저장소

### Frontend
- **Tailwind CSS**: 유틸리티 우선 CSS 프레임워크
- **daisyUI**: Tailwind CSS 컴포넌트 라이브러리
- **JavaScript**: 클라이언트 사이드 로직

### Development Tools
- **Black**: 코드 포맷터
- **Ruff**: Python 린터
- **MyPy**: 타입 체커
- **pytest**: 테스트 프레임워크

## 🚀 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/tigers2020/UmaSimCraft.git
cd UmaSimCraft
```

### 2. 가상환경 생성 및 활성화
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 마이그레이션
```bash
python manage.py migrate
```

### 5. 개발 서버 실행
```bash
python manage.py runserver
```

### 6. 브라우저에서 접속
```
http://localhost:8000
```

## 📁 프로젝트 구조

```
UmaSimCraft/
├── project/                 # Django 프로젝트 설정
├── simulation/             # 시뮬레이션 앱
├── restapi/               # REST API 앱
├── websocket/             # WebSocket 앱
├── theme/                 # Tailwind CSS 테마
├── templates/             # 기본 템플릿
├── static/                # 정적 파일
├── media/                 # 미디어 파일
├── logs/                  # 로그 파일
├── docs/                  # 프로젝트 문서
└── planning/              # 개발 계획서
```

## 🔧 개발 환경 설정

### 코드 품질 도구
```bash
# 코드 포맷팅
black .

# 린팅
ruff check .

# 타입 체킹
mypy .

# 테스트 실행
pytest
```

### Tailwind CSS 빌드
```bash
cd theme
npm install
npm run build
```

## 📊 API 문서

- **캐릭터 API**: `GET /api/characters/`
- **서포트 카드 API**: `GET /api/support-cards/`
- **스킬 API**: `GET /api/skills/`

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 📞 연락처

- 프로젝트 링크: [https://github.com/tigers2020/UmaSimCraft](https://github.com/tigers2020/UmaSimCraft)

---

**UmaSimCraft** - 우마무스메 육성 시뮬레이터 🏇 