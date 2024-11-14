![image](https://github.com/user-attachments/assets/b6000034-9ba6-49aa-996c-43498669789a)# TestRail Old runs&results cleanup
TestRail API를 이용해서 만든 오래된 Runs & Results를 클린업하여 testrail 내부의 속도 케어 목표로 제작된 코드입니다.



사용방법 및 설명

![image](https://github.com/user-attachments/assets/c5694586-40f4-4d97-a211-118438c7f9b3)
먼저 project_id, username, password 내부를 추가하셔야합니다.

예시
project_id : 149
username : leeyongg@gmarket.com
password : dasd214sa... (apikey)
키추가
api 키는
1) 테스트레일 로그인 후 상단 "My Settings"에서 구성할 수 있으며 
2) 키를 추가 (Add key) 선택하고 
3) 적당한 키명을 입력 및 Generate Key 선택한 후 
4) 생성된 키를 복사한다. (이후 키를 조회할 수 없으니 꼭 복사할 것)
5) API 를 사용하려면 테스트 레일의 권한도 필요함

![image](https://github.com/user-attachments/assets/4f94f91b-c646-4b84-adfb-10479d1e0087)
그리고 keword 를 지정하여 지우고싶은 키워드를 넣고 실행하시면 됩니다.
실행되는 부분은 불러오는 목록과 삭제되는 목록을 보여줍니다.

아래는 결과입니다.

결과.
가져온 테스트 런 목록:
dWeb - Automated Test    (2024-11-13 10:39:24 / leeyongg)
dWeb - Automated Test    (2024-11-13 10:37:50 / leeyongg)
.
.
dWeb - Automated Test    (2024-09-04 14:21:19 / leeyongg)
Deleting Test Run ID: 42255 - dWeb - Automated Test    (2024-09-30 17:56:37 / leeyongg)
Test Run 42255이(가) 성공적으로 삭제되었습니다.
Deleting Test Run ID: 42254 - dWeb - Automated Test    (2024-09-30 17:56:07 / leeyongg)
Test Run 42254이(가) 성공적으로 삭제되었습니다.
.
.
총 216개의 테스트 런이 삭제되었습니다.





