import requests
import sys
import os
from datetime import datetime
from tqdm import tqdm  # tqdm 라이브러리 추가


class TestRailCleaner:
    def __init__(self):
        # TestRail API URL과 프로젝트 ID
        self.base_url = "http://172.30.2.20/index.php?/api/v2"
        self.project_id = "149"  # 실제 프로젝트 ID로 대체
        self.username = "leeyongg@gmarket.com"  # 사용자 이름 설정
        self.password = "GQwTJFxxjzQfZ122hHtv-36t0b/ffDthkYgZlW.VZ"  # API 키를 비밀번호처럼 사용
        
        # 세션 생성
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)
        
        # 세션 헤더 설정
        self.session.headers.update({
            "Content-Type": "application/json"
        })
        self.screenshot_counter = 0  # 스크린샷 카운터 변수 추가
    
    def get_test_runs(self):
        """특정 프로젝트의 테스트 런 목록을 페이지네이션을 통해 모두 가져옵니다."""
        runs = []
        offset = 0
        limit = 250  # TestRail API의 최대 limit 값
        
        while True:
            url = f"{self.base_url}/get_runs/{self.project_id}&limit={limit}&offset={offset}"
            response = self.session.get(url)
            
            if response.status_code == 200:
                data = response.json()
                runs.extend(data)  # 가져온 데이터를 전체 runs 목록에 추가
                if len(data) < limit:
                    # 가져온 데이터가 limit보다 적으면 마지막 페이지에 도달한 것임
                    break
                offset += limit  # 다음 페이지로 넘어가기 위한 offset 조정
            else:
                print(f"테스트 런 목록을 가져오는 데 실패했습니다. 상태 코드: {response.status_code}")
                print(response.json())
                break
        
        return runs
    
    def delete_test_run(self, run_id):
        """지정된 테스트 런을 삭제합니다."""
        url = f"{self.base_url}/delete_run/{run_id}"
        response = self.session.post(url)
        if response.status_code == 200:
            print(f"Test Run {run_id}이(가) 성공적으로 삭제되었습니다.")
        else:
            print(f"테스트 런 삭제에 실패했습니다. 상태 코드: {response.status_code}")
            print(response.json())
    
    def clean_old_test_runs(self, keyword="2024-10"):
        """지정된 키워드가 포함된 테스트 런을 찾아 삭제합니다."""
        runs = self.get_test_runs()
        deleted_runs = []
        
        # 가져온 테스트 런 목록 출력
        print("가져온 테스트 런 목록:")
        for run in runs:
            print(run['name'])  # 각 테스트 런의 이름 출력
        
        # 키워드가 포함된 테스트 런 삭제
        print("삭제를 시작합니다... (진행 중 표시)")
        for i, run in tqdm(enumerate(runs), total=len(runs), desc="삭제 진행", unit="개"):
            if keyword in run['name']:
                print(f"Deleting Test Run ID: {run['id']} - {run['name']}")
                self.delete_test_run(run['id'])
                deleted_runs.append(run['id'])
        
        if deleted_runs:
            print(f"총 {len(deleted_runs)}개의 테스트 런이 삭제되었습니다.")
        else:
            print("삭제할 테스트 런이 없습니다.")


def save_output_to_file(func):
    """함수를 실행하고 출력 결과를 텍스트 파일에 저장하는 데코레이터."""
    
    def wrapper(*args, **kwargs):
        # 현재 날짜와 시간으로 파일 이름 생성
        timestamp = datetime.now().strftime("%Y.%m.%d_%H:%M")
        file_name = f"old_test_runs_cleanup_{timestamp}.txt"
        
        # 파일 열기
        with open(file_name, "w", encoding="utf-8") as f:
            # 기존 stdout을 파일로 리디렉션
            original_stdout = sys.stdout
            sys.stdout = f
            
            try:
                # 함수 실행
                func(*args, **kwargs)
            finally:
                # 실행 후 다시 원래의 stdout으로 복구
                sys.stdout = original_stdout
        print(f"출력 결과가 {file_name}에 저장되었습니다.")
    
    return wrapper


# 데코레이터 적용
@save_output_to_file
def run_cleaner():
    cleaner = TestRailCleaner()
    cleaner.clean_old_test_runs()


if __name__ == "__main__":
    print("실행 중...")
    run_cleaner()
    print("작업이 완료되었습니다.")
