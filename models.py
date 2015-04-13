#coding: utf-8
import MySQLdb
import sqlite3

class DB_mysql(object):
	"""docstring for DB_mysql"""
	def __init__(self):
		super(DB_mysql, self).__init__()
		self.host="localhost"
		self.user="root"
		self.passwd="1994225317"
		self.db="flask_db"

	def create_db(self):
		with MySQLdb.connect(self.host,self.user,self.passwd,self.db) as db:
			db.execute('''CREATE TABLE article
       			(ID INTEGER PRIMARY KEY AUTO_INCREMENT,
       			 article VARCHAR(50),
       			 title VARCHAR(100),
       			 link VARCHAR(100) UNIQUE,
       			 pubdate VARCHAR(50),
       			 descr TEXT NOT NULL,
       			 content TEXT NOT null
      			 );''')
	
	def insert_db(self,content):
		db=MySQLdb.connect(self.host,self.user,self.passwd,self.db)
		db.set_character_set('utf8')
		cursor=db.cursor()
		try:
			cursor.execute("INSERT IGNORE INTO article (article,title,link,pubdate,descr,content) VALUES (%s,%s,%s,%s,%s,%s)",content)
			db.commit()
		except:
			print "error"
			db.rollback()
		db.close()

	def check_db(self,sql):
		db=MySQLdb.connect(self.host,self.user,self.passwd,self.db)
		db.set_character_set('utf8')
		cursor=db.cursor()
		try:		
			cursor.execute(sql)
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
		except:
			print "error"
		db.close()

class DB_sqlite3(object):
	"""docstring for DB_sqlite3"""
	def __init__(self):
		super(DB_sqlite3, self).__init__()

	def create_db(self):
		with sqlite3.connect("text.db") as conn:
			conn.execute('''CREATE TABLE article
       			(ID INTEGER PRIMARY KEY AUTOINCREMENT,
       			 article VARCHAR(50),
       			 title VARCHAR(100),
       			 link VARCHAR(100) UNIQUE,
       			 pubdate VARCHAR(50),
       			 descr TEXT NOT NULL,
       			 content TEXT NOT null
      			 );''')

	def insert_db(self,content):
		with sqlite3.connect("text.db") as conn:
			conn.execute("INSERT OR IGNORE INTO article (article,title,link,pubdate,descr,content) VALUES (?,?,?,?,?,?)",content)
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
		self.db =DB_mysql()
		
	def latest_data(self):
		sql='''SELECT * FROM article ORDER BY ID DESC LIMIT 6'''
		results=self.db.check_db(sql)
		return results

	def check_article(self,article):
		sql='''SELECT * FROM article WHERE article=%s ORDER BY ID DESC LIMIT 6'''%article
		results=self.db.check_db(sql)
		return results

if __name__ == '__main__':
	'''
	   DB_sqlite3 for sqlite3
	   DB_mysql for MySQLdb
	'''
	# db=DB_sqlite3()
	# db.create_db()

	db=DB_mysql()
	db.create_db()

