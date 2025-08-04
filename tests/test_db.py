

import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):

        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):

        test_db.drop_tables(MODELS)

        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name = 'John Doe', email = 'john@exapmle.com', content = 'Hello world, I\'m John!')
        assert(first_post.id == 1)
        second_post = TimelinePost.create(name = 'Jane doe', email = 'jane@exapmle.com', content = 'Hello world, I\'m Jane!')
        assert(second_post.id == 2)
       
        # get all timeline posts
        # Hint: Use TimelinePost.select() to get all records
        all_posts = TimelinePost.select()
        
        # Convert to list and check count
        posts_list = list(all_posts)
        assert(len(posts_list) == 2)
        
        # Check the first post
        assert(posts_list[0].name == 'John Doe')
        assert(posts_list[0].email == 'john@exapmle.com')
        
        # Check the second post
        assert(posts_list[1].name == 'Jane doe')
        

