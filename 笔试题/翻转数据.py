import pprint



def rotate(grid, row, col):
    n_row = len(grid)
    n_col = len(grid[0])
    col = col - 1
    row = row - 1
    if 0 < col < n_col - 1:
        left = col - 1
        right = col + 1
        grid[row][left], grid[row][right] = grid[row][right],grid[row][left]
        print("左右翻转", row+1, col+1)
        print("\n".join([str(item) for item in grid]))
        print("=" * 30)

    if 0 < row < n_row - 1:
        up = row - 1
        down = col + 1
        grid[up][col], grid[down][col] = grid[down][col], grid[up][col]
        print("上下翻转", row+1, col+1)
        print("\n".join([str(item) for item in grid]))
        print("=" * 30)

def task(grid, coords):
    for row, col in coords:
        rotate(grid, row, col)
    return grid

if __name__ == "__main__":
    line1 = input()
    print(line1)
    # line2 = input()
    # grid = eval(line1)
    # coords = eval(line2)
    # grid =[[0, 0, 1, 1], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0]]
    # print("\n".join([str(item) for item in grid]))
    # coords = [[2, 2], [3, 3], [4, 4]]
    # new_grid = task(grid, coords)
    # print(new_grid)


# filpColor函数是将黑白棋子的颜色翻转，1变为0，0变为1
def flipChess(color):
    # color代表棋子的颜色
    if color == 1:
        return 0
    else:
        return 1
    # 可简化为
    # return 0 if color == 1 else 1


# array是存储需要翻转棋盘数组，position是定支点位置
def doFlip(array, position):
    for i in position:
        # 获取数组索引 = 棋盘坐标 - 1
        row, col = i[0] - 1, i[1] - 1
        # 如果定支点还有左方棋子（即行索引大于0），则进行翻转
        if row > 0:
            array[row - 1][col] = flipChess(array[row - 1][col])
        # 如果定支点还有右方棋子（即行索引小于3），则进行翻转
        if row < 3:
            array[row + 1][col] = flipChess(array[row + 1][col])
        # 如果定支点还有上方棋子（即列索引大于0），则进行翻转
        if col > 0:
            array[row][col - 1] = flipChess(array[row][col - 1])
        # 如果定支点还有下方棋子（即列索引小于3），则进行翻转
        if col < 3:
            array[row][col + 1] = flipChess(array[row][col + 1])
    return array



"""
N = int(input().strip())
arr = []
for i in range(N):
    arr.append(int(input().strip()))
for j in range(N): 
    k=1
    while k<N-j: 
        if arr[j+k]>arr[j]:
            print(k)
            break
        k+=1
    else:
        print(-1)
"""

"""
data1List = input('')
data2List = input('')
 
data1List = data1List.split(' ')
data2List = data2List.split(' ')
 
id1 = data1List[0]
name = data1List[1]
id2 = data2List[0]
JanLen = data2List[2]
FebLen = data2List[4]
MarLen = data2List[6]
TotalLen = int(JanLen)+int(FebLen)+int(MarLen)
 
print("%s %s %s %s %d" % (name,JanLen,FebLen,MarLen,TotalLen))
"""

"""
callist = input('')
nums = input('')
callist = callist.split(' ')
n = int(callist[0])    #数组长度
k = int(callist[1])    #窗口大小
nums = nums.split(' ')
resultlist = []
 
for i in range(len(nums)):
    nums[i]=float(nums[i])
for j in range(0,len(nums)-k+1):
    slide=nums[j:j+k]
    slide.sort()
    if(k%2==0):
        median = (slide[int(k/2)-1]+slide[int(k/2)+1-1])/2
    else:
        median = (slide[int((k+1)/2)-1])
    median = str(median)
    resultlist.append(median)
resultstring = ' '.join(resultlist)
print(resultstring)
"""
"""
def get_month_year(x, y):
    if y in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif y in [4, 6, 9 ,11]:
        return 30
    elif y == 2 and x%4 == 0 and x%100 != 0&nbs***bsp;x%400 == 0:
        return 29
    else:
        return 28
while True:
    try:
        year, month = map(int,input().split())
        print(get_month_year(year, month))
    except:
        break;
"""

"""
def GetTypeNum(n,k):
    n = n-1 #间隔总数
    k = k-1 #需要的分割的间隔数
    if n%2 == 0:
        half = int(n/2)
    if n%2 != 0:
        half = int((n+1)/2)        
    j = []
    for i in itertools.combinations(range(1,half+1), k): #无放回不重复抽样
        li = list(i)
        j.append(li)
    return len(j)
"""

if __name__ == '__main__':
    array = eval(input())
    position = eval(input())
    doFlip(array, position)
    print(str(array).replace(' ', ''))
