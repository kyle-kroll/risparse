class Author:
    def __init__(self):
        self.lastname = ""
        self.firstname = ""
        self.middlename = ""
        self.affiliations = []
    
    def __repr__(self):
        name = f"{self.lastname}, {self.firstname} {self.middlename}"
        return name.strip()