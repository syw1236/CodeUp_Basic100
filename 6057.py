
# 2개의 정수값이 입력될 때, 
# 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and b) or(not a) and (not b))