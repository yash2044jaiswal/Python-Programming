class Student:
    def __init__(self, name, marks):
        self.name = name        # public
        self.__marks = marks    # private variable

    def show_marks(self):
        print("Marks:", self.__marks)

    def update_marks(self, new_marks):
        if new_marks >= 0:
            self.__marks = new_marks
        else:
            print("Invalid marks")
