#coding:utf-8

import os

# 查报告是否存在
# 判断报告目录是否存在，不存在择新建
# 如果存在，则删除历史报告
def findreport(val):
	if not os.path.exists('result/'):
		os.mkdir('result/')
	else:
		target = 'result/'+val
		if os.path.exists(target):
			os.remove(target)
