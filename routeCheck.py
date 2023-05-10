from collections import deque
import copy
from itertools import permutations

class Stack :                                                                           ## backTracking 알고리즘과
                                                                                        ## 유사한 방법으로 경로를 찾기위해 stack을 사용                                                  
    def __init__(self):
        self.top=[]
    def isEmpty(self):return len(self.top)==0
    def size(self):return len(self.top)
    def clear(self):self.top=[]
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def __str__(self):
        return str(self.top[::-1])



direction = [[1,0],[-1,0],[0,1],[0,-1]]                                             ## 상하좌우의 이동방향값 

    
def isValidPos(A,x,y):                                                                  ## 해당하는 좌표가 map의 범위에 속해있으며
                                                                                        ## 청소할 구역(0)의 값을 가지는지 확인하는 함수
    if (((x < len(A)-1) and (x>0))
        and ((y < len(A[0])-1) and (y>0))) : 
        if (A[x][y] == 0):
            return True
    return False


def routeCheck(A,R,C):

    priorityDir = list(permutations(direction, 4))                                      ## 상하좌우의 모든 우선 순위 경우의 수를 저장

    for i in range(len(priorityDir)):
        priorityDir[i] = list(priorityDir[i])       

    print(priorityDir)
    print()
    
    X = 0                                                                               ## 시작점 start의 x 좌표
    Y = 0                                                                               ## 시작점 start의 y 좌표
    for x in range(R):                                                                  ## 로봇의 현재 위치(3)의 값을 찾아 저장
        for y in range(C):
            if (A[x][y] == 3):
                X = x
                Y = y
                
    lenList = []                                                                        ## priorityDir의 모든 원소에 대한 결과값을 저장
    
    for i in priorityDir:
        visitedRoute = copy.deepcopy(A)                                                 ## 방문한 위치를 저장
    
        start = [X,Y]                                                                   ## 알고리즘을 실행하기 위한 시작점 start 의 좌표 List
        queue = deque([start])                                                          ## 알고리즘을 위한 stack, 첫 좌표 삽입

        breakPoint = Stack()                                                            ## 경로의 분기점을 저장하는 stack
        length = 0                                                                      ## 경로의 길이를 저장
        while(queue):
            
            v = queue.pop()
            count = 0                                                                   ## 분기 발생을 체크하기위한 변수
            for j in i:
                if( isValidPos(A,v[0]+j[0],v[1]+j[1])                                   ## 이동한 좌표가 청소할 구역과 
                    and visitedRoute[v[0]+j[0]][v[1]+j[1]] == 0):                       ## 청소한 구역인지 체크
                
                    queue.append([v[0]+j[0],v[1]+j[1]])                                 ## 이동한 좌표가 청소할 구역이면 stack에 삽입
                    visitedRoute[v[0]+j[0]][v[1]+j[1]] = 1                              ## 해당 좌표를 방문 처리
                
                    count = count + 1                                                   

            if count >= 2:                                                              ## count가 2이상이면 분기가 발생했으므로 
                breakPoint.push(v)                                                      ## 해당 좌표를 breakPoint에 삽입
            
            elif count == 0 and not breakPoint.isEmpty():                               ## count가 0이면 더이상 주변에 청소할 구역이 없으므로
                point = breakPoint.pop()                                                ## 가장 최근의 분기점을 pop하여 되돌아감
                length = length + (abs(v[0]-point[0]) + abs(v[1]-point[1]) - 1)         ## 분기점 까지 돌아가는 경로의 길이를 length에 추가

            length = length + 1
            visitedRoute[v[0]][v[1]] = 1                                                ## queue에서 pop한 좌표를 방문 처리
            
        lenList.append(length)                                                          ## priorityDir의 원소에 대한 결과값을 저장

    print(lenList)          
    minDir = priorityDir[lenList.index(min(lenList))]                                   ## 가장 적은 길이를 가진 경로의 우선 방향 출력
    print(minDir)
    
    return lenList  

    
