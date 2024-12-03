import json
import os #파이썬이용해 시스템 내부에 접근가능

TASK_FILE = 'tasks.json' #여따가 할일 저장할거셈ㅋ
 
#파일열기
def load_task(): #path=경로
    if os.path.exists('tasks.json'): #파일명 가진 파일이 있나?
        with open(TASK_FILE,'r',encoding='utf-8') as file: #있으면 읽어.
            return json.load(file) #json.load() 함수이면서 메소드(---.---())= 클래스 안에 구현된 함수
    return [] #파일없다? 그럼머..아무것도없다 알겐니? =>빈리스트  

#파일에 저장
def save_task(tasks):#add_task 를 통해 전달받은 리스트를 파일에 저장하는 기능
    with open(TASK_FILE, "w",encoding='utf-8')as file :# file => open(task_FILE, "w",encoding='utf-8')
        json.dump(tasks, file, indent=4 , ensure_ascii=False) #들여쓰기 =indent

#할일추가
def add_task(task_name): 
    #리스트에 추가하기
    tasks = load_task() #파일 있다면 가져와!
    task = {'name':task_name, "completed":False} #add_task 에서 입력받은 할일 이름 파일에 저장되었음 
    tasks.append(task) #데이터 리스트 집어넣기 ! []
    save_task(tasks)


def view_task(): #(단순히) 할일목록보기 ,merge 진행
    tasks = load_task() #파일이 잇는 경우 안에 내용물이 tasks에 들어가고 없으면 빈 리스트가 들어감
    if not tasks: 
        print ("현재 등록된 할일이 없습니다.")
    else :
        print ("---- 할일 목록 ----")
        for i,task in enumerate(tasks,start=1): #enumerate() : 숫자와 같이 출력됨. (변수,시작하는숫자)i에 숫자 1식증가
            # i =1, task = {"name": "파이썬공부하기","completed": false}
                status = "완료" if task['completed'] else "미완료" #키값넣으면 자동적으로 반환(출력 또는 돌려주기) 값을 준다
                                #if 뒤가 맞으면 앞에 , 아니면 else 뒤에
                print(f"{i}. {task['name']} : {status}") # 1. 파이썬 공부하기 : 미완료
        print("-------------------")

def complete_task(task_number): # 완료한 할일
    tasks = load_task() #tasks = [{"name":"파이썬 공부하기", "completed":false}, ]
    if 1 <= task_number <= len(tasks) : #3번 입력한 경우 번호 잘못입력했으니 다시입력해 !
        tasks[task_number-1]["completed"] = True # tasks [0]["completed"] =>{"name":"파이썬 공부하기", "completed":false} =>false
        save_task(tasks)
        print(f"할 일 중 '{tasks[task_number-1]['name']}' 이(가) 완료 처리 되었습니다.")
            
    else :
        print('유효하지 않은 번호입니다. 다시 입력해주세요.')

def delete_task(task_number): #삭제할 할일 
    tasks = load_task() # 목록 불러오기
    if 1 <=task_number <= len(tasks) : # 목록중 고르기
        remove_task = tasks.pop(task_number-1) # pop통해 삭제 및 반환, 삭제된 데이터가 remove_task에 들어감
        save_task(tasks) #리스트에 저장
        print (f"할 일 중 '{remove_task['name']}'이(가) 삭제되었습니다.")
    else :
        print ("유효하지 않은 번호입니다. 다시 입력해주새요.")

def show_menu() : # 메뉴
    print("---- 작업관리 애플리케이션 ----")
    print("1. 할 일 추가")
    print("2. 할 일 목록보기")
    print("3. 할 일 완료")
    print("4. 할 일 삭제")
    print("5. 종료")

def main():
    while True : 
        show_menu()
        choice = input("원하는 작업을 선택해주세요 .1~5 : ")
        if choice =='1':
            task_name = input("추가할 할 일을 입력하세요 : ") # : 공부하기 입력
            add_task(task_name) 
        elif choice =='2':
            view_task() #할일 목록보기
        elif choice =='3':
            task_number =int(input("완료한 할 일을 선택해주세요 : "))
            complete_task(task_number)
        elif choice =='4':
            task_number =int(input("삭제할 할 일을 선택해주세요 : "))
            delete_task(task_number)
        elif choice =='5':
            print ("시스템을 종료합니다. ")
            break
        else :
            print("다시 입력해 주세요. (보기 : 1,2,3,4,5)")
main()
