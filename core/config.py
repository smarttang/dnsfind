#coding:utf-8
import os

version = 'V1.1'
author = 'Smarttang'

def init_option(keys):
	vardict = {
		'timeout': check_time(keys.timeout),
		'target': check_target(keys.target),
		'dictname': check_dictname(keys.dictname),
		'threads_count': check_threads(keys.threads_count),
		'finger':keys.finger,
		'keywords':check_keywords(keys.keywords)
	}
	return vardict


# 检查关键字
def check_keywords(val):
	if val:
		return val.split(',')
	else:
		return None

# 最高设置为超时10
def check_time(val):
	if val > 0 and val < 10:
		return val
	else:
		return 5

# 默认不能有空值
def check_target(val):
	domain = val.split('.')
	if len(domain) > 1 and '' not in domain:
		return '.'.join(domain)
	else:
		return 'baidu.com'

# 字典检查
def check_dictname(val):
	default_val = 'dict/domain.txt'
	if val:
		if os.path.exists('dict/'+val):
			return 'dict/'+val
		else:
			return default_val
	else:
		return default_val

# 线程数控制
def check_threads(val):
	try:
		threads_count = int(val)

		if threads_count > 0 and threads_count < 21:
			return threads_count
		else:
			return 10
	except Exception, e:
		threads_count = 5
	finally:
		return threads_count