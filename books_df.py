from utils.data_loader import load_books

class BookDataManager:
    def __init__(self):
        self.df = load_books()

    def get_all_books(self):
        return self.df.to_dict(orient='records')