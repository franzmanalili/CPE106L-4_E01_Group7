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
    students = [
        Student("Ken", 5),
        Student("Charlie", 5),
        Student("Alice", 5),
        Student("Eve", 5),
        Student("Bob", 5)
    ]

    # Assign scores to each student for demonstration purposes
    scores = [
        [100, 90, 80, 70, 60],
        [85, 95, 75, 65, 55],
        [78, 88, 98, 68, 58],
        [90, 85, 80, 75, 70],
        [95, 85, 75, 65, 55]
    ]

    for student, score_list in zip(students, scores):
        for i, score in enumerate(score_list, 1):
            student.setScore(i, score)

    print("Unsorted students:")
    for student in students:
        print(student)

    # Sort the list
    students.sort()
    print("\nSorted students:")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()
