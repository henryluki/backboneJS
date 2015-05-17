#coding: utf-8

"""
use flask-sqlalchemy

TABLE------article
FUNCTIONS----latest check read remove


"""
from pure_flask import app
from flask.ext.sqlalchemy import SQLAlchemy
DB=SQLAlchemy(app,use_native_unicode="utf8")

class Article(DB.Model):
	"""docstring for show_detail"""
	ID=DB.Column(DB.Integer(),primary_key=True)
	article=DB.Column(DB.String(50))
	title=DB.Column(DB.String(100))
	link=DB.Column(DB.String(100),unique=True)
	pubdate=DB.Column(DB.String(50))
	descr=DB.Column(DB.Text)
	content=DB.Column(DB.Text)

	def __init__(self):
		super(Article,self).__init__()

	def insert_db(self,arr):
		status=Article.query.filter_by(link=arr['link']).first()
		if not status:
			article=Article()
			article.article=arr['article']
			article.title=arr['title']
			article.link=arr['link']
			article.pubdate=arr['pubdate']
			article.descr=arr['descr']
			article.content=arr['content']
			DB.session.add(article)
			DB.session.commit()

	def latest_data(self):
		arr=Article.query.order_by(Article.ID.desc()).limit(6).all()
		data=[]
		for a in arr:
			temp={
			'id':a.ID,
			'article':a.article,
			'title':a.title,
			'link':a.link,
			'pubdate':a.pubdate,
			'descr':a.descr,
			'content':a.content
			}
			data.append(temp)
		return data

	def check_article(self,article):
		arr=Article.query.filter_by(article=article).order_by(Article.ID.desc()).limit(6).all()
		data=[]
		for a in arr:
			temp={
			'id':a.ID,
			'article':a.article,
			'title':a.title,
			'link':a.link,
			'pubdate':a.pubdate,
			'descr':a.descr,
			'content':a.content
			}
			data.append(temp)
		return data

	def read_article(self,id):
		return Article.query.get(id)


	def remove(self,id):
		obj=Article.query.get(id)
		DB.session.delete(obj)
		DB.session.commit()

if __name__ == '__main__':
	DB.create_all()

