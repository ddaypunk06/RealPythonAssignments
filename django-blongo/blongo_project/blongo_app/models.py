from mongoengine import Document, StringField, DateTimeField
import datetime

# Create your models here.

class Post(Document):
	title = StringField(max_length=200, required=True)
	content = StringField(required=True)
	date_published= DateTimeField(default=datetime.datetime.now, required=True)