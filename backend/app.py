from flask import Flask
from queries import fetch_first_page,fetch_next_page
from flask import request

currbook = "null"

app = Flask(__name__)


# routing different web addresses
@app.route('/')
def default():
    return 'Hello'

#gets post request from frontend and sends queried data to frontend in json format
@app.route('/getpage', methods = ['POST'])
def get_first_page():
    global currbook 
    data = request.json
    if data:
        fetched_first_page = fetch_first_page(data)
        print(fetched_first_page)    
        ret = {
            "title": fetched_first_page.book.title,
            "pagenum": fetched_first_page.pagenum,
            "content": fetched_first_page.content
        }
        currbook = fetched_first_page.book.title
        return ret
    return "no input"

@app.route('/nextpage', methods = ['POST'])
def get_next_page():
    global currbook 
    data = request.json
    if data:
        fetched_next_page = fetch_next_page(currbook, data)
        print(fetched_next_page)    
        ret = {
            "title": fetched_next_page.book.title,
            "pagenum": fetched_next_page.pagenum,
            "content": fetched_next_page.content
        }
        currbook = fetched_next_page.book.title
        return ret
    return "no input"

if __name__ == "__main__":
    app.run(debug = True)
    # updates the page in real time


#ABOUT FLASK
#is a WGSI ( Web Server Gateway Interface is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python)