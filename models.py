from __init__ import db


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    articles = db.relationship('Article', backref='subject', lazy=True)

    def __repr__(self):
        return f'<Subject {self.name}>'


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True, nullable=False)
    subject_id = db.Column(
        db.Integer, db.ForeignKey('subject.id'), index=True, nullable=False
    )
    text_file = db.Column(db.String(128))
    exercises = db.relationship('Exercise', backref='article', lazy=True)

    def __repr__(self):
        return f'<Article {self.name} from {self.subject.name} subject>'


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(
        db.Integer, db.ForeignKey('article.id'), index=True, nullable=False
    )
    text = db.Column(db.String(128))

    def __repr__(self):
        return f'<Exercise {self.id} from {self.article.name}>'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(162))#PBKDF2, SHA-256
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
