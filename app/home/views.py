from flask import render_template, make_response
from flask_restful import Api, Resource,fields,marshal_with

from app import db
from app.models import User, Article, Tag
from . import home

api = Api(home)


# 返回html类型
@api.representation('text/html')
def output_html(data, code, headers):
    # 在representation装饰的函数中，必须返回一个Response对象
    resp = make_response(data)
    return resp


class ArticleView(Resource):
    resource_fields = {
        'aritice_title':fields.String(attribute='title'),
        'content':fields.String,
        'author':fields.Nested({
            'username':fields.String,
            'email':fields.String,
        }),
        'tags':fields.List(fields.Nested({
            'id':fields.Integer,
            'name':fields.String
        })),
        'read_count':fields.Integer(default=80)
    }
    @marshal_with(resource_fields)
    def get(self, article_id):
        article = Article.query.get(article_id)
        return article


api.add_resource(ArticleView, '/article/<article_id>/', endpoint='article')


class IndexView(Resource):
    def get(self):
        user = User(username='zhiliao', email='hl163@outlook.com')
        article = Article(title='邪神', content='威武雄壮')
        article.author = user
        tag1 = Tag(name='Java')
        tag2 = Tag(name='Python')
        article.tags.append(tag1)
        article.tags.append(tag2)
        db.session.add(article)
        return render_template('home/index.html')


api.add_resource(IndexView, '/', endpoint='index')
