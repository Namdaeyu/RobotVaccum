#https://www.koreascience.or.kr/article/JAKO201117057862338.pdf
#https://www.koreascience.or.kr/article/JAKO200504840652372.pdf


# 메인 함수
def main():
    myList = [  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 2, 2, 0, 0, 2, 2, 0, 1],
                [1, 0, 2, 2, 0, 0, 2, 2, 0, 1],
                [1, 0, 0, 2, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 2, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 2, 2, 0, 1],
                [1, 0, 0, 0, 0, 0, 2, 2, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]
    rowList = []
    colList = []

    rowList = cellDivision(myList, "ROW")                               #행 기준으로 셀분할하기
    colList = cellDivision(myList, "COL")                               #열 기준으로 셀분할하기

# 셀 분할 알고리즘
def cellDivision(mapArray, type):

    if(type == "COL"):                                                  #열 기준으로 구역분할할 시
        mapArray = rotate_map_in90(mapArray)                            #맵의 구조를 90도 시계방향 회전시킨다

    for i in mapArray:
        print(i)

    tempList = []
    rowList = []

    #행 숫자
    rowCount = 0

    for row in mapArray:
        count = 0                                                       #배열 인덱스
        colStart = 0                                                    #열 시작 인덱스
        colEnd = 0                                                      #열 종료 인덱스
        obsStart = 0                                                    #장애물 시작 인덱스
        obsEnd = 0                                                      #장애물 종료 인덱스

        for col in row:
            if(col == 0):                                               #열이 빈칸일 경우
                if(colStart == 0):                                      #열의 시작이 빈 경우
                    colStart = count                                    #열 시작 인덱스 삽입
                if(colStart != 0):                                      #열 시작 인덱스가 있을 경우
                    colEnd = count                                      #열 종료 인덱스 삽입
                    if(obsStart != 0):                                  #장애물이 있을 경우
                        obsEnd = count                                  #장애물 종료 인덱스 삽입
                        obsStart = 0                                    #장애물 시작 인덱스 초기화

            elif(col == 2):                                             #장애물이 있을 경우
                if(obsStart == 0):                                      #아직 장애물 시작점이 안정해졌을 때
                    tempList.append([rowCount, colStart, count - 1])    #구역 구분된 것을 정렬
                    colStart = 0                                        #열 시작 인덱스 초기화
                    obsStart = count                                    #장애물 시작 인덱스 삽입
                    
            count += 1                                                  #배열 인덱스 증가

        if(colStart !=0 and colEnd != 0):                               #열의 시작&종료 인덱스가 있을 시
            tempList.append([rowCount, colStart, colEnd])               #임시리스트에 삽입

        rowCount += 1                                                   #행 인덱스 증가

    rowList = cellMerge(tempList)                                       #셀 구역 합쳐서 정확한 구역 분할
    return rowList
    

#맵을 시계방향으로 90도 돌리는 함수
def rotate_map_in90(mapArray):
    if(len(mapArray) < 0):                                          #맵이 없을 경우 예외처리
        return mapArray

    rowLength = len(mapArray)                                       #행의 길이
    colLength = len(mapArray[0])                                    #열의 길이
    newList = [[0] * rowLength for _ in range(colLength)]           #새로운 리스트의 길이 고정

    for row in range(rowLength):                            
        for col in range(colLength):
            newList[col][rowLength-1-row] = mapArray[row][col]      #새로운 리스트 삽입
    
    return newList


#구역별로 구분한 것을 다시 합치는 함수
#[행의 시작점, 행의 종료점, 열의 시작위치, 열의 종료위치] 형태의 2차원 리스트로 반환
def cellMerge(arrayList):
    rowList = []                                                            #반환할 전체 구역리스트
    tempList = []                                                           #임시 리스트
    selectedIndexList = []                                                  #리스트중 선택된 인덱스

    #arrayList는 [행 인덱스, 열의 시작인덱스, 열의 종료 인덱스]로 구성되어있다

    #똑같은 구역을 확인할 반복문
    for i in range (len(arrayList)):
        flag = 1                                                            #선택된 구역을 확인할 boolean
        for selected in selectedIndexList:                                  #선택된 구역 인덱스 확인
            if(selected == i):
                flag = 0
                break
            
        if(flag):                                                           #선택된 구역이 아니라면
            for j in range (len(arrayList)):                                #배열 중 자기와 같은 range가 있는 지 확인
                if(j == 0):                                                 #첫번재와 똑같은 것을 비교하지 않기 위하여 j에 1을 더해준다
                    j += 1

                if(i + j > len(arrayList) - 1):                             #배열의 길이를 넘지않기 위한 예외처리
                    break

                #만약 같은 range를 청소를 한다면 합쳐준다
                if(arrayList[i][1] == arrayList[i+j][1]
                    and arrayList[i][2] == arrayList[i+j][2]):
                    if(tempList == []):                                     #임시리스트가 비어있을 때 초기화 작업
                        if(arrayList[i][0] < arrayList[i+j][0] - 1):        #임시리스트가 비어있을 때 중간에 구역이 제대로 이어지지 않는다면 스킵
                            break

                        tempList = [arrayList[i][0], arrayList[i+j][0],
                                    arrayList[i][1], arrayList[i+j][2]]

                    if(tempList != []):                                     #임시리스트가 비어있지 않다면 행 시작 인덱스는 놔두고 
                        if(arrayList[i][0] < arrayList[i+j][0] - 2):        #임시리스트가 비어있지 않을 때 구역이 제대로 이어지지 않는다면 스킵
                            break

                        tempList = [tempList[0], arrayList[i+j][0],         #행 종료 인덱스만 바꾼다
                                    arrayList[i][1], arrayList[i+j][2]]

                    selectedIndexList.append(i+j)                           #선택된 인덱스는 나중에 스킵하기 위하여 새로운 리스트에 더한다

            if(tempList == []):                                                                         
                rowList.append([arrayList[i][0], arrayList[i][0], arrayList[i][1], arrayList[i][2]])    #임시리스트가 비어있다면 자기자신의 행시작과 종료인덱스를 삽입
            else:
                rowList.append(tempList)                                                                #임시리스트 삽입
            tempList = []                                                                               #임시리스트 초기화

    selectedIndexList.sort()                                                                            #선택된 인덱스 정렬
    
    return rowList

# 플로우 네트워크
def flowNetwork(mapArray):
    ""

# 실행 함수
if __name__ == "__main__":
    main()