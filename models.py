#coding: utf-8
import MySQLdb
import sqlite3

class DB_mysql(object):
	"""docstring for DB_mysql"""
	def __init__(self):
		super(DB_mysql, self).__init__()
		
	def db_select(self,article):
		#连接数据库 传入sql语句
		article=article
		with MySQLdb.connect(host="localhost",user="root",passwd="1994225317",db="django",charset="utf8") as db:
			cursor=db
			data=[]
			query="SELECT id,title,link,pubdate,brief,descr,content FROM rss_article WHERE article=%s ORDER BY pubdate DESC LIMIT 0,10" %(article)
			# query="SELECT * FROM rss_article WHERE WHERE article=%s ORDER BY pubdate DESC LIMIT 0,10" %(article)
			cursor.execute(query)
			# cursor.execute(" SELECT * FROM rss_article where id=1")
			results=cursor.fetchall()
			for obj in results:
				arr={}
				arr['id']=obj[0]
				arr['title']=obj[1]
				arr['link']=obj[2]
				arr['pubdate']=obj[3]
				arr['brief']=obj[4]
				arr['descr']=obj[5]
				arr['content']=obj[6]
				data.append(arr)
		return data

class DB_sqlite3(object):
	"""docstring for DB_sqlite3"""
	def __init__(self):
		super(DB_sqlite3, self).__init__()

	def create_db(self):
		with sqlite3.connect("text.db") as conn:
			conn.execute('''CREATE TABLE article
       			(ID INTEGER PRIMARY KEY AUTOINCREMENT,
       			 article VARCHAR(50),
       			 title VARCHAR(50),
       			 link VARCHAR(100),
       			 pubdate VARCHAR(50),
       			 descr TEXT NOT NULL,
       			 content TEXT NOT null
      			 );''')

	def insert_db(self,content):
		with sqlite3.connect("text.db") as conn:
			conn.execute("INSERT INTO article (article,title,link,pubdate,descr,content) VALUES (?,?,?,?,?,?)",content)
			conn.commit()

		conn.close()

	def check_db(self,sql):
		with sqlite3.connect("text.db") as conn:
			cursor=conn.execute(sql)
			fetchall=cursor.fetchall()
			data=[]
			for obj in fetchall:
				arr={}
				arr['id']=obj[0]
				arr['article']=obj[1]
				arr['title']=obj[2]
				arr['link']=obj[3]
				arr['pubdate']=obj[4]
				arr['descr']=obj[5]
				arr['content']=obj[6]
				data.append(arr)
			return data

		conn.close()

class data_curd(object):
	"""docstring for show_detail"""
	def __init__(self):
		super(data_curd, self).__init__()
		self.db =DB_sqlite3()
		
	def latest_data(self):
		sql='''SELECT * FROM article ORDER BY pubdate DESC LIMIT 5'''
		results=self.db.check_db(sql)
		return results

	def check_article(self,article):
		sql='''SELECT * FROM article WHERE article=%s ORDER BY pubdate DESC LIMIT 5'''%article
		results=self.db.check_db(sql)
		return results

if __name__ == '__main__':
	# db=DB_sqlite3()
	# db.insert_db()
	# db.create_db()
	data=data_curd()
	results=data.check_data()
	for r in results:
		print r['id']