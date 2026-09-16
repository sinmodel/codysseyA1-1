import json

def save_prompts():
    with open("prompts.json", "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)

def export_to_markdown():
    print()
    print("[Markdown 내보내기]")

    exported_categories = set()

    for prompt in prompts:
        filename = prompt["category"] + ".md"
        mode = "w" if prompt["category"] not in exported_categories else "a"

        with open(filename, mode, encoding="utf-8") as file:
            file.write(f"# {prompt['title']}\n\n")
            file.write(f"{prompt['content']}\n\n")
        exported_categories.add(prompt["category"])

    print("Markdown 내보내기가 완료되었습니다.")

def load_prompts():
    try:
        with open("prompts.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

prompts = [
    {
        "title": "Python 학습",
        "category": "개발",
        "content": "Python을 쉽게 설명해 주세요.",
        "favorite": False
    },
    {
        "title": "AI 사용법을 익히기 위한 회의록 요약 작성",
        "category": "업무",
        "content": """회의록 원문을 바탕으로 사용 목적에 맞는 실용적인 요약을 작성해 주세요.

[작업 순서]

1. 먼저 사용자가 원하는 요약 목적과 결과 형식을 파악하세요.
   - 상사 보고용
   - 부서별 업무 분담용
   - 회의록 보관용
   - 기타 사용자가 지정한 형식

2. 회의록을 분석하여 다음 정보를 확인하세요.
   - 결정사항
   - 담당자별 할 일
   - 일정 및 마감일
   - 리스크 및 우려사항
   - 다음 일정
   - 아직 결정되지 않은 사항
   - 확인이 필요한 정보

3. 회의록에 없는 정보나 확인되지 않은 내용은 추측하지 마세요.
   정보가 없으면 "명시되지 않음" 또는 "확인 필요"라고 표시하세요.

4. 특히 숫자, 날짜, 금액, 담당자, 일정 등은 원문에 근거해서 작성하세요.
   사용자의 질문에 잘못된 전제가 포함되어 있으면 그대로 받아들이지 말고
   회의록의 실제 내용을 근거로 바로잡아 주세요.

5. 필요한 경우 먼저 누락되었거나 확인이 필요한 정보를 알려주고,
   사용자의 확인이 끝난 후 최종 요약을 작성하세요.

6. 최종 요약은 필요에 따라 다음 4개 항목으로 구성하세요.
   - 결정사항
   - 할 일
   - 리스크
   - 다음 일정

7. 사용자가 말투, 형식 또는 특정 조건을 변경하면
   변경된 부분만 수정하고 나머지 조건은 유지하세요.

8. 사용자가 새로운 정보를 제공하면 기존 회의록의 내용과 구분하여
   새로운 정보를 반영하세요.

9. 답변은 핵심부터 간단명료하게 작성하고,
   어려운 내용은 쉬운 말로 설명하세요.
   필요하면 표나 목록을 사용하세요.

10. 회의록 원문에 없는 사실, 수치, 날짜, 담당자 또는 확정되지 않은 내용을
    임의로 만들어내지 마세요.

[회의록 원문]
여기에 회의록을 붙여 넣으세요.""",        
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
    print("8. Markdown 내보내기")
    print("0. 종료")

def add_prompt():
    print()
    print("[프롬프트 등록]")

    title = input("제목을 입력하세요 : ").strip()

    if not title:
        print("제목을 입력하세요.")
        return

    for prompt in prompts:
        if prompt["title"].lower() == title.lower():
            print("이미 등록된 제목입니다.")
            return

    category = input("카테고리를 입력하세요 : ").strip()

    if not category:
        print("카테고리를 입력하세요.")
        return

    content = input("내용을 입력하세요 : ").strip()

    if not content:
        print("내용을 입력하세요.")
        return

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

    if not keyword:
        print("검색어를 입력하세요.")
        return

    found = False

    for prompt in prompts:
        if (keyword in prompt["title"].lower()
                or keyword in prompt["content"].lower()
                or keyword in prompt["category"].lower()):
            print(prompt["title"], "-", prompt["category"])
            found = True
            
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
    prompts[:] = load_prompts() or prompts

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

        elif choice == "8":
            export_to_markdown()

        elif choice == "0":
            save_prompts()
            print("프로그램을 종료합니다.") 
            break 

        else: print("잘못된 메뉴입니다. 다시 선택하세요.") 

        print()

if __name__ == "__main__": 
    main()
    