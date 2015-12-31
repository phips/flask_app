from app import app
from nose.tools import eq_, ok_, set_trace
from pyquery import PyQuery as pq

test_app = app.test_client()

def test_homepage():
    ret = test_app.get('/')
    eq_(ret.status_code, 200)
    doc = pq(ret.data)
    eq_(doc.find('h1').text(), "Hello World!")

def test_bootstrap_static():
    ret = test_app.get('/')
    eq_(ret.status_code, 200)
    # set_trace()
    ok_("/static/bootstrap/css/bootstrap.min.css" in ret.data)
