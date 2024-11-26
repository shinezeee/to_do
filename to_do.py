import json
import os #파이썬이용해 시스템 내부에 접근가능

TASK_FILE = 'tasks.json' #여따가 할일 저장할거셈ㅋ
 
#파일열기
def load_task(): #path=경로
    if os.path.exists('tasks.json'): #파일명 가진 파일이 있나?
        with open(TASK_FILE,'r',encoding=utf-8) as file: #있으면 읽어.
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

    
def view_task(): #(단순히) 할일목록보기
    pass

def complete_task(task_number): # 완료한 할일
    pass

def del_task(task_number): #삭제할 할일
    pass

def show_menu() : # 메뉴
    print("작업관리 애플리케이션")
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
            del_task(task_number)
        elif choice =='5':
            print ("시스템을 종료합니다. ")
            break
        else :
            print("다시 입력해 주세요. (보기 : 1,2,3,4,5)")
main()
