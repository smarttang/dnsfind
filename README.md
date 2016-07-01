# DnsFind 域名穷举工具

[![Python 2.6|2.7](https://img.shields.io/badge/python-2.6|2.7-yellow.svg)](https://www.python.org/)
[![build|passing](https://img.shields.io/appveyor/ci/gruntjs/grunt/master.svg)](#)

```
    ____             _______           __
   / __ \____  _____/ ____(_)___  ____/ /
  / / / / __ \/ ___/ /_  / / __ \/ __  / 
 / /_/ / / / (__  ) __/ / / / / / /_/ /  
/_____/_/ /_/____/_/   /_/_/ /_/\__,_/ 

          Author: Smarttang && Ver: V1.1
```

###前言
---
平常经常需要穷举某些特殊的站点踩点，用了很多东西都不太顺手，所以开发了这个东西，平常可以自己离线扫下。字典是结合别人的去重后弄出来的，增加了关键字筛选，方便找目录可浏览漏洞，同时方便识别WEB服务。差个webservice，后面补上。web service主要是用于分布式扫描用，等有时间加，先凑合用着。(PS: 自己给自己的生日礼物)

###功能列表
---
1. dns子域名穷举。
2. 定制网站关键字筛选。
3. 自动识别 Web Server 指纹。

###目录结构
---
目录结构基本上比较清晰，命名规范都比较标准，目的在于长久使用和维护。

```
├── core
│   ├── __init__.py
│   ├── config.py
│   ├── dnsfind.py
│   └── utils.py
├── dict
│   └── domain.txt
└── run.py
```

### Console Service:
---
Console版本主要用于测试和脱机使用，应用场景在于自身特殊的应用，比如单兵作战，我需要单独的扫描目标直接输出结果。在对参数不了解时，可以help一下。：）

```
    console: python run.py -h
```

```
    ____             _______           __
   / __ \____  _____/ ____(_)___  ____/ /
  / / / / __ \/ ___/ /_  / / __ \/ __  / 
 / /_/ / / / (__  ) __/ / / / / / /_/ /  
/_____/_/ /_/____/_/   /_/_/ /_/\__,_/ 

          Author: Smarttang && Ver: V1.1
  
Usage: run.py [options]

Options:
  -h, --help            show this help message and exit
  -u TARGET, --target=TARGET
                        set domain.(simple: baidu.com)
  -t THREADS_COUNT, --threads=THREADS_COUNT
                        threads count.(default 10)
  -s TIMEOUT, --timeout=TIMEOUT
                        set timeout of requests.(default 5s)
  -d DICTNAME, --dictname=DICTNAME
                        choice dicts.(default All)
  -f, --finger          choice finger on/off.(default False)
  -k KEYWORDS, --keywords=KEYWORDS
                        set keywords.(default None)
```

常规的命令执行诸如以下，执行子域名穷举。：

```
    console: python run.py -u baidu.com -t 30 -s 5 --finger --keywords welcome,nginx,apache,index,of
```

###依赖包
---
* gevent
* optparse
* requests

