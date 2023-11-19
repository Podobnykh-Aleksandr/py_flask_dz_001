from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_migrate import Migrate


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Advertisement(db.Model):
    __tablename__ = 'advertisement'

    advert_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    author = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<advert_id %r>' % self.advert_id

db.create_all()


# Создаем routes
@app.route('/')
def home():
    return ('<h1>«Домашнее задание Flask»</h1> '
            '<h3>Методы [GET, PATCH, DEL]: api/id</h3> '
            '<h3>Метод POST: api/post</h3>')


@app.route('/api/post', methods=['POST'])
def post_advert():
    data = request.json
    ad = Advertisement(title=data.get("title"),
                           description=data.get("description"),
                           author=data.get("author"))
    db.session.add(ad)
    db.session.commit()
    return {'status': 201}


@app.route('/api/<int:ad_id>', methods=['GET'])
def get_advert(ad_id):
    ad = Advertisement.query.filter_by(advert_id=ad_id).first_or_404()
    return {"id": ad.advert_id,
            "title": ad.title,
            "description": ad.description,
            "created": ad.created,
            "author": ad.author
            }, {'status': 200}


@app.route('/api/<int:ad_id>', methods=['PATCH'])
def patch_advert(ad_id):
    data = request.json
    Advertisement.query.filter_by(advert_id=ad_id).update(data)
    db.session.commit()
    new_ad = Advertisement.query.filter_by(advert_id=ad_id).first_or_404()
    return {"id": new_ad.advert_id,
            "title": new_ad.title,
            "description": new_ad.description,
            "created": new_ad.created,
            "author": new_ad.author
            }, {'status': 201}


@app.route('/api/<int:ad_id>', methods=['DELETE'])
def delete_advert(ad_id):
    ad = Advertisement.query.filter_by(advert_id=ad_id).first_or_404()
    db.session.delete(ad)
    db.session.commit()
    return {'status': 200}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
