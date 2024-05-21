[ Model ERD ]
https://lucid.app/documents/view/9b98b991-e4cd-4b4f-8b30-81895abb6004 

![](image-1.png)

# final pjt

<!-- [API docs](https://www.notion.so/db65eca14411457e81023b037b8b2965?pvs=21) -->

# 1. 메인페이지

- 메인페이지 [HomeView.vue]
- 내브바
    - 금리비교 - [SavingView.vue]로 이동
    - 환율계산기 - [CalculatorView.vue]로 이동
    - 은행지도 - [BankSearchView.vue]로 이동
    - 커뮤니티 - [ArticleListView.vue] 로 이동
    - 회원가입 - [SignUpView.vue] 로 이동
    - 로그인 - [LogInView.vue] 로 이동
    - 비밀번호 찾기 - [PasswordFindView.vue] 로 이동
    - 로그아웃 - [로그아웃 버튼] → 로그아웃
    - 환영메세지 - 상세 페이지 [ProfileView.vue] 로 이동
- 캐루젤
    - 금융상품 추천! 어쩌구~ → 자세히 보기 버튼 : 추천페이지 [ProductRecommendView.vue] 로 이동
    - 근처은행검색 → [BankSearchView.vue]로 이동
- 카드 버튼
    - 환율 계산기 [Exchange.vue]
    - 은행 찾기 [BankSearch.vue]
    - 커뮤니티 [ArticleList.vue]
    - 금융상품 추천 페이지 [ProductRecommendView.vue]

# 2. 회원 커스터마이징

- 회원가입 [SignUpView.vue]
    - 회원 정보 model
        - username
        - password
        - name
        - email
        - profile_img
        - financial_products ( 가입상품 목록 )
        - age
        - money ( 자산 )
        - salary ( 연봉 )
        - is_superuser
- 로그인 [LogInView.vue]
- 비밀번호 찾기 [PasswordFindView.vue]

# 3. 예적금 금리 비교

- 금융상품통합비교공시 API → 데이터 가져와서 DB에 저장 ( 이미 존재하는 데이터 저장 x - filter 기능)
1. 예적금 금리 [SavingView.vue] (가입기간, 은행 선택 → 해당 상품 목록 반환)
    1. 가입기간, 은행 선택 창
    2. 상품 목록 리스트 컴포넌트 [SavingList.vue]
    3. 상품 상세페이지 [SavingDetailView.vue]
        1. 가입하기 버튼 - 클릭시 해당 회원의 가입한 상품목록 ID에 상품 추가
        2. 로그인한 사용자만 해당 버튼 출력

# 4. 환율 계산기

- 환율 계산기 [ExchangeView.vue]
- 한국수출입은행 환율정보 API
- 국가선택 → 환율 정보 반환

# 5. 근처 은행 검색

- 카카오맵 API
- 은행 검색 [BankMapView.vue]
    1. 은행 검색 창
    2. 검색한 은행 지도

# 6. 커뮤니티

- 게시글 CRUD, 댓글 CRUD 구현
- 게시글 좋아요 기능 (도움돼요!)
1. 게시글 페이지 [ArticleView.vue]
    1. 게시글 작성 버튼
    2. 게시글 목록 컴포넌트 [ArticleList.vue]
        1. 게시글 리스트 아이템 컴포넌트 [ArticleListItem.vue] ( 클릭하면 상세페이지로 이동 )
2. 게시글 상세페이지 [ArticleDetailView.vue]
    1. 게시글 상세 정보
    2. 다른 사람 게시글일 경우 - 도움돼요 버튼, 도움돼요 수
    3. 본인 게시글 - 삭제, 수정 버튼
    4. 댓글 리스트 컴포넌트 [ArticleComment.vue]
        1. 댓글 상세정보
        2. 본인 댓글이면 삭제, 수정 → 수정 누르면 수정 폼 제시 (수정은 나중에..)
        3. 댓글 CRUD [ArticleCommentUpdate.vue]
3. 게시글 작성 페이지 [ArticleCreateView.vue]
4. 게시글 수정 페이지 [ArticleUpdateView.vue]

# 7. 프로필 페이지

- 회원 상세 정보 [ProfileView.vue]
    - 회원 정보 model 기반
    - 프로필 수정 버튼 - [ProfileUpdateView.vue]로 이동
- 수정, 회원 탈퇴 기능 [ProfileUpdateView.vue]
    - 회원 정보 model 기반
    - 회원 탈퇴 버튼 → 회원 탈퇴
- 작성한 게시글 컴포넌트 [ProfileArticle.vue]
- 작성한 댓글 컴포넌트 [ProfileComment.vue]
- 좋아요한 게시글 컴포넌트 [ProfileLike.vue]

# 8. 금융 상품 추천 알고리즘

- 더미데이터 생성 [ProductRecommendView.vue]
- 금융상품 [ProductDetailView.vue]

# 9. README

- 팀원 정보 및 업무 분담 내역
    - 0516
        - 수인 : 모델 구성, ERD 작성, vue 컴포넌트 생성,
        - 아영 : 컴포넌트 구성, 모델 구성, 게시판 crud 구현
    - 0517
        - 수인 : 환율 api 데이터 조회/ db저장
        - 아영 : articles model, serializer 설계
    - 0518
        - 수인 : 지도 완성
        - 아영 : article crud 구현
    - 0519
        - 수인 : 게시글 댓글 crud, article 수정 기능
        - 아영 :  profile페이지 구현, Authentication 기능 구현
    - 0520
        - 수인 : 게시글 좋아요/좋아요취소, 프로필 페이지에 좋아요한 목록 출력, dummy data 생성, 환율계산기 완성
        - 아영 : 예적금 정보 api 데이터 조회, 예적금 리스트 출력, 예적금 상세페이지 구현
    - 0521
        - 수인 : 예/적금 상품 필터링, AI Chatbot 구현
        - 아영 : 예/적금 상품의 관심 상품 등록/취소, 나의 관심상품 목록 구현, 추천 알고리즘 구현
        
- 설계 내용 및 실제 구현 정도
- 데이터베이스 모델링 (ERD)
- 금융 상품 추천 알고리즘에 대한 기술적 설명
- 서비스 대표 기능들에 대한 설명
- 기타 (느낀 점, 후기)