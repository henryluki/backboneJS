import feedparser,time
from multiprocessing.dummy import Pool as ThreadPool 
from models import DB_sqlite3

_urls=[]
# _urls.append('http://36kr.com/feed')#1h
# _urls.append('http://www.fotofeel.com/rss')#2
# _urls.append('http://www.huxiu.com/rss/4.xml')#3
# _urls.append('http://www.douban.com/feed/review/book')#4
# _urls.append('http://jiaren.org/feed/')#5
# _urls.append('http://www.geekpark.net/rss')#6
# _urls.append('http://www.yp136.com/feed')#7
# _urls.append('http://www.guokr.com/rss/')#guokr
# _urls.append('http://www.qiushibaike.com/hot/rss')#qiubai
# _urls.append('http://onehd.herokuapp.com/')#one
# _urls.append('http://meiwenrishang.com/rss')#meiwen
_urls.append('http://yikerss.miantiao.me/rss')#douban

def time_it(func):
	'''This decorator is for timing a program'''
	def wrapper(*s):
		start=time.time()
		#put the tested function here 
		func(*s)
		end=time.time()
		print 'run time:',end-start
	return wrapper


class for_loop(object):
	"""docstring for for_loop"""
	def __init__(self):
		super(for_loop, self).__init__()
		self.db=DB_sqlite3()

	@time_it
	def run_loop(self):
		db=self.db
		for url in _urls:
			feed=feedparser.parse(url)
			contents=[]
			items=feed.entries
			for e in items:
				content=''
				time=''
				descr=''
		        # description and content issue 
				if 'content' in e and 'summary' in e:
					descr=e.summary
					content=e.content[0].value
				elif 'summary' not in e:
					content=e.content[0].value
				else:
					descr=e.summary
				# updated and published issue
				time=''
				if 'published' in e:
					time=e.published
				else:
					time=e.updated
				#insert into the database
				contents=[feed.feed.title,e.title,e.link,time,descr,content]
				db.insert_db(contents)

	
class map_loop(object):
	"""docstring for map_loop"""
	def __init__(self):
		super(map_loop, self).__init__()
		self.db=DB_sqlite3()
	
	@time_it
	def run_loop(self):
		db=self.db
		pool = ThreadPool(4) 
		results=[]
		results=pool.map(feedparser.parse,_urls)
	 	pool.close() 
		pool.join()
		for feed in results:
			contents=[]
			items=feed.entries
			for e in items:
				content=''
				time=''
				descr=''
		        # description and content issue 
				if 'content' in e and 'summary' in e:
					descr=e.summary
					content=e.content[0].value
				elif 'summary' not in e:
					content=e.content[0].value
				else:
					descr=e.summary
				# updated and published issue
				time=''
				if 'published' in e:
					time=e.published
				else:
					time=e.updated
				#insert into the database
				contents=[feed.feed.title,e.title,e.link,time,descr,content]
				db.insert_db(contents)

if __name__ == '__main__':
	# ins_1=for_loop()
	# ins_1.run_loop()
	ins_2=map_loop()
	ins_2.run_loop()

