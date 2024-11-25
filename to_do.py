
def add_todo(todo_name): #할일추가
    pass #리스트에 추가하기

def view_todo(): #(단순히) 할일목록보기
    pass

def complete_todo(todo_number): # 완료한 할일
    pass

def del_todo(todo_number): #삭제할 할일
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
            todo_name = input("추가할 할 일을 입력하세요 : ") # : 공부하기 입력
            add_todo(todo_name) 
        elif choice =='2':
            view_todo() #할일 목록보기
        elif choice =='3':
            todo_number =int(input("완료한 할 일을 선택해주세요 : "))
            complete_todo(todo_number)
        elif choice =='4':
            todo_number =int(input("삭제할 할 일을 선택해주세요 : "))
            del_todo(todo_number)
        elif choice =='5':
            print ("시스템을 종료합니다. ")
            break
        else :
            print("다시 입력해 주세요. (보기 : 1,2,3,4,5)")
main()
