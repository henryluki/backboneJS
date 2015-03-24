# encoding: utf-8
from flask import Flask
from flask import render_template
import requests
from models import data_curd
import json

app=Flask(__name__)
@app.route('/')
def index():
	return render_template('new.html')

@app.route('/latest')
def latest():
	db=data_curd()
	data=db.latest_data()
	return json.dumps(data)

@app.route('/douban')
def test():
	db=data_curd()
	article="'豆瓣一刻'"
	data=db.check_article(article)
	return json.dumps(data)

@app.route('/yige')
def api():
	db=data_curd()
	article="'一个-韩寒'"
	data=db.check_article(article)
	return json.dumps(data)

@app.route('/36kr')
def check_36():
	db=data_curd()
	article="'36氪 | 关注互联网创业'"
	data=db.check_article(article)
	return json.dumps(data)

@app.route('/geekpark')
def geekpark():
	db=data_curd()
	article="'极客公园-GeekPark'"
	data=db.check_article(article)
	return json.dumps(data)

if __name__ == '__main__':
	app.run(debug=True)
