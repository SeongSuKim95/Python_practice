# decorator : 함수의 기능을 확장하고 싶은 경우에 사용
# 함수를 인자로 받아 함수의 기능을 추가한 후 return

from re import X
import time

def func_time_interval(funct):
	def time_check(*args, **kwargs):
		start_time = time.perf_counter()
		result = funct(*args, **kwargs)
		finished_time = time.perf_counter()
		print('실행 소요 시간:', finished_time - start_time)
		return result
	return time_check

# def square(n):
# 	return n*n
	
# new_funct = func_time_interval(square)
# new_funct(5)

@ func_time_interval
def square(n):
    return n*n

square(5)

# decorator 이해하기

# Step 1 : 함수
# Python에 있어서 함수는 def 키워드로 함수명과 파라미터의 리스트(임의)를 이용해 정의한다. 또한 괄호를 붙인 이름을 지정하여 함수를 지정한다.

# Step 2 : 스코프
# Python에서는 함수를 만들면 새로은 스코프가 만들어진다.  다시 말하자면 각각의 함수르 각각의 이름 공간을 가지고 있다는 의미이다.
# Python에서 이것을 확인하기 위한 함수도 준비되어 있다. locals()라는 함수로 자신이 가진 로컬 이름 공간의 값을 사전형으로 반환한다.
# def foo(arg): 
#     x = 10 
#     print(locals())

# foo(20) # {'arg' : 20, 'x' : 10}

# Step 3 : 변수의 해결 규칙
# Python에서의 변수의 해결 룰은 다음과 같다.
# -작성할 때는 항상 새로운 변수가 그 이름공간 안에 만들어진다.
# -참고는 먼저 이름공간 내부터 검색하고 없으면 외부로 검색 영역을 넓혀간다.

# Step 4: 변수의 라이프 사이클
# 네임스페이스는 함수 foo가 호출될 때마다 생성되며 처리가 끝나면 사라져버린다.


# Step 5 : 함수의 인수와 파라미터

# Python에서는 함수에 인수를 전달하는 것이 가능하다. 정의할때의 파라미터의 이름은 로컬 변수의 이름으로써 사용된다.

# def foo(x):
#    print(locals())
# foo(1) # {'x' :1}

# Step 6: 함수의 중첩
# Python에서는 함수 내에 다시 함수를 정의, 즉 중첩할 수 있다.

def outer():
    x = 1
    def inner():
        print(x) # 1
    inner() # 2
outer() 
# #1에서는 로컬 변수 x를 찾아보지만, 내부의 네임스페이스에 없으므로 외부의 네임 스페이스를 찾아서 outer내에 정의되어 있는 x를 참고한다. 
# 또한 #2에서는 inner()를 호출하고 있지만, inner이라는 것 또한 하나의 변수명에 지나지 않고 outer내의 namespace에서 정의를 찾아서 호출한다.

# Step 7: 함수는 python에게 있어서 퍼스트 클래스 오브젝트이다.
# Python에서 함수는 객체에 불과하다.

print(issubclass(int,object)) # True
print(outer.__class__) # <class 'function'>
print(issubclass(outer.__class__,object)) # True

# 즉, 함수를 일반적인 다른 변수와 동일하게 취급한다. 다른 함수의 인수로 전달하거나 함수의 리턴값으로써 사용할 수 있다.

def outer_2():
    def inner_2():
        print("Inside Inner")
    return inner_2

a = outer_2()
a() # Inside Inner

# Step 8 : 
