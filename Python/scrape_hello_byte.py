from bs4 import BeautifulSoup
import base64
import pickle
import requests

class Rube(object):
    def __init__(self, *args, **kwargs):
        url = 'gANYGgAAAGh0dHBzOi8vanVzdHBhc3RlLml0LzdxeDZ5cQAu\n'
        self.url = pickle.loads(base64.decodebytes(url.encode('utf-8')))
        self.response = self.get_source(self.url)
        self.content = "gANYAQAAAEhxAC4=\ngANYAQAAAGVxAC4=\ngANYAQAAAGxxAC4=\ngANYAQAAAGxxAC4=\ngANYAQAAAG9xAC4=\ngANYAQAAACBxAC4=\ngANYAQAAAFdxAC4=\ngANYAQAAAG9xAC4=\ngANYAQAAAHJxAC4=\ngANYAQAAAGxxAC4=\ngANYAQAAAGRxAC4=\ngANYAQAAACFxAC4=\n"
    
    def get_source(self, url=None):
        if url:
            return requests.get(url)
        else:
            return requests.get(self.url)
    
    def scrape_url_string(self):
        soup = BeautifulSoup(self.response.text, "html.parser")
        content = soup.find('div', {'id': 'articleContent'}).find('div').text.strip()
        pickel_content = [base64.decodebytes(i.encode('utf-8')) for i in content.split('\\n') if i]
        string = ''
        for index, item in enumerate(pickel_content):
            string += pickle.loads(item)
        return string

    def decode_direct(self):
        pickel_content = [base64.decodebytes(i.encode('utf-8')) for i in self.content.split('\n') if i]
        string = ''
        for index, item in enumerate(pickel_content):
            string += pickle.loads(item)
        return string

if __name__ == "__main__":
    rube = Rube()
    if rube.response.status_code == 200:
        stat = rube.scrape_url_string()
    else:
        stat = rube.decode_direct()
    print(stat)

    


