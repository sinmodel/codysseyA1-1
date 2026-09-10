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

while True:

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
    print("8. 종료")

    choice = input("메뉴를 선택하세요 : ")

    if choice == "1":
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

    elif choice == "2":
        print()
        print("[프롬프트 목록 보기]")

        for prompt in prompts:
            print(prompt["title"], "-", prompt["category"])

    elif choice == "3":
        print()
        print("[프롬프트 검색]")

        keyword = input("검색어를 입력하세요 : ").lower()

        for prompt in prompts:
            if (keyword in prompt["title"].lower()
                    or keyword in prompt["content"].lower()
                    or keyword in prompt["category"].lower()):
                print(prompt["title"], "-", prompt["category"])

    elif choice == "4":
        print()
        print("[카테고리별 조회]")

        category = input("카테고리를 입력하세요 : ")

        for prompt in prompts:
            if prompt["category"] == category:
                print(prompt["title"], "-", prompt["category"])   

    elif choice == "5":  
        print() 
        print("[즐겨찾기 등록/해제]")        
        
        title = input("제목을 입력하세요 : ").lower()

        for prompt in prompts:
            if prompt["title"].lower() == title:
                if prompt["favorite"] == False:
                    prompt["favorite"] = True
                    print("즐겨찾기에 등록되었습니다.")
                else:
                    prompt["favorite"] = False
                    print("즐겨찾기에서 해제되었습니다.")
                break
        else:
            print("해당 프롬프트를 찾을 수 없습니다.")

    elif choice == "6":
        print()
        print("[즐겨찾기 목록]")

        for prompt in prompts:
            if prompt["favorite"]:
                print(prompt["title"], "-", prompt["category"])

    elif choice == "7":
        print()
        print("[상세보기]")

        title = input("제목을 입력하세요 : ").lower()

        for prompt in prompts:
            if prompt["title"].lower() == title:
                print("제목 :", prompt["title"])
                print("카테고리 :", prompt["category"])
                print("내용 :", prompt["content"])
                print("즐겨찾기 :", prompt["favorite"])

    elif choice == "8":
        print("프로그램을 종료합니다.")
        break
    