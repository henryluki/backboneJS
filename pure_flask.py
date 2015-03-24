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

@app.route('/test')
def test():
	db=data_curd()
	article="'极客公园-GeekPark'"
	data=db.check_article(article)
	return json.dumps(data)

@app.route('/api')
def api():
	db=data_curd()
	data=db.latest_data()
	return json.dumps(data)


@app.route('/36kr')
def check_36():
	article="'36氪 | 关注互联网创业'"
	data=requests.get("http://myreading.sinaapp.com/36kr/?offset=-2")
	# data=models.db_select(article)
	# return render_template('index.html',arr=data.json())
	return json.dumps(data.json())

@app.route('/zhihu')
def check_zhihu():
	article="'知乎日报'"
	data=requests.get("http://myreading.sinaapp.com/zdaily/?offset=0")
	# data=models.db_select(article)
	return render_template('index.html',arr=data.json())
if __name__ == '__main__':
	app.run(debug=True)
