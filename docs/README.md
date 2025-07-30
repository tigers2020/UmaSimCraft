# UmaSimCraft 프로젝트 문서

이 디렉토리는 UmaSimCraft 프로젝트의 모든 기술 문서와 가이드를 포함합니다.

## 📚 문서 목록

### 1. [프로젝트 개요](./01-프로젝트-개요.md)
- 프로젝트 소개 및 목적
- 기술 스택 및 아키텍처
- 개발 로드맵
- 성능 목표

### 2. [기술 설계서](./02-기술-설계서.md)
- 시스템 아키텍처
- 데이터 모델 설계
- API 설계
- 시뮬레이션 엔진 설계
- 프론트엔드 설계
- 보안 및 성능 최적화

### 3. [개발 진행 계획서](./03-개발-진행-계획서.md)
- 프로젝트 일정 및 마일스톤
- 상세 개발 일정 (12주)
- 리소스 할당
- 품질 관리
- 리스크 관리

### 4. [데이터 설계서](./04-데이터-설계서.md)
- 데이터 소스 및 API
- 데이터베이스 스키마
- 데이터 로딩 전략
- 캐싱 전략
- 백업 및 복구

### 5. [API 설계서](./05-API-설계서.md)
- REST API 엔드포인트
- WebSocket API
- 인증 및 보안
- 에러 처리
- 성능 최적화

### 6. [프론트엔드 설계서](./06-프론트엔드-설계서.md)
- 기술 스택 (Django + Tailwind CSS)
- 컴포넌트 설계
- JavaScript 모듈
- PWA 기능
- 성능 최적화

### 7. [배포 및 운영 가이드](./07-배포-운영-가이드.md)
- Docker 배포
- Nginx 설정
- 모니터링 및 로깅
- 백업 및 복구
- 보안 설정
- 장애 대응

## 🚀 빠른 시작

### 개발 환경 설정
```bash
# 1. 프로젝트 클론
git clone https://github.com/tigers2020/UmaSimCraft.git
cd UmaSimCraft

# 2. 환경 변수 설정
cp .env.example .env
# .env 파일 편집

# 3. Docker 컨테이너 실행
docker-compose up -d

# 4. 데이터베이스 마이그레이션
docker-compose exec web python manage.py migrate

# 5. 정적 파일 수집
docker-compose exec web python manage.py collectstatic

# 6. Tailwind CSS 빌드
docker-compose exec web python manage.py tailwind build
```

### 개발 서버 실행
```bash
# 로컬 개발 서버
python manage.py runserver

# Tailwind CSS 개발 서버
python manage.py tailwind start
```

## 📋 개발 체크리스트

### Phase 1: 기본 인프라 (1-4주)
- [ ] Django 5.2.4 프로젝트 설정
- [ ] MariaDB + Redis 환경 구성
- [ ] Tailwind CSS + daisyUI 설정
- [ ] 기본 앱 구조 생성
- [ ] 데이터 모델 설계
- [ ] API 엔드포인트 구현

### Phase 2: 핵심 기능 (5-8주)
- [ ] 시뮬레이션 엔진 구현
- [ ] WebSocket 실시간 통신
- [ ] 프론트엔드 UI 구현
- [ ] PWA 기능 구현
- [ ] 통합 테스트

### Phase 3: 확장 기능 (9-12주)
- [ ] 고급 기능 구현
- [ ] 모니터링 시스템
- [ ] 성능 최적화
- [ ] 보안 강화
- [ ] 문서화 완성

## 🔧 기술 스택

### 백엔드
- **Python 3.13**: 최신 기능 활용
- **Django 5.2.4 LTS**: 2028년까지 지원
- **Django REST Framework**: API 개발
- **Django Channels 4**: WebSocket 실시간 통신
- **Uvicorn 0.30**: HTTP/2 + WebSocket 서버

### 프론트엔드
- **Django Templates**: 서버 사이드 렌더링
- **Tailwind CSS v3**: Utility-first CSS
- **daisyUI v5**: 300+ 컴포넌트 (MIT 라이선스)
- **Alpine.js**: 경량 반응형 프레임워크
- **Chart.js**: 데이터 시각화

### 데이터베이스 & 캐시
- **MariaDB 11**: master.mdb Loader SQL 호환
- **Redis 7**: Channels 레이어, 객체 캐싱
- **SQLite**: 로컬 캐시 (선택사항)

### 인프라
- **Docker Compose**: 개발/배포 환경 통일
- **Nginx**: 리버스 프록시, 정적 파일 서빙
- **Prometheus + Grafana**: 모니터링
- **Sentry**: 에러 추적

## 📊 성능 목표

| 지표 | 목표값 | 측정 방법 |
|------|--------|-----------|
| API 응답 시간 | p95 < 300ms | Prometheus |
| 시뮬레이션 성능 | 1회당 < 1초 | 내부 측정 |
| 부하 테스트 | 1k RPS | k6 |
| CSS 번들 크기 | < 40KB | PurgeCSS |
| Docker 이미지 | < 120MB | multi-stage build |

## 🔒 보안 고려사항

### 데이터 보안
- master.mdb·이미지는 Cygames 소유
- 배포가 아닌 개인 학습 목적 사용만 허용
- GameTora 동의서: 비상업 목적만 허가

### 기술적 보안
- HTTPS 강제 적용
- 보안 헤더 설정
- Rate Limiting 적용
- SQL Injection 방지 (ORM 사용)
- XSS 방지 (입력 데이터 검증)

## 📈 모니터링

### 주요 지표
- **응답 시간**: API 응답 시간 모니터링
- **에러율**: 4xx, 5xx 에러 비율
- **사용량**: 동시 사용자 수, 요청 수
- **리소스**: CPU, 메모리, 디스크 사용량

### 알림 설정
- 서비스 장애 시 Slack 알림
- 에러율 임계값 초과 시 알림
- 리소스 사용량 임계값 초과 시 알림

## 🤝 기여 가이드

### 코드 스타일
- **Python**: Black, Ruff, isort 적용
- **JavaScript**: ESLint, Prettier 적용
- **CSS**: Tailwind CSS 클래스 순서 준수

### 커밋 메시지
```
feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 수정
style: 코드 스타일 변경
refactor: 코드 리팩토링
test: 테스트 추가/수정
chore: 빌드 프로세스 또는 보조 도구 변경
```

### PR 프로세스
1. 기능 브랜치 생성 (`feature/기능명`)
2. 개발 및 테스트
3. PR 생성 및 리뷰 요청
4. 코드 리뷰 및 승인
5. main 브랜치 머지

## 📞 연락처

- **프로젝트 매니저**: [이메일]
- **기술 문의**: [이메일]
- **버그 리포트**: GitHub Issues
- **기능 요청**: GitHub Discussions

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](../LICENSE) 파일을 참조하세요.

---

**문서 버전**: v1.0  
**최종 업데이트**: 2025-01-27  
**작성자**: UmaSimCraft 개발팀 