import datetime
from mongoengine import *
db=connect('mongoengine_test', host='localhost', port=27017)
posts = db.Post

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField()



def save_docs():
    post_1 = Post(
    title='Sample Post1',
    content='Some engaging content',
    author='Scott',
    is_published = False
    )
    post_1.save()       # This will perform an insert

def read_docs():
    for post in Post.objects(is_published = True):   
        print(post.title)
        print(post.is_published)


if __name__ == '__main__':
    # save_docs()
    read_docs()
