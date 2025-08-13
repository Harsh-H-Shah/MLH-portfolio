import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # Clean up any existing timeline posts and cache
        with app.app_context():
            from app import TimelinePost
            TimelinePost.delete().execute()
            # try:
            #     cache.delete('timeline_posts')
            # except Exception:
            #     pass  # Cache might not exist in test mode

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Harsh Shah - Home</title>" in html

        # TODO:  Add more tests relating to the home page
        assert "Software Developer Intern" in html
        assert "Aumsat Technologies" in html

        assert "Stony Brook University" in html
        assert "MS in Computer Science" in html

        assert "href=\"/hobbies\"" in html
        assert "href=\"/timeline\"" in html 
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        
        # Handle both possible response formats
        if isinstance(json, dict) and "timeline_posts" in json:
            posts = json["timeline_posts"]
            assert len(posts) == 0
        else:
            assert isinstance(json, list)
            assert len(json) == 0  # Should be empty initially

    # TODO Add more tests relating to the /api/timeline_post GET and POST apis
    def test_timeline_post_api(self):
        post_data ={
            'name' : 'Test User',
            'email' : 'test@example.com',
            'content' : 'This is test post'
        }

        response = self.client.post("/api/timeline_post", data = post_data)
        assert response.status_code == 200

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        json = response.get_json()
        
        # Handle both possible response formats
        if isinstance(json, dict) and "timeline_posts" in json:
            posts = json["timeline_posts"]
        else:
            posts = json
            
        assert len(posts) == 1
        assert posts[0]["name"] == "Test User"
        assert posts[0]["email"] == "test@example.com"
        assert posts[0]["content"] == "This is test post"



    # TODO Add more tests relating to timeline page 
    def test_timeline_page(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text = True)

        assert '<title>' in html
        assert '<form' in html  
        assert 'name="name"' in html 
        assert 'name="email"' in html 
        assert 'name="content"' in html 

        assert 'timeline_post' in html

        hobbies_response = self.client.get("/hobbies")
        assert hobbies_response.status_code == 200 


    def test_malformed_timeline_post(self):
        # POST resquest missing name

        response = self.client.post("/api/timeline_post", data= {
            "email" : "john@example.com", "content":"Hello world, This is John"
        })
        assert response.status_code == 400
        html =  response.get_data(as_text = True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post ("/api/timeline_post", data ={
            "name" : "John Doe", "email" : "john@example.com", "content" : ""
        })
        assert response.status_code == 400 
        html = response.get_data(as_text = True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post ("/api/timeline_post", data ={
            "name" : "John Doe", "email" : "not-an-email", "content" : "Hello World"
        })
        assert response.status_code == 400 
        html = response.get_data(as_text = True)
        assert "Invalid email" in html