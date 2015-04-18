#coding:utf-8

from flask import render_template,jsonify
from model import Article
import requests
from pure_flask import app
app.config.from_object('config')


@app.route('/')
def index():
	return render_template('old.html')

@app.route('/today')
def new():
	return render_template('new.html')

@app.route('/test')
def test():
	db=Article()
	data=db.latest_data()
	return jsonify({'data':data})

@app.route('/latest')
def latest():
	db=Article()
	data=db.latest_data()
	return jsonify({'data':data})

@app.route('/douban')
def douban():
	db=Article()
	article="豆瓣一刻"
	data=db.check_article(article)
	return jsonify({'data':data})

@app.route('/yige')
def api():
	db=Article()
	article="一个-韩寒"
	data=db.check_article(article)
	return jsonify({'data':data})

@app.route('/36kr')
def check_36():
	db=Article()
	article="36氪"
	data=db.check_article(article)
	return jsonify({'data':data})

@app.route('/geekpark')
def geekpark():
	db=Article()
	article="极客公园-GeekPark"
	data=db.check_article(article)
	return jsonify({'data':data})