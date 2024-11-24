
class News:

    id:int
    author:int
    title:str
    content:str
    published:bool
    publication_date:str


    def __init__(self,id:int, author:int, title:str, content:str, published:bool, publication_date:str):
        self.id = id
        self.author = author
        self.title = title
        self.content = content
        self.published = published
        self.publication_date = publication_date
        
    def getDados(self) -> dict:
        return {
            'id':self.id,
            'author': self.author,
            'title': self.title,
            'content': self.content,
            'published': self.published,
            'publicatino_date': self.publication_date
        }