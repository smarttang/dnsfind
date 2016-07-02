#coding:utf-8

import socket, gevent, os
from gevent.pool import Pool
from core.utils import findreport, FindObj, getpath

class DnsFind:

	def __init__(self,options):
		self.options = options
		self.blockip = None
		self.keywords = False
		self.pool = Pool(self.options['threads_count'])
		self.document = self.options['target'].replace('.','_')+'.txt'
		socket.setdefaulttimeout(self.options['timeout'])

	# 域名解析
	def checkdomain(self,domain=None,mode=None):
		print '[*] Check domain: %s' % domain
		try:
			results = socket.getaddrinfo(domain,None)[0][4][0]
		except Exception, e:
			results = None
		finally:
			if results is not None and mode != 'block':

				# 识别指纹
				if self.options['finger']:
					domain_finger = FindObj(domain).findfinger()
					print '\033[1;32;40m[*] Domain alive: %s => %s => %s!! \033[0m' % (domain,results,domain_finger) 
				else:
					print '\033[1;32;40m[*] Domain alive: %s => %s!! \033[0m' % (domain,results)

				# 页面关键字搜索
				if self.options['keywords']:
					for _keyword in self.options['keywords']:
						if FindObj(domain,_keyword).findcontent():							
							self.keywords = True

				ipgroup = results.split('.')
				data = [results,'.'.join(ipgroup[:3])]

				# 存储结果
				# 第一种，激活了关键字筛选且有关键字匹配，则存储。
				# 第二种，没有激活关键字，存储
				if self.options['keywords'] is not None and self.keywords == True or self.options['keywords'] is None:
					report = open(getpath()+'/result/'+self.document,'a+')
					report.write(domain+'\n')
					report.close()
			else:
				data = None

			# block模式，主要是测试是否有block功能
			if mode == 'block':
				return data
	
	# 字典爆破
	def run(self):
		# 先判断结果是否存在过
		# 以及报告目录是否存在
		findreport(self.document)

		# 先检测一个不存在的地址
		# 如果能解析，则证明做了一些保护措施
		# 将对方地址记录下来，作为block的标准
		block_check_results = self.checkdomain('d312379196bd822558ca7dfb3c95ba61.'+self.options['target'],'block')
		
		if block_check_results:
			self.blockip = block_check_results[0]

		# 构建字典
		dic_list = (dic.strip('\n')+'.'+self.options['target'] for dic in open(getpath() + '/' +self.options['dictname'],'r'))
		# 协程爆破测试
		self.pool.map(self.checkdomain,dic_list)