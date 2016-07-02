#coding:utf-8

import os, requests, sys

# 获得绝对路径
def getpath():
	return sys.path[0]

# 查报告是否存在
# 判断报告目录是否存在，不存在择新建
# 如果存在，则删除历史报告
def findreport(val):
	path = getpath() + '/result/'
	if not os.path.exists(path):
		os.mkdir(path)
	else:
		target = path + val
		if os.path.exists(target):
			os.remove(target)


# 1、查服务指纹
# 2、页面关键字筛选
class FindObj:

	def __init__(self,target,keyword=None):
		self.target = target
		self.response = None
		self.keyword = keyword
			
	def _getrequest(self):
		try:
			self.response = requests.get('http://'+target)
		except:
			pass

	# 获得服务指纹
	def findfinger(self):
		self._getrequest()

		if self.response:
			return self.response.headers['Server']
		else:
			return None

	# 获得页面内容
	# 比对关键字规则
	def findcontent(self):
		self._getrequest()

		if self.response:
			content = ''.join([con.strip() for con in self.response.content.split('\n')])

			if self.keyword:
				for keyword_item in self.keyword:
					if content.find(keyword_item) != -1:
						return True
		return False
