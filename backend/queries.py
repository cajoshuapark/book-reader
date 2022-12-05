from schemas import Book, Page, Chapter
from base import session

def fetch_book(tname):
    books = session.query(Book).filter(Book.title == tname).all()
    return books[0].id


def fetch_first_page(tname):
    pages = session.query(Page).join(Book).filter(Book.title == tname, Page.pagenum == 1).all()
    return pages[0]

def fetch_next_page(tname, pnum):
    pages = session.query(Page).join(Book).filter(Book.title == tname, Page.pagenum == pnum).all()
    return pages[0]


#fetch page
def fetch_chapter_page(cnum, bid):
    pages = session.query(Page).join(Chapter).join(Book).filter(
        Chapter.num == cnum, Book.id == bid, Chapter.startPage == Page.id
    ).all()
    return pages[0]

#fetch chapters
# def fetch_chapter(bid):
#     chapters = session.query(Chapter).join(Book).filter(Book.id == bid).all()
#     return chapters

# create a mpa and cycle through contents and fill out map