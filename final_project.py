import random

#기본 리스트
word = []
nounWord = []
dictList = ["표준국어대사전"]
dictListOut = []
usedWord = []
nan = ["하"]
hintChance = 3
hintChanceP1 = 3
hintChanceP2 = 3

#파일을 리스트에 담기(컴퓨터 위치에 따라 변경)
f = open("kr_korean.csv", "r", encoding="utf-8")
for contents in f:
    word.append(contents.strip("\n").replace(" ","").replace("^","").replace("-","").split(","))

#명사 단어만 추출하기
a = 0
while a < len(word):
    if word[a][1] == "명사":
        nounWord.append(word[a][0])
        a = a + 1
    else:
        a = a + 1
f.close()

while True:
    print("****************************************")
    print("1. 횟수 대결 플레이 (쉬움)")
    print("2. 글자 수 대결 플레이 (어려움)")
    print("3. PVP 플레이 (점수제)")
    print("4. 단어장 목록")
    print("5. 단어장 설정")
    print("6. 기타 설정")
    print("7. 분석")
    print("8. 종료")
    print("****************************************")

    menu = int(input("실행시킬 번호를 입력하세요:"))
    if menu == 1:
        print("잠시 후 게임이 시작됩니다.\n1=기권, 2=힌트") 
        
        #카운트 함수
        count=3
        while count > 0:
            print(count)
            count = count - 1
        print("start")

        #단어설정
        rd = 0
        already = []
        first = True

        while True:
            #컴퓨터 차례
            if first:
                comWord = random.choice(nounWord)
                already.append(comWord)
                print("COM: {0}".format(comWord))
                first = False
                rd = rd + 1
                lastLetter = comWord[-1]
            else:
                pass

            #내 차례
            myWord = input("단어를 입력하세요:")
            if myWord == "1":
                print("당신은 기권하셨습니다.")
                break
            elif myWord == "2":
                hintList = []
                if hintChance > 0:
                    for temp2 in nounWord:
                        if temp2[0] == lastLetter:
                            hintList.append(temp2)
                        else:
                            pass
                    hint = random.choice(hintList)
                    print("힌트는 {0} 입니다.".format(hint))
                    hintChance = hintChance - 1
                    print("남은 힌트 갯수 {0}".format(hintChance))
                    continue
                else:
                    print("남은 힌트 갯수가 없습니다.")
                    continue
            elif myWord in already:
                print("이미 사용한 단어 입니다.")
                continue
            elif myWord not in nounWord:
                print("없는 단어 입니다.")
                continue
            elif myWord[0] != lastLetter:
                print("{0}(으)로 시작하는 단어를 입력하십시오.".format(lastLetter))
                continue
            else:
                already.append(myWord)
                usedWord.append(myWord)
                rd = rd + 1

            #컴퓨터차례
            if rd >= 20:
                print("당신이 승리하셨습니다!")
                break
            else:
                #첫글자가 맞는 것 고르기
                lastLetter = myWord[-1]
                printList = []
                for temp in nounWord:
                    if temp[0] == lastLetter:
                        printList.append(temp)
                    else:
                        pass
                    
                #컴퓨터 출력
                comWord = random.choice(printList)
                already.append(comWord)
                print("COM: {0}".format(comWord))
                rd = rd + 1
                lastLetter = comWord[-1]
        restart = input("재시작하려면 아무 버튼이나 입력하세요:")
    elif menu == 2:
        print("잠시 후 게임이 시작됩니다.\n1=기권, 2=힌트") 
        
        #카운트 함수
        count=3
        while count > 0:
            print(count)
            count = count - 1
        print("start")

        #단어설정
        rd = 0
        already = []
        first = True
        comScore = 0
        myScore = 0

        while True:
            #컴퓨터 차례
            if first:
                comWord = random.choice(nounWord)
                already.append(comWord)
                print("COM: {0}".format(comWord))
                first = False
                rd = rd + 1
                lastLetter = comWord[-1]
                comScore = comScore + len(comWord)
            else:
                pass

            #내 차례
            myWord = input("단어를 입력하세요:")
            if myWord == "1":
                print("당신은 기권하셨습니다.")
                break
            elif myWord == "2":
                hintList = []
                if hintChance > 0:
                    for temp2 in nounWord:
                        if temp2[0] == lastLetter:
                            hintList.append(temp2)
                        else:
                            pass
                    hint = random.choice(hintList)
                    print("힌트는 {0} 입니다.".format(hint))
                    hintChance = hintChance - 1
                    print("남은 힌트 갯수 {0}".format(hintChance))
                    continue
                else:
                    print("남은 힌트 갯수가 없습니다.")
                    continue
            elif myWord in already:
                print("이미 사용한 단어 입니다.")
                continue
            elif myWord not in nounWord:
                print("없는 단어 입니다.")
                continue
            elif myWord[0] != lastLetter:
                print("{0}(으)로 시작하는 단어를 입력하십시오.".format(lastLetter))
                continue
            else:
                already.append(myWord)
                usedWord.append(myWord)
                rd = rd + 1
                myScore = myScore + len(myWord)

            #컴퓨터차례
            if rd >= 20:
                print("게임 종료!")
                if myScore > comScore:
                    print("당신이 승리하셨습니다! (내점수: {0}, 컴퓨터점수: {1}".format(myScore,comScore))
                elif myScore < comScore:
                    print("당신이 패배하였습니다. (내점수: {0}, 컴퓨터점수: {1}".format(myScore,comScore))
                else:
                    print("무승부! (내점수: {0}, 컴퓨터점수: {1}".format(myScore,comScore))
                break
            else:
                #첫글자가 맞는 것 고르기
                lastLetter = myWord[-1]
                printList = []
                for temp in nounWord:
                    if temp[0] == lastLetter:
                        printList.append(temp)
                    else:
                        pass
                    
                #컴퓨터 출력
                comWord = random.choice(printList)
                already.append(comWord)
                print("COM: {0}".format(comWord))
                rd = rd + 1
                lastLetter = comWord[-1]
                comScore = comScore + len(comWord)
        restart = input("재시작하려면 아무 버튼이나 입력하세요:")
    elif menu == 3:
        print("잠시 후 게임이 시작됩니다.\n1=기권, 2=힌트") 
        
        #카운트 함수
        count=3
        while count > 0:
            print(count)
            count = count - 1
        print("start")

        #단어설정
        rd = 0
        already = []
        first = True
        comScore = 0
        myScore = 0

        while True:
            #P1 차례
            if first:
                comWord = input("P1님, 단어를 입력하세요:")
                if myWord not in nounWord:
                    print("없는 단어 입니다.")
                    continue
                else:
                    already.append(comWord)
                    print("P1: {0}".format(comWord))
                    first = False
                    rd = rd + 1
                    lastLetter = comWord[-1]
                    comScore = comScore + len(comWord)
            else:
                pass

            #P2 차례
            myWord = input("P2님, 단어를 입력하세요:")
            if myWord == "1":
                print("당신은 기권하셨습니다.")
                break
            elif myWord == "2":
                hintList = []
                if hintChanceP2 > 0:
                    for temp2 in nounWord:
                        if temp2[0] == lastLetter:
                            hintList.append(temp2)
                        else:
                            pass
                    hint = random.choice(hintList)
                    print("힌트는 {0} 입니다.".format(hint))
                    hintChanceP2 = hintChanceP2 - 1
                    print("남은 힌트 갯수 {0}".format(hintChanceP2))
                    continue
                else:
                    print("남은 힌트 갯수가 없습니다.")
                    continue
            elif myWord in already:
                print("이미 사용한 단어 입니다.")
                continue
            elif myWord not in nounWord:
                print("없는 단어 입니다.")
                continue
            elif myWord[0] != lastLetter:
                print("{0}(으)로 시작하는 단어를 입력하십시오.".format(lastLetter))
                continue
            else:
                print("P2: {0}".format(myWord))
                already.append(myWord)
                usedWord.append(myWord)
                rd = rd + 1
                lastLetter = myWord[-1]
                myScore = myScore + len(myWord)

            #다시 P1 차례
            if rd >= 20:
                print("게임 종료!")
                if myScore > comScore:
                    print("P2가 승리하였습니다! (P1 점수: {0}, P2 점수: {1}".format(comScore,myScore))
                elif myScore < comScore:
                    print("P1이 승리하였습니다! (P1 점수: {0}, P2 점수: {1}".format(comScore,myScore))
                else:
                    print("무승부! (P1 점수: {0}, P2 점수: {1}".format(comScore,myScore))
                break
            else:
                comWord = input("P1님, 단어를 입력하세요:")
                if comWord == "1":
                    print("당신은 기권하셨습니다.")
                    break
                elif comWord == "2":
                    hintList = []
                    if hintChanceP1 > 0:
                        for temp2 in nounWord:
                            if temp2[0] == lastLetter:
                                hintList.append(temp2)
                            else:
                                pass
                        hint = random.choice(hintList)
                        print("힌트는 {0} 입니다.".format(hint))
                        hintChanceP1 = hintChanceP1 - 1
                        print("남은 힌트 갯수 {0}".format(hintChanceP1))
                        continue
                    else:
                        print("남은 힌트 갯수가 없습니다.")
                        continue
                elif comWord in already:
                    print("이미 사용한 단어 입니다.")
                    continue
                elif comWord not in nounWord:
                    print("없는 단어 입니다.")
                    continue
                elif comWord[0] != lastLetter:
                    print("{0}(으)로 시작하는 단어를 입력하십시오.".format(lastLetter))
                    continue
                else:
                    print("P2: {0}".format(comWord))
                    already.append(comWord)
                    usedWord.append(comWord)
                    rd = rd + 1
                    lastLetter = comWord[-1]
                    comScore = comScore + len(comWord)
        restart = input("재시작하려면 아무 버튼이나 입력하세요:")
    elif menu == 4:
        print("현재 적용 중인 단어장 목록입니다.")
        print(dictList)
    elif menu == 5:
        print("****************************************")
        print("1. 단어장 적용")
        print("2. 단어장 추가")
        print("3. 단어장 삭제")
        print("4. 뒤로가기")
        print("****************************************")
        menu3 = int(input("실행시킬 번호를 입력하세요:"))
        if menu3 == 1:
            print("현재",dictList,"가 적용되어 있으며",dictListOut,"가 미적용되어 있습니다.")
        elif menu3 == 2:
            print("****************************************")
            print("1. 기존 단어장 DB에서 추가")
            print("2. 외부 파일 단어장 불러오기")
            print("****************************************")
            menuDict = int(input("실행시킬 번호를 입력하세요:"))
            if menuDict == 1:
                print("****************************************")
                print("1. 표준국어대사전")
                print("2. 뒤로가기")
                print("****************************************")
                menuDict0 = int(input("추가할 사전의 번호를 입력하세요:"))
                if menuDict0 == 1:
                    dictList.append("표준국어대사전")
                    print("{0}(이)가 추가되었습니다.".format(dictList[-1]))
                else:
                    pass
            elif menuDict == 2:
                cl = input("불러올 파일의 위치를 입력하세요:")
                f = open(cl, "r", encoding="utf-8")
                for contents in f:
                    word.append(contents.strip("\n").replace("^","").replace("-","").split(",").split(" "))
                dictList.append("단어장1")
            else:
                print("다시 입력하십시오.")
        elif menu3 == 3:
            print(dictList)
            dictIndex = int(input("삭제할 사전의 인덱스를 입력하세요:"))
            print("{0}(이)가 삭제되었습니다.".format(dictList[dictIndex]))
            del dictList[dictIndex]
        elif menu3 == 4:
            pass
    elif menu == 6:
        print("****************************************")
        print("1. 난이도 설정")
        print("2. 뒤로가기")
        print("****************************************")
        menu4 = int(input("실행시킬 번호를 입력하세요:"))
        if menu4 == 1:
            nanYN = int(input("현재 난이도는 {0} 상태입니다. 변경하시겠습니까? (예:1 / 아니요:2):".format(nan[0])))
            if nanYN == 1:
                print("****************************************")
                print("1. 난이도 하")
                print("2. 난이도 중")
                print("3. 난이도 상")
                print("****************************************")
                nanYN2 = int(input("숫자를 입력해 난이도를 새로 설정하십시오:"))
                if nanYN2 == 1:
                    del nan[:]
                    nan.append("하")
                    print("난이도 하로 조절되었습니다.")
                    hintChance = 3
                    hintChanceP1 = 3
                    hintChanceP2 = 3
                elif nanYN2 == 2:
                    del nan[:]
                    nan.append("중")
                    print("난이도 중으로 조절되었습니다.")
                    hintChance = 2
                    hintChanceP1 = 2
                    hintChanceP2 = 2
                elif nanYN2 == 3:
                    del nan[:]
                    nan.append("상")
                    print("난이도 상으로 조절되었습니다.")
                    hintChance = 1
                    hintChanceP1 = 1
                    hintChanceP2 = 1
                else:
                    print("다시 입력하십시오.")
                    continue
            elif nanYN == 2:
                pass
            else:
                print("다시 입력하십시오.")
                continue
            continue
        else:
            pass
    elif menu == 7:
        print("단어 분석을 시작합니다.")
        word_analysis = {}
        chosung = [wa[0] for wa in nounWord]
        for chosung_analysis in chosung:
            if chosung_analysis in word_analysis:
                word_analysis[chosung_analysis] = word_analysis[chosung_analysis] + 1
            else:
                word_analysis[chosung_analysis] = 1
        for chosung2, num in word_analysis.items():
            print(chosung2, num)

        print("당신이 지금까지 사용한 단어입니다.")
        print(usedWord)
    elif menu == 8:
        print("게임을 종료합니다.")
        break
    else:
        print("다시 입력하십시오.")