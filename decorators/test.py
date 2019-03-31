import datetime

# decorated = decorator(decorated)

# def decorator(func):
# 	def new_func():
# 		return 42
# 	return new_func
#
#
# @decorator
# def decorated():
# 	print('hello')
#
#
# print(decorated())


##############################################
# def deco(f):
# 	print("Вызвана функция {}".format(f.__name__))
# 	return f
#
#
#
# @deco
# def printer(x):
# 	return "х = {}".format(x)
#
#
# r = printer(10)
# print(r)



#############################################



# def logger(func):
# 	def wrapped(*args,**kwargs):
# 		result = func(*args,**kwargs)
# 		with open('log.txt','a+') as f:
# 			f.write(str(datetime.datetime.now()) + ' ' + str(result)+'\n')
# 		return result
# 	return wrapped
#
#
#
# @logger
# def summator(num_list):
# 	return sum(num_list)
#
#
# summator([1,2,3,4,5])




##################################################




def logger(filename):
	def decorator(func):
		def wrapped(*args,**kwargs):
			result = func(*args,**kwargs)
			with open(filename,'a+') as f:
				f.write(str(result) + '\n')
			return result
		return wrapped
	return decorator
	
	
	
	
@logger('new_log.txt')	
def summator(num_list):
	return sum(num_list)



summator([1,2,3,4,5])