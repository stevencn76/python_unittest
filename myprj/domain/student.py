class Student:
    def __init__(self, id: int, name: str, gender: str = "female"):
        self.id = id
        self.name = name
        self.gender = gender

    def rename(self, new_name: str) -> bool:
        if 3 < len(new_name) < 10:
            self.name = new_name
            return True

        return False

    def valid_name(self) -> bool:
        if self.name:
            return 3 < len(self.name) < 10

        return False

    def valid_gender(self) -> bool:
        return self.gender and self.gender.casefold() in ["male", "female"]
