from base import session, engine, Base
from schemas import Book, Page, Chapter

# generate database schema
#create all will check if table exists. if not it will create the table
Base.metadata.create_all(engine)

harry_potter = Book(title="Harry Potter")  
session.add(harry_potter)  

brisingr = Book(title="Brisingr")  
session.add(brisingr)  

# add book instance harry_potter to object
p1_1 = Page(
    pagenum=1,
    content= "This is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTERThis is page 1 body for HARRY POTTER", 
    book = harry_potter
)  
session.add(p1_1)  
p1_2 = Page(
    pagenum=2,
    content= "This is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTERThis is page 2 body for HARRY POTTER", 
    book = harry_potter 
)  
session.add(p1_2)  
p1_3 = Page(
    pagenum=3,
    content= "This is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTERThis is page 3 body for HARRY POTTER",
    book =  harry_potter 
)  
session.add(p1_3)  

p2_1 = Page(
    pagenum=1,
    content= "This is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for BrisingrThis is page 1 body for Brisingr", 
    book = brisingr 
)  
session.add(p2_1)  
p2_2 = Page(
    pagenum=2,
    content= "This is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for BrisingrThis is page 2 body for Brisingr", 
    book = brisingr 
)  
session.add(p2_2)  
p2_3 = Page(
    pagenum=3,
    content= "This is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for BrisingrThis is page 3 body for Brisingr", 
    book = brisingr 
)  
session.add(p2_3)  

c1_1 = Chapter(num = 1, book = harry_potter, page = p1_1 )  
session.add(c1_1)  
c1_2 = Chapter(num = 2, book = harry_potter, page = p1_3 )  
session.add(c1_2)  

c2_1 = Chapter(num = 1, book = brisingr, page = p2_1 )  
session.add(c2_1)  
c2_2 = Chapter(num = 2, book = brisingr, page = p2_1 )  
session.add(c2_2)  

session.commit()


#read in data from csv file

