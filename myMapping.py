import random
import copy
import sys
from collections import deque


##cleanMap = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
##            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
##            


cleanMap = [[0,0,0,0,0,0,0,0,0,0],                  ## 10*10 맵 
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]


visited = []                                        ## isolationCheck에서 사용하는 방문노드 저장 List

def isolationCheck (A, R, C):                       ## 랜덤 매핑 중, 고립구간을 제거하기 위해 BFS알고리즘과 유사한 방법을 사용한 함수
                                                    ## 방문 노드의 수(vCount)를 체크하여 청소할 구역(count)의 수와 동일하면 True 아니면 False를 return
    
    visited = copy.deepcopy(A)                      ## 방문 노드를 체크하기위해 map을 deepcopy
    
    count = 0                                       ## 청소할 구역의 수를 저장

    for i in range(R):                              
        for j in range(C):
            if (A[i][j] == 0):
                count = count+1
    X = 0                                           ## 시작점 start의 x 좌표
    Y = 0                                           ## 시작점 start의 y 좌표
    for x in range(R):                             
        for y in range(C):
            if (A[x][y] == 0):
                X = x
                Y = y
    
    start = [X,Y]                                   ## BFS알고리즘을 실행하기 위한 시작점 start 의 좌표 List
    queue = deque([start])                          ## BFS알고리즘을 위한 deque
    
    vCount = 0                                      ## 방문 노드의 수를 저장
    while(queue):                                   ## queue가 비어있을 때 까지
        v = queue.popleft()                         ## 먼저 들어온 좌표를 pop
        
        if( isValidPos(A,v[0],v[1]-1)
           and visited[v[0]][v[1]-1] == 0):         ## down
            queue.append([v[0],v[1]-1])             ## 해당 좌표를 queue에 저장
            visited[v[0]][v[1]-1] = 1               ## 해당 좌표를 방문 처리
        if( isValidPos(A,v[0],v[1]+1)
           and visited[v[0]][v[1]+1] == 0):         ## up
            queue.append([v[0],v[1]+1])             ## 해당 좌표를 queue에 저장 
            visited[v[0]][v[1]+1] = 1               ## 해당 좌표를 방문 처리
        if( isValidPos(A,v[0]-1,v[1])
           and visited[v[0]-1][v[1]] == 0):         ## left
            queue.append([v[0]-1,v[1]])             ## 해당 좌표를 queue에 저장
            visited[v[0]-1][v[1]] = 1               ## 해당 좌표를 방문 처리
        if( isValidPos(A,v[0]+1,v[1])
           and visited[v[0]+1][v[1]] == 0):         ## right
            queue.append([v[0]+1,v[1]])             ## 해당 좌표를 queue에 저장
            visited[v[0]+1][v[1]] = 1               ## 해당 좌표를 방문 처리
        
        vCount = vCount+1                           ## 방문 좌표의 수를 체크
        visited[v[0]][v[1]] = 1                     ## queue에서 pop한 좌표를 방문 처리
        
    if (vCount == count):                           ## 방문 노드의 수와 청소할 구역의 수가 같으면 True
        return True
    
    return False                                    
    
def isValidPos(A,x,y):                              ## 해당하는 좌표가 map의 범위에 속해있으며 청소할 구역(0)의 값을 가지는지 확인하는 함수
    if (((x < len(A)-1) and (x>0))
        and ((y < len(A[0])-1) and (y>0))) : 
        if (A[x][y] == 0):
            return True
    return False

def wall(A, R, C):                                  ## 초기 상태의 map에 외벽(1)을 추가하는 함수
    for i in range(0,R):
        for j in range(0,C):
            if i == 0 or j == 0:
                A[i][j] = 1
            
            if i == (R-1) or j == (C-1):
                A[i][j] = 1


def randomWalk(R, C):                               ## 랜덤한 장애물(2)을 생성하는 함수
    
    newMap = copy.deepcopy(cleanMap)                ## 랜덤한 장애물을 저장하는 변수
    
    for k in range(20):                             ## 임의의 수를 지정하여 랜덤하게 생성
        a = random.randint(1,R-2)
        b = random.randint(1,C-2)
        newMap[a][b] = 2

    while not (isolationCheck(newMap, R, C)):       ## isolationCheck를 통해 고립된 구역이 없을 때 까지 반복
        return randomWalk(R, C)

    return newMap                                   ## 생성된 맵을 return


def obsCheck(A, R, C):                              ## 장애물을 판단하여 벽(1)과 장애물(2)로 저장
    tempMap = copy.deepcopy(A)                      ## 벽과 장애물을 완전히 판단했는지 검사하기위한 임시 map 저장소
    mapCheck = 0                                    ## 0: 검사 완료, 1: 검사 중
    
    while(obsCheck):                                ## 재귀함수를 이용하여 벽과 장애물을 검사
        for i in range(1,R-1):
            for j in range(1,C-1):
                if (A[i][j] == 2):                  ## 장애물이 벽인지 검사, 벽이라면 장애물(2)을 벽(1)으로 변환
                    if ((A[i-1][j] == 1) or
                        (A[i][j-1] == 1) or
                        (A[i+1][j] == 1) or
                        (A[i][j+1] == 1)):
                        A[i][j] = 1
                        
        for a in range(0,R):                        ## 이전 상태의 map과 현재 상태의 map을 검사하여 변한 부분이 있는지 체크
            for b in range(0,C):
                if (tempMap[a][b] != A[a][b]):
                    mapCheck = 1
                    
        if (mapCheck == 1):                         ## 변환이 일어났다면 재귀함수를 이용하여 다시 check
            return obsCheck(A,R,C)
        return True


def printMap(A):                                    ## map을 출력하는 함수
    for i in A :
        for j in i:
            print(j,end=" ")
        print()

def makeMap(A,Row,Col):
    
    newMap = copy.deepcopy(A)

    for i in range(Row):
        for j in range(Col):
            if not (newMap[i][j] == 0):
                newMap[i][j] = 'x'

    return newMap

def startPos(A,R,C):
    start = input("Machine position: ").split()
    start = [int(start[0]),int(start[1])]
    while(True):
        if A[start[0]][start[1]] == 0:
            print('Valid start position {0},{1}'.format(start[0],start[1]))
            A[start[0]][start[1]] = 3
            return True
        else :
            print("Unvalid start position")
            return startPos(A,R,C)
    return False

    
def main():
    global cleanMap
    maxRow = len(cleanMap)                          ## map의 Row 크기를 저장
    maxCol = len(cleanMap[0])                       ## map의 Col 크기를 저장
    
    wall(cleanMap, maxRow, maxCol)

    sys.setrecursionlimit(100000000)                ## 재귀 깊이 한계를 설정
    
    cleanMap = randomWalk(maxRow, maxCol)           

    obsCheck(cleanMap, maxRow, maxCol)
    
    cleanMap = makeMap(cleanMap,maxRow,maxCol)

    startPos(cleanMap,maxRow,maxCol)
    
    printMap(cleanMap)

main()

