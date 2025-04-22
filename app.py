from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Bíblia Sagrada',
        'author': 'Philip C. Almond'
    },
    {
        'id': 2,
        'title': 'Harry Potter e a Pedra Filosofal',
        'author': 'J.K Howling'
    },
    {
        'id': 3,
        'title': 'The Invention of Hugo Cabret',
        'author': 'Brian Selznick'
    },
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/books/<int:id>', methods=['GET'])
def get_bookById(id):
    for book in books:
       if book.get('id') == id:
           return jsonify(book)
           

@app.route('/books/<int:id>', methods=['PUT'])
def edit_bookById(id):
    edited_book = request.get_json()
    for index,book in enumerate(books):
        if book.get('id') == id:
            books[index].update(edited_book)
            return jsonify(books[index])


@app.route('/books', methods=['POST'])
def add_newBook():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_books(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
            
        return jsonify(books)

app.run(port=5000,host='localhost',debug=True)