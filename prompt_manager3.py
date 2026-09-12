prompts = [
    {
        "title": "Python 학습",
        "category": "개발",
        "content": "Python을 쉽게 설명해 주세요.",
        "favorite": False
    },
    {
        "title": "회의록 요약",
        "category": "업무",
        "content": "회의 내용을 핵심 내용 중심으로 요약해 주세요.",
        "favorite": False
    },
    {
        "title": "영상 제작",
        "category": "영상",
        "content": "영상 제작을 위한 장면 구성과 프롬프트를 만들어 주세요.",
        "favorite": False
    }
]

def show_menu():

    print("=================================")
    print("      프롬프트 관리 프로그램")
    print("=================================")
    print()

    print("1. 프롬프트 등록")
    print("2. 프롬프트 목록 보기")
    print("3. 프롬프트 검색")
    print("4. 카테고리별 조회")
    print("5. 즐겨찾기 등록/해제")
    print("6. 즐겨찾기 목록")
    print("7. 상세 보기")
    print("0. 종료")

def add_prompt():
    print()
    print("[프롬프트 등록]")

    title = input("제목을 입력하세요 : ")
    category = input("카테고리를 입력하세요 : ")
    content = input("내용을 입력하세요 : ")

    new_prompt = {
        "title": title,
        "category": category,
        "content": content,
        "favorite": False
    }

    prompts.append(new_prompt)

    print("등록되었습니다.")

def show_list():
    print()
    print("[프롬프트 목록 보기]")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f"{i}. {prompt["title"]} - {prompt["category"]}{star}")

def search_prompt():
    print()
    print("[프롬프트 검색]")

    keyword = input("검색어를 입력하세요 : ").lower()

    found = False

    for prompt in prompts:
        if (keyword in prompt["title"].lower()
                or keyword in prompt["content"].lower()
                or keyword in prompt["category"].lower()):
            print(prompt["title"], "-", prompt["category"])

    if not found:
        print("검색 결과가 없습니다.")

def show_by_category():
    print()
    print("[카테고리별 조회]")

    category = input("카테고리를 입력하세요 : ")

    found = False

    for prompt in prompts:
        if prompt["category"] == category:
            print(prompt["title"], "-", prompt["category"])   
            found = True

    if not found:
        print("해당 카테고리의 프롬프트가 없습니다.")

def toggle_favorite():  
    print() 
    print("[즐겨찾기 등록/해제]")        
        
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    
    for i, prompt in enumerate(prompts, start=1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f"{i}. {prompt['title']} - {prompt['category']}{star}")

    number = input("즐겨찾기에 등록할 프롬프트 번호를 입력하세요 : ")

    if not number.isdigit():
        print("번호를 입력하세요.")
        return

    index = int(number) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[index]
    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print("즐겨찾기에 등록되었습니다. ⭐")
    else:
        print("즐겨찾기에서 해제되었습니다.")

def show_favorites():
    print()
    print("[즐겨찾기 목록]")

    found = False

    for prompt in prompts:
        if prompt["favorite"]:
            print(prompt["title"], "-", prompt["category"])
            found = True

    if not found:
        print("즐겨찾기에 등록된 프롬프트가 없습니다.")

def show_detail():
    print()
    print("[상세보기]")

    title = input("제목을 입력하세요 : ").lower()

    for prompt in prompts:
        if prompt["title"].lower() == title:
            print("제목 :", prompt["title"])
            print("카테고리 :", prompt["category"])
            print("내용 :", prompt["content"])
            print("즐겨찾기 :", prompt["favorite"])
            break
    else:
        print("해당 프롬프트를 찾을 수 없습니다.")

def main(): 
    while True: 
        show_menu() 

        choice = input("메뉴를 선택하세요 : ")

        if choice == "1": 
            add_prompt() 

        elif choice == "2": 
            show_list() 

        elif choice == "3": 
            search_prompt() 

        elif choice == "4": 
            show_by_category() 

        elif choice == "5": 
            toggle_favorite() 

        elif choice == "6": 
            show_favorites() 

        elif choice == "7": 
            show_detail() 

        elif choice == "0": 
            print("프로그램을 종료합니다.") 
            break 

        else: print("잘못된 메뉴입니다. 다시 선택하세요.") 

        print()

if __name__ == "__main__": 
    main()
    