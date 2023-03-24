# Initiating app instance with flask
import flask, csv
app = flask.Flask("Bibliothèqa")

# Class definition
class Book:

    # Constructor and Properties definition
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Methods definition
    # Func: adding books
    def add_book(self):
        csv_file = open('books.csv', 'a', newline='')
        book_writer = csv.writer(csv_file, delimiter='\t')
        book_writer.writerow([self.title,self.author])
        csv_file.close()


    # Func: deleting books
    def delete_book(self):
        books = get_books()
        csv_file = open('books.csv', 'w', newline='')
        book_writer = csv.writer(csv_file, delimiter='\t')
        
        for book in books:
            if book[0].lower().find(self.title.lower()) == -1 or book[1].lower().find(self.author.lower()) == -1:
                book_writer.writerow(book)
        
        csv_file.close()


# Setup of functions
# Func: read html pages
def get_html(page_name):
    html_file = open("templates/" + page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

# Func: read books from database file
def get_books():
    books_list_titled = []
    csv_file = open('books.csv', 'r', newline='')
    book_reader = csv.reader(csv_file, delimiter='\t')
    for line in book_reader:
        books_list_titled.append(line)
    csv_file.close()
    return books_list_titled


# Setup of index route
@app.route("/")
def home():
    html_file = get_html("index")
    return html_file 


# Setup of Login route
@app.route('/login')
def login():
    html_file = get_html("login")
    return html_file 


# Setup of filter page route
@app.route("/filter")
def filter_books():
    html_file = get_html("filter")
    return html_file

# Setup of add-book route
@app.route("/add_book", methods=['GET','POST'])
def add__book():
    html_file = get_html("add_book")
    if flask.request.method == 'POST':
        book_title = flask.request.form['book_title'].strip()
        book_author = flask.request.form['book_author'].strip()
        if book_title != "" and book_author != "":

            new_book = Book(book_title, book_author)             
            new_book.add_book()
            
            return html_file.replace("<br>", "<h4>Book is added successfully!</h4>")
        
        elif book_title.strip() == "" and book_author.strip() == "":
            return html_file.replace("enter a book title...", "Field is required!").replace("enter the author name...", "Field is required!")
        
        elif book_title.strip() == "":
            return html_file.replace("enter a book title...", "Field is required!")
        
        elif book_author.strip() == "":
            return html_file.replace("enter the author name...", "Field is required!")
        
    return html_file

# Setup of library_books route
@app.route("/show_books")
def showBooks():
    html_file = get_html("show_books")
    books = get_books()[1:]
    all_books = ""
    books_title = ""
    books_author = ""
    if len(books) > 0:
        for book in books:
            books_title = "<p class=\"text-title\">" + book[0] + "</p>"
            title_value = "<input type=\"hidden\" name=\"title\" value=" + book[0] + ">"
            books_author = "<p class=\"text-body\">" + book[1] +  "</p>"
            author_value = "<input type=\"hidden\" name=\"author\" value=" + book[1] + ">"
            all_books += "<div class=\"card\"><div class=\"card-details\">" + books_title + books_author + "</div><form action=\"/del_book\" method=\"GET\">" + title_value + author_value + "<input type=\"submit\" class=\"card-button\" value=\"Delete\"></form></div>"
    else:
        all_books = "<div class=\"card\"><div class=\"card-details\"><p class=\"text-title\">No books in the library</p></div></div>"   
    return html_file.replace("$$books$$", all_books)


# Setup of search route
@app.route("/search")
def search():
    html_file = get_html("show_books")
    books = get_books()[1:]
    title = flask.request.args.get("title").strip()
    author = flask.request.args.get("author").strip()
    found_books = ""
    books_title = ""
    books_author = ""
    if title != "" or author != "":
        for book in books:
            if book[0].lower().find(title.lower()) != -1 and book[1].lower().find(author.lower()) != -1:
                books_title = "<p class=\"text-title\">" + book[0] +  "</p>"
                title_value = "<input type=\"hidden\" name=\"title\" value=" + book[0] + ">"
                books_author = "<p class=\"text-body\">" + book[1] +  "</p>"
                author_value = "<input type=\"hidden\" name=\"author\" value=" + book[1] + ">"
                found_books += "<div class=\"card\"><div class=\"card-details\">" + books_title + books_author + "</div><form action=\"/del_book\" method=\"GET\">" + title_value + author_value + "<input type=\"submit\" class=\"card-button\" value=\"Delete\"></form></div>"

    if found_books == "":
        found_books = "<div class=\"card\"><div class=\"card-details\"><p class=\"text-title\">No result found</p></div></div>"
    return html_file.replace("$$books$$", found_books)


# Setup of delete route
@app.route("/del_book", methods=['GET','POST'])
def delete():
    title = flask.request.args.get("title").strip()
    author = flask.request.args.get("author").strip()

    new_book = Book(title, author)    
    new_book.delete_book()

    return flask.redirect("/show_books")