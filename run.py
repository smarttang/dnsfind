#coding:utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from core.config import version,author,init_option
from core.dnsfind import DnsFind
from optparse import OptionParser 

if __name__ == '__main__':
	usage = '''　　
    ____             _______           __
   / __ \____  _____/ ____(_)___  ____/ /
  / / / / __ \/ ___/ /_  / / __ \/ __  / 
 / /_/ / / / (__  ) __/ / / / / / /_/ /  
/_____/_/ /_/____/_/   /_/_/ /_/\__,_/ 

         	Author: %s && Ver: %s
	''' % (author,version)
	print usage
	parser = OptionParser()
	parser.add_option("-u", "--target", dest="target", default=None, help="set domain.(simple: baidu.com)")
	parser.add_option("-t", "--threads", dest="threads_count", default=None, help="threads count.(default 10)")
	parser.add_option("-s", "--timeout", dest="timeout", default=5, help="set timeout of requests.(default 5s)")
	parser.add_option("-d", "--dictname", dest="dictname", default=None, help="choice dicts.(default All)")

	(options, args) = parser.parse_args()

	try:
		DnsFind(init_option(options)).run()
	except KeyboardInterrupt, e:
		sys.exit(1)
