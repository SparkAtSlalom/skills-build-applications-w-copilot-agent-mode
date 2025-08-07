from mongoengine import Document, StringField, EmailField, ReferenceField, ListField, IntField, EmbeddedDocument, EmbeddedDocumentField

class User(Document):
    username = StringField(max_length=100, required=True)
    email = EmailField(unique=True, required=True)
    password = StringField(max_length=100, required=True)

class Team(Document):
    name = StringField(max_length=100, required=True)
    members = ListField(ReferenceField(User))

class Activity(Document):
    user = ReferenceField(User, required=True)
    activity_type = StringField(max_length=100, required=True)
    duration = StringField(required=True)  # Representing duration as a string

class Leaderboard(Document):
    user = ReferenceField(User, required=True)
    score = IntField(required=True)

class Workout(Document):
    name = StringField(max_length=100, required=True)
    description = StringField()