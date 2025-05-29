"""Este módulo define la clase Student y una función de prueba."""

class Student:
    """Define la creación del objeto estudiante."""

    def __init__(self, identificacion, name):
        self.id = identificacion
        self.name = name
        self.grades = []
        self.average = 0.0
        self.is_passed = "NO"
        self.honor = "?"

    def add_grade(self, grade):
        """Agrega una nota al estudiante."""
        self.grades.append(grade)

    def calc_average(self):
        """Calcula el promedio del estudiante."""
        if not self.grades:
            self.average = 0
        else:
            self.average = sum(self.grades) / len(self.grades)
        return self.average

    def check_honor(self):
        """Determina si el estudiante es de honor."""
        if self.average > 90:
            self.honor = "Sí"
        else:
            self.honor = "No"

    def delete_grade(self, index):
        """Elimina una nota del estudiante si el índice es válido."""
        if 0 <= index < len(self.grades):
            del self.grades[index]

    def report(self):
        """Muestra el informe del estudiante."""
        print("ID:", self.id)
        print("Nombre:", self.name)
        print("Número de notas:", len(self.grades))
        print("Promedio final:", round(self.average, 2))
        print("Honor:", self.honor)


def startrun():
    """Ejecuta el inicio de la aplicación."""
    a = Student("1", "Juan")
    a.add_grade(100)
    a.add_grade(50)
    a.calc_average()
    a.check_honor()
    a.delete_grade(1)  # Verificado en delete_grade
    a.report()
