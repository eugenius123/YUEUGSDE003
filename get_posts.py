import requests
from contextlib import closing
from bs4 import BeautifulSoup
import json


def get_posts_in_json():
    """
    Visits expedia's FB page using BeautifulSoup as HTML
    """
    raw_html = simple_get('https://www.facebook.com/pg/expedia/posts/')
    soup = BeautifulSoup(raw_html, 'html.parser')
    posts = soup.find_all('div', attrs={"class":"userContentWrapper"})
    post_list = []
    for post in posts[:8]:
        time = post.find('abbr')['title']
        page = post.find('p').getText()
        post_list.append({"date":time,"post":page})
    with open('./output.txt', 'w') as outfile:
        json.dump({"posts":post_list}, outfile)
    print("all posts successfully dumped in output.txt in same folder")
    return post_list
def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(requests.get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except requests.RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

#get_posts_in_json()
