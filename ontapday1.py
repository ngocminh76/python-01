#Bài tập về chuỗi (Strings):
#Viết một hàm nhận vào một chuỗi và in ra các từ có độ dài lớn hơn 5.
import math

def printString(str):
    words = str.split()
    long_word=[word for word in words if len(word)>5]
    print(long_word)

input_string = "Tôi tên là Nguyễn Ngọc Minh, this is a sample in Python"
printString(input_string)
#Bài tập về list (Lists):
#Viết một chương trình nhận vào một list số nguyên 
# và trả về một list mới chỉ chứa các số chẵn từ list ban đầu.
def soChan(lstInt):
    new_list = [int(x) for x in lstInt if x%2==0]
    return new_list
listinput =[1,5,6,7,0,12,3,7,97]
print(soChan(listinput))
#Bài tập về vòng lặp (Loops):
#Viết một hàm tính giai thừa của một số nguyên dương n bằng cách sử dụng vòng lặp.
def factorial(n):
    result = 1
    for i in range( 1, n + 1):
        result *= i
    return result
    # result = 1
    # for i in range(1, n + 1):
    #     result *= i
    # return result

print(factorial(3))
#Bài tập về điều kiện (Conditionals):
#Viết một hàm kiểm tra xem một số nguyên cho trước có phải là số nguyên tố hay không.
def is_prime(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True
number =6
print(is_prime(6))
    
#Bài tập về dictionary (Dictionaries):
#Viết một hàm đếm số lần xuất hiện của mỗi ký tự trong một chuỗi và lưu kết quả vào một dictionary.
def count_characters(string):
    char_count ={}
    for char in string:
        char_count[char] = char_count.get(char,0)+1
    return char_count

in_string = "hellopython"
print(count_characters(in_string))
#
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length +self.width)

rect = Rectangle(4,5)
print("Area :", rect.area())
print("Perimeter :" ,rect.perimeter())
# tạo class hình tròn
class Circle:
    def __init__(self, radius):
        self.radius= radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius

cir = Circle(5)

print(cir.radius())
print(cir.perimeter())
       