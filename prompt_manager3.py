import json

def save_prompts():
    with open("prompts.json", "w", encoding="utf-8") as file:
        json.dump(prompts, file, ensure_ascii=False, indent=4)

def export_to_markdown():
    print()
    print("[Markdown 송출]")

    exported_categories = set()

    for prompt in prompts:
        filename = prompt["category"] + ".md"
        mode = "w" if prompt["category"] not in exported_categories else "a"

        with open(filename, mode, encoding="utf-8") as file:
            file.write(f"# {prompt['title']}\n\n")
            file.write(f"{prompt['content']}\n\n")
        exported_categories.add(prompt["category"])

    print("Markdown 송출이 완료되었습니다.")

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
        "favorite": False,
        "usage_count": 0
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
        "favorite": False,
        "usage_count": 0
    },
    {
        "title": "AI를 활용한 4컷 멀티모달 콘텐츠 제작",
        "category": "영상",
        "content": """생성형 AI를 활용하여 하나의 완성된 4컷 멀티모달 콘텐츠를 제작해 주세요.

[작업 순서]

1. 콘텐츠의 목적, 대상, 분위기, 핵심 메시지를 정리하세요.

2. 전체 제작 과정을 다음 순서로 설계하세요.
   - 콘텐츠 기획
   - 4컷 스토리 구성
   - 프롬프트 설계
   - 이미지 생성
   - 영상 생성
   - 음성 및 배경음악
   - 최종 편집

3. 4개의 장면을 하나의 자연스러운 이야기로 연결하세요.

4. 각 장면마다 다음 내용을 작성하세요.
   - 장면 번호
   - 장면의 목표 메시지
   - 화면 구성
   - 인물과 배경
   - 분위기와 조명
   - 내레이션 또는 화면 카피
   - 사용할 AI 도구

5. 이미지와 영상 생성 과정에서는
   캐릭터, 배경, 화풍 등의 일관성을 유지하도록 프롬프트를 작성하세요.

6. AI 도구마다 결과가 다를 수 있으므로
   사용하는 도구의 특성에 맞게 프롬프트를 조정하세요.

7. 생성 결과가 의도와 다르면 문제를 확인하고
   프롬프트를 수정하여 결과를 개선하세요.

8. 여러 AI 도구를 사용할 경우
   이미지 생성, 영상 생성, 음성·음악, 편집 등 각 도구의 역할을 구분하세요.

9. 마지막 4번째 장면에서는
   전체 콘텐츠의 핵심 메시지가 명확하게 전달되도록 구성하세요.

10. 최종적으로 4개의 장면이 하나의 완성된 영상으로
    자연스럽게 연결되도록 확인하세요.

[제작 정보]
콘텐츠 목적:
대상:
분위기:
핵심 메시지:
사용할 AI 도구:
영상 길이:""",
        "favorite": False,
        "usage_count": 0
    },
    {
        "title": "반복 업무를 위한 노코드 자동화 워크플로우 설계",
        "category": "업무",
        "content": """반복적으로 수행하는 업무를 분석하여 노코드 자동화 워크플로우를 설계해 주세요.

[작업 순서]

1. 먼저 자동화할 반복 업무를 하나 정의하세요.
 - 어떤 업무를 반복하고 있는지
 - 현재 어떤 과정으로 처리하는지
 - 자동화하면 어떤 부분을 줄일 수 있는지

2. 자동화에 사용할 도구를 선정하고 선정 이유를 설명하세요.
 필요하면 여러 도구를 비교하여 업무에 적합한 도구를 선택하세요.

3. 전체 워크플로우를 다음 구조로 설계하세요.
 - Trigger : 자동화를 시작하는 조건
 - Filter : 조건 확인 및 분기
 - Action : 조건에 따른 실제 처리

4. 여러 조건으로 업무를 분류해야 한다면
 Router 또는 Filter를 활용하여 각각의 처리 경로를 설계하세요.

5. 필요한 경우 AI를 워크플로우에 연결하여
 분류, 분석, 요약 등의 작업을 자동화하세요.

6. 자동화된 처리 결과를 저장 공간에
 기록하거나 보관하는 방법을 설계하세요.

7. 불필요한 데이터나 메일은 조건에 따라
 별도의 보관 또는 삭제 과정이 이루어지도록 설계하세요.

8. 각 단계에서 사용하는 서비스와 역할을 명확하게 구분하세요.
 예:
 - 이메일 수신
 - 조건 분기
 - AI 분석 및 요약
 - 결과 저장
 - 최종 정리

9. 테스트 과정에서 예상과 다른 결과가 발생하면
 어느 단계에서 문제가 발생했는지 확인하고
 조건이나 워크플로우를 수정하세요.

10. 최종적으로 전체 자동화 과정이 처음부터 끝까지
 자연스럽게 연결되는지 확인하고,
 향후 조건을 추가하거나 확장할 수 있도록 구성하세요.

[자동화 정보]
자동화할 반복 업무:
사용할 서비스:
자동화 목적:
분류 또는 조건:
AI 활용 여부:
결과 저장 방법:
최종 처리 방법:""",
        "favorite": False,
        "usage_count": 0
    },
    {
        "title": "영상 제작",
        "category": "영상",
        "content": "영상 제작을 위한 장면 구성과 프롬프트를 만들어 주세요.",
        "favorite": False,
        "usage_count": 0
    }
]

def show_menu():

    print("=================================")
    print("      프롬프트 관리 프로그램")
    print("=================================")
    print()

    print("1. 프롬프트 등록")
    print("2. 프롬프트 목록")
    print("3. 프롬프트 검색")
    print("4. 카테고리 조회")
    print("5. 즐겨찾기 등록/해제")
    print("6. 즐겨찾기 목록")
    print("7. 상세하게 보기")
    print("8. Markdown 송출")
    print("9. 프롬프트 수정")
    print("10.프롬프트 삭제")
    print("11.사용횟수 목록")
    print("0. 프로그램 종료")

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
        origin/main

    if not title:
        print("제목을 입력하세요.")
        return

    for prompt in prompts:
        if prompt["title"].lower() == title.lower():
            print("이미 등록된 제목입니다.")
            return

    category = input("카테고리를 입력하세요 : ").strip()
    content = input("내용을 입력하세요 : ").strip()
    
    if not category:
        print("카테고리를 입력하세요.")
        return

    if not content:
        print("내용을 입력하세요.")
        return
    
    new_prompt = {
        "title": title,
        "category": category,
        "content": content,
        "favorite": False,
         "usage_count": 0
    }

    prompts.append(new_prompt)

    print("등록되었습니다.")

def show_list():
    print()
    print("[프롬프트 목록]")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f"{i}. {prompt["title"]} - {prompt["category"]}{star}")

def search_prompt():
    print()
    print("[프롬프트 검색]")

    keyword = input("검색어를 입력하세요 : ").strip().lower()

    if not keyword:
        print("검색어를 입력하세요.")
        return

    found = False
    result_number = 1

    for prompt in prompts:
        if (keyword in prompt["title"].lower()
                or keyword in prompt["content"].lower()
                or keyword in prompt["category"].lower()):

            star = " ⭐" if prompt["favorite"] else ""
            print(f"{result_number}. {prompt['title']} - {prompt['category']}{star}")

            found = True
            result_number += 1
    if not found:
        print("검색 결과가 없습니다.")

def show_by_category():
    print()
    print("[카테고리 조회]")

    category = input("카테고리를 입력하세요 : ").strip()

    if not category:
        print("카테고리를 입력하세요.")
        return
    
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
        print("즐겨찾기에 등록된 프롬프트가 없습니다.")
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
        print("즐겨찾기가 해제되었습니다.")

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

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, prompt in enumerate(prompts, start=1):
        print(f"{i}. {prompt['title']} - {prompt['category']}")

    number = input("상세보기 할 프롬프트 번호를 입력하세요 : ").strip()

    if not number.isdigit():
        print("번호를 입력하세요.")
        return

    index = int(number) - 1

    if index < 0 or index >= len(prompts):
        print("잘못된 번호입니다.")
        return

    prompt = prompts[index]

    prompt.setdefault("usage_count", 0)
    prompt["usage_count"] += 1

    print("제목 :", prompt["title"])
    print("카테고리 :", prompt["category"])
    print("내용 :", prompt["content"])
    print("즐겨찾기 :", "⭐ 등록됨" if prompt["favorite"] else "미등록")
    print("사용 횟수 :", prompt["usage_count"])
    print("상세보기가 완료되었습니다.")

def show_usage_top():
    print()
    print("[사용횟수 목록]")

    sorted_prompts = sorted(
        prompts,
        key=lambda prompt: prompt.get("usage_count", 0),
        reverse=True
    )

    for index, prompt in enumerate(sorted_prompts, 1):
        print(
            f"{index}. {prompt['title']} - "
            f"{prompt['category']} - "
            f"사용 횟수: {prompt.get('usage_count', 0)}"
        )

def update_prompt():
    print()
    print("[프롬프트 수정]")

    title = input("수정할 제목을 입력하세요 : ").strip().lower()

    if not title:
        print("수정할 제목을 입력하세요.")
        return

    for prompt in prompts:
        if prompt["title"].lower() == title:
            new_title = input(
                f"새 제목 [{prompt['title']}] : "
            ).strip()

            new_category = input(
                f"새 카테고리 [{prompt['category']}] : "
            ).strip()

            new_content = input(
                f"새 내용 [{prompt['content']}] : "
            ).strip()

            if new_title:
                for other_prompt in prompts:
                    if (
                        other_prompt is not prompt
                        and other_prompt["title"].lower() == new_title.lower()
                    ):
                        print("이미 등록된 제목입니다.")
                        return

                prompt["title"] = new_title

            if new_category:
                prompt["category"] = new_category

            if new_content:
                prompt["content"] = new_content

            print("프롬프트가 수정되었습니다.")
            return

    print("해당 프롬프트를 찾을 수 없습니다.")

def delete_prompt():
    print()
    print("[프롬프트 삭제]")

    title = input("삭제할 제목을 입력하세요 : ").strip().lower()

    if not title:
        print("삭제할 제목을 입력하세요.")
        return

    for prompt in prompts:
        if prompt["title"].lower() == title:
            prompts.remove(prompt)
            print("프롬프트가 삭제되었습니다.")
            return

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

        elif choice == "9":
            update_prompt()

        elif choice == "10":
            delete_prompt()

        elif choice == "11":
            show_usage_top()

        elif choice == "0":
            save_prompts()
            print("프로그램을 종료합니다.") 
            break 

        else: print("잘못된 메뉴입니다. 다시 선택하세요.") 

        print()

if __name__ == "__main__": 
    main()
    