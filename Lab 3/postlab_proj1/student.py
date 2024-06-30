"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __eq__(self, other):
        """Tests for equality."""
        return self.name == other.name

    def __lt__(self, other):
        """Tests for less than."""
        return self.name < other.name

    def __ge__(self, other):
        """Tests for greater than or equal to."""
        return self.name >= other.name

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    student1 = Student("Ken", 5)
    student2 = Student("Alice", 5)
    student3 = Student("Ken", 5)

    print("Testing equality (Ken == Ken):", student1 == student3)
    print("Testing less than (Alice < Ken):", student2 < student1)
    print("Testing greater than or equal to (Ken >= Alice):", student1 >= student2)

    for i in range(1, 6):
        student1.setScore(i, 100)
    print(student1)

    for i in range(1, 6):
        student2.setScore(i, 90)
    print(student2)

    for i in range(1, 6):
        student3.setScore(i, 80)
    print(student3)

if __name__ == "__main__":
    main()


