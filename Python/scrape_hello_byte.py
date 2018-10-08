#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Gahan Saraiya
GiT: https://github.com/gahan9
StackOverflow: https://stackoverflow.com/users/story/7664524

The Complex Steps:
- initialize class
    - gets source content from url
- check response status
    - if 200 OK then scrape web page to get byte text
    - otherwise work on local default
- decode bytes >to>> pickle object >to>> string/result
- decoded result is expected string "Hello World!"
"""
from bs4 import BeautifulSoup
import base64
import pickle
import requests


class Rube(object):
    def __init__(self, *args, **kwargs):
        url = 'gANYGgAAAGh0dHBzOi8vanVzdHBhc3RlLml0LzdxeDZ5cQAu\n'  # pickled url encoded in base64
        self.url = pickle.loads(base64.decodebytes(url.encode('utf-8')))  # load url
        self.response = self.get_source(self.url)  # get content from source
        self.content = "gANYAQAAAEhxAC4=\ngANYAQAAAGVxAC4=\ngANYAQAAAGxxAC4=\ngANYAQAAAGxxAC4=\ngANYAQAAAG9xAC4=\ngANYAQAAACBxAC4=\ngANYAQAAAFdxAC4=\ngANYAQAAAG9xAC4=\ngANYAQAAAHJxAC4=\ngANYAQAAAGxxAC4=\ngANYAQAAAGRxAC4=\ngANYAQAAACFxAC4=\n"
    
    def get_source(self, url=None):
        if url:
            return requests.get(url)
        else:
            return requests.get(self.url)
    
    def scrape_url_string(self):
        soup = BeautifulSoup(self.response.text, "html.parser")  # parse html content
        content = soup.find('div', {'id': 'articleContent'}).find('div').text.strip()  # get text
        pickle_content = [base64.decodebytes(i.encode('utf-8')) for i in content.split('\\n') if i]  # load text pickle
        string = ''
        for index, item in enumerate(pickle_content):
            string += pickle.loads(item)
        return string

    def decode_direct(self):
        pickle_content = [base64.decodebytes(i.encode('utf-8')) for i in self.content.split('\n') if i]
        string = ''
        for index, item in enumerate(pickle_content):
            string += pickle.loads(item)
        return string


if __name__ == "__main__":
    rube = Rube()  # create class instance to get file
    if rube.response.status_code == 200:
        stat = rube.scrape_url_string()
    else:
        stat = rube.decode_direct()
    print(stat)

    


