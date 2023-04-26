class Stack():
    def __init__(self, list):
        self.list = list
    
    def isEmpty(self) -> bool:
        return not len(self.list) > 0   #回傳是否為空值

    def push(self, item: str):          #將元素加到list的最右端
        return self.list.append(item)   
    
    def pop(self):                      #將最右端元素移除
        return self.list.pop(-1)
    
    def peak(self):                     #返回最右端元素
        return self.list[-1]
    
    def size(self):                     #返回list長度
        return len(self.list)

#operations
list_a = ['a','aa','aaa','b','d','c','bbb']
stack = Stack(list_a)
print(f'回傳是否為空值:{stack.isEmpty()}') #False
stack.push('zzz')
print(f'將元素加到list的最右端 {list_a}') #['a','aa','aaa','b','d','c','bbb','zzz']
stack.pop()
print(f'將最右端元素移除 {list_a}') #['a','aa','aaa','b','d','c','bbb']
print(f'返回最右端元素 {stack.peak()}') #'bbb'
print(f'返回list長度 {stack.size()}') #7