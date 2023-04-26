import numpy as np
class Student():
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def record(self, name:str, score:int):                      #將分數累加到該同學的名字底下
        self.dictionary[name] = self.dictionary[name] + score
    
    def best_student(self):                                     #返回分數最高的學生&分數
        return max(self.dictionary,key = self.dictionary.get)
                        
    def worst_student(self):                                    # 返回分數最低學生&分數
        return min(self.dictionary,key = self.dictionary.get)
    
    def pop(self, name):                                        #刪除學生
        return self.dictionary.popitem(name)
                    
    def add(self, name, score):                                 #新增轉學生
        return self.dictionary.update({name:score})
                     
    def total_score(self):                                      #返回所有學生總分
        return sum(self.dictionary.values())   

    def sort(self):                                             #將學生名字按照分數由高到低排列，返回一個list
        return sorted(self.dictionary.items(), key = lambda x:x[1],reverse=True)
        
    def evaluate(self):                                         #返回所有學生的分數的平均、標準差                                         
        average = self.total_score() / len(self.dictionary)
        standard = np.std(list(self.dictionary.values()))
        return average , standard
    
#operations
dictionary_a = {'John':30, 'Mary':5, 'Cindy':-5, 'Carol':3}
student = Student(dictionary_a)
student.record('John', 20)
print(f'將分數累加到該同學的名字底下 {student.dictionary}')
print(f'返回分數最高的學生&分數 {student.best_student()}')
print(f'返回分數最低學生&分數 {student.worst_student()}')
dictionary_a.pop('John')
print(f'刪除學生 {dictionary_a}')
student.add('Andy', 10)
print(f'新增轉學生 {dictionary_a}')
print(f'返回所有學生總分 {student.total_score()}')
print(f'將學生名字按照分數由高到低排列，返回一個list {student.sort()}')
print(f'返回所有學生的分數的平均、標準差 {student.evaluate()}')
