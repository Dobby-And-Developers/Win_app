# Win_app
DSM-Owl application

# Application

# OWL Function
## 개요
### 메인화면
### * 회원가입
    < 받아올 정보 >
    * 이름
    * 이메일 - 인증번호 구현
    * 아이디 - 중복체크 구현
    * 비밀번호 - 영문숫자특문 상관없이, *처리

### * 로그인
    < 받아올 정보 >
    * 아이디
    * 비밀번호 - *처리

### * 시간표
    < 구상 >
    * 로그인을 한 정보를 통하여 사용자의 반을 찾는다
    * 로그인후 메인화면에 시간표를 버튼형식으로 표시한다.
    * 시간표가 적힌 버튼을 클릭하면 내부 내용을 팝업으로 표시하여준다.
    
### * 온라인 판별
    * 선생님용을 따로 만들어 온라인 전환버튼을 배치한다.
    * 온라인 버튼을 누르면 학생들이 확인할 수 있도록 교무실 배치표에 온라인 표시를 띄운다.
    * 각 선생님들의 자리도 버튼으로 하여 누르면 선생님의 출장 일정이나 업무를 간략히 팝업으로 출력한다.

### * 급식표 - 추가 가능하다면 
    * 그날의 급식은 프로그램을 실행함과 동시에 팝업으로 띄우고 메인화면에서 급식표 창으로 넘어가면 주간, 월간 급식을 차례대로 볼 수 있게 해준다.    


# OWL - 진행상황

## 메인
### 버튼
    * pushButton1 : 로그인
    * pushButton2 : 회원가입

### 입력창
    * NONE

## 회원가입
### 버튼
    * pushButton1 : 중복확인
    * pushButton2 : 회원가입
    * pushButton3 : 메일인증
    * pushButton4 : 확인

### 입력창
    * lineEdit1 : 이름
    * lineEdit2 : 이메일
    * lineEdit3 : 인증번호
    * lineEdit4 : 아이디
    * lineEdit5 : 비밀번호

## 로그인 
### 버튼 
    * pushButton1 : 로그인

### 입력창
    * lineEdit1 : 아이디
    * lineEdit2 : 비밀번호


# 기술 스택
* Python
* PyQT5
* MySQL
