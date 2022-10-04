# 주의: 기존 코드를 수정하지 마세요.
# 주석을 통해 코드를 설명하는 것을 권장합니다.
# 세미 콜론(;)을 통한 코드 이어 붙이기는 금지입니다.

# Problem 1
# 내부 코드는 오로지 한 줄이어야 합니다.
# Hint: max 함수에 대해 알아보세요.
def p1(X):
    return [i[[sum([int(j) for j in list(str(n))]) for n in i].index(max([sum([int(j) for j in list(str(n))]) for n in i]))] for i in X] if X != None else None

#Problem 2
# 내부 코드는 최대 세 줄이어야 합니다.
def p2(X):
    example_list = [j for j in X if j >= 0]
    answer_list = [[0 if k != i else 1 for k in range(max(example_list) + 1)] for i in example_list]
    return answer_list

# Problem 3
# 내부 코드는 최대 네 줄이어야 합니다.
# Hint: sample과 data의 크기가 클 수 있기 때문에 효율적인 자료구조를 사용하세요.
def p3(sample, data):
  last_name, first_name = [i[0] for i in data], [i[1:3] for i in data]
  return [True if i[0] in last_name and i[1:3] in first_name else False for i in sample]

# Problem 4
# 내부 코드는 최대 여섯 줄이어야 합니다.
def p4(sample,data):
  data_list = sorted(list(set([j.lower() for i in data for j in i.split()])))
  answer_list = [[data_list.index(l.lower()) if l.lower() in data_list else len(data_list) for l in k.split()] for k in sample]
  return answer_list

class Matrix2d:
    def __init__(self, data):
        assert len(data) > 0
        self.data = [list(row) for row in data]
        self.shape = (len(data), len(data[0]))
        
    def add(self, x):
        assert self.shape == x.shape
        r, c = self.shape
        for i in range(r):
            for j in range(c):
                self.data[i][j]+=x.data[i][j]
    
    def where(self, func):
        r, c = self.shape
        for i in range(r):
            for j in range(c):
                if func(self.data[i][j]):
                    yield i, j
            
    def __eq__(self, img):
        return img.data == self.data and img.shape == self.shape
    
    def __repr__(self):
        return str([list(map(lambda x: round(x, 4), row)) for row in self.data])
    
# Problem 5
# p5 함수가 정상 동작 하게끔 아래 클래스를 구현하세요.
class GrayScaleImg(Matrix2d):
    def __init__(self, data):
        assert all(all(0<=x and x<=1 for x in row) for row in data)
        super().__init__(data)
    
    def ImgAdd(self, img):
        assert isinstance(img, GrayScaleImg)
        super().add(img)
        add_list = self.data
        for i in range(len(add_list)):
          for j in range(len(add_list[i])):
            if add_list[i][j] > 1:
              add_list[i][j] = 1
        self.data = add_list
    
    def Transpose(self):
        self.data = [list(x) for x in zip(*self.data)]
    
    
    def FixBrightness(self, threshold, ratio):
        assert 0 <= ratio and ratio <= 1
        add_list = self.data
        for x in range(len(add_list)):
          for y in range(len(add_list[x])):
            if add_list[x][y] > threshold:
              add_list[x][y] = add_list[x][y] * ratio
        self.data = add_list
          
    def Pad(self):
        add_list = self.data       
        for x in range(len(add_list)):
            add_list[x].insert(0, 0)
            add_list[x].append(0)
        add_list.insert(0, [0] * (len(add_list[0]))) 
        add_list.append([0] * (len(add_list[0])))
        self.data = add_list
        
def p5(data, low, img_to_add, threshold, ratio):
    try:
        result = dict()
        img = GrayScaleImg(data)
        result["lower"] = list(img.where(lambda x: x < low))
        
        to_add = GrayScaleImg(img_to_add)
        img.ImgAdd(to_add)
        result["add"] = Matrix2d(img.data)
    
        img.Transpose()
        result["transpose"] = Matrix2d(img.data)

        img.FixBrightness(threshold, ratio)
        result["fix"] = Matrix2d(img.data)

        img.Pad()
        result["pad"] = Matrix2d(img.data)
        return result
    
    except Exception as e:
        print("[Error]", e)
        return None
        

    
# Problem 6
# n은 매우 큰 수가 될 수 있음을 유의하세요.
def p6(n):
    dp = [0, 1]
    for i in range(n+1):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = 1
        else:
            if i % 2 == 0:
                dp[0] = (dp[0] % (10**9 + 7) + dp[1] % (10**9 + 7)) % (10**9 + 7)  
            else:
                dp[1] = (dp[0] % (10**9 + 7) + dp[1] % (10**9 + 7)) % (10**9 + 7)
    if i % 2 == 0:
        return dp[0]
    else:
        return dp[1]