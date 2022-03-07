# decorater : 함수의 기능을 확장하고 싶은 경우에 사용
# 함수를 인자로 받아 함수의 기능을 추가한 후 return

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