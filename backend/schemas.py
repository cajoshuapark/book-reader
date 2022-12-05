from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from base import Base

class Page(Base):  
    __tablename__ = 'pages'
    id = Column(Integer, primary_key= True)
    pagenum = Column(Integer)
    content = Column(String)
    bookId = Column(Integer, ForeignKey('books.id'))
    #represents a one to one relationship
    book = relationship("Book",  backref=backref("page", uselist=False))
    # self is the instance of the object itself. Similar to this-> in c++
    #init is the constructor for the class. 
    #gets called after memory is allocated for the object
    def __init__(self, pagenum, content, book):
        #stores for lifetime of the object.
        #if I did _pagenum = pagenum, var would be stored on stack
        self.pagenum = pagenum
        self.content = content
        self.book = book

class Book(Base):  
    __tablename__ = 'books'
    id = Column(Integer, primary_key= True)
    title = Column(String)
    def __init__(self, title):
        self.title = title

class Chapter(Base): 
    __tablename__ = 'chapters'
    id = Column(Integer, primary_key= True)
    num = Column(Integer)
    bookId = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book",  backref=backref("chapter", uselist=False))
    startPage = Column(Integer, ForeignKey('pages.id'))
    page = relationship("Page",  backref=backref("chapter", uselist=False))
    def __init__(self, num, book, page):
        self.num = num
        self.book = book
        self.page = page
