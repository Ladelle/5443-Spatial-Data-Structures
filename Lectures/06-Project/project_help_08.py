from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)


class BooksData():
    def __init__(self):
        with open('books.json','r') as f:
            data = f.read()

        self.books_dict = json.loads(data)

    def getByIsbn(self,isbn=None):
        for book in self.books_dict:
            if book['isbn'] == isbn:
                return book

        return None

    def getCategories(self):
        categories = []
        for book in self.books_dict:
            for cat in book['categories']:
                if not cat in categories:
                    categories.append(cat)

        return categories

    def getByPageCount(self,start=0,end=9000,filter=[]):
        results = []
        for book in self.books_dict:
            if book['pageCount'] >= int(start) and book['pageCount'] < int(end):
                if len(filter) == 0:
                    results.append(book)
                else:
                    newbook = {}
                    for k,v in book.items():
                        if k in filter:
                            newbook[k] = v
                    results.append(newbook)
                        
        return results


books = BooksData()

@app.route('/')
def index():
    print(request.args)
    return '<h1>Answer From A Route</h1>'


@app.route('/book/<string:isbn>')
def book(isbn):
    global books
    count = 0
    success = True

    data = books.getByIsbn(isbn)

    return handle_response(data)

@app.route('/categories/')
def categories():
    global books
    count = 0
    success = True

    data = books.getCategories()

    return handle_response(data)

@app.route('/pages/')
def pages():
    global books
    count = 0
    success = True

    start = request.args.get('start',0)
    end  = request.args.get('end',9000)

    filter = ["title","isbn","thumbnailUrl","shortDescription","pageCount"]

    data = books.getByPageCount(start,end,filter)

    return handle_response(data)


def handle_response(data,error=None):
    success = True
    count = len(data)
    
    result = {"success":success,"count":count,"results":data}

    if error:
        success = False
        result['error'] = error
    
    
    return jsonify(result)



if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080,debug=True)
