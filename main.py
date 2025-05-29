"""Sistema de Gestión de Calificaciones de Estudiantes."""


class Student:
    """Representa a un estudiante con sus calificaciones."""

    def __init__(self, student_id, name):
        if not student_id.strip():
            raise ValueError("El ID del estudiante no puede estar vacío.")
        if not name.strip():
            raise ValueError("El nombre del estudiante no puede estar vacío.")
        self.id = student_id.strip()
        self.name = name.strip()
        self.grades = []
        self.average = 0.0
        self.letter_grade = "N/A"
        self.status = "Failed"
        self.honor_roll = "No"

    def add_grade(self, grade):
        """Agrega una calificación si es válida."""
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(float(grade))
            print(f"Calificación {grade} añadida.")
        else:
            print(f"Calificación inválida '{grade}'. Debe ser un número entre 0 y 100.")

    def calc_average(self):
        """Calcula el promedio y actualiza atributos relacionados."""
        if not self.grades:
            self.average = 0.0
            self.letter_grade = "N/A"
            self.status = "Failed"
            self.honor_roll = "No"
            return self.average

        self.average = sum(self.grades) / len(self.grades)

        # Asignar calificación en letras
        if self.average >= 90:
            self.letter_grade = "A"
            self.honor_roll = "Yes"
        elif self.average >= 80:
            self.letter_grade = "B"
            self.honor_roll = "No"
        elif self.average >= 70:
            self.letter_grade = "C"
            self.honor_roll = "No"
        elif self.average >= 60:
            self.letter_grade = "D"
            self.honor_roll = "No"
        else:
            self.letter_grade = "F"
            self.honor_roll = "No"

        # Estado de aprobación
        self.status = "Passed" if self.average >= 60 else "Failed"
        return self.average

    def remove_grade_by_value(self, value):
        """Elimina la primera ocurrencia de una calificación específica."""
        try:
            self.grades.remove(float(value))
            print(f"Calificación {value} eliminada.")
        except ValueError:
            print(f"Calificación {value} no encontrada.")

    def remove_grade_by_index(self, index):
        """Elimina una calificación según su índice."""
        try:
            removed = self.grades.pop(index)
            print(f"Calificación en posición {index} eliminada: {removed}")
        except IndexError:
            print(f"Índice {index} fuera de rango.")

    def summary_report(self):
        """Devuelve el resumen del estudiante como string."""
        self.calc_average()
        report = (
            f"===== RESUMEN DEL ESTUDIANTE =====\n"
            f"ID: {self.id}\n"
            f"Nombre: {self.name}\n"
            f"Total de Calificaciones: {len(self.grades)}\n"
            f"Promedio: {round(self.average, 2)}\n"
            f"Calificación Letra: {self.letter_grade}\n"
            f"Estado: {self.status}\n"
            f"Honor Roll: {self.honor_roll}\n"
            f"=================================="
        )
        return report




def main():
    """Funcion main"""
    try:
        student = Student("001", "Ana Pérez")
        student.add_grade(95)
        student.add_grade(87)
        student.add_grade(74.5)
        student.add_grade(-10)     # Inválido
        student.add_grade(102)     # Inválido
        # Eliminar una calificación por índice y valor
        student.remove_grade_by_index(2)
        student.remove_grade_by_value(999)  # No existe
        # Imprimir el resumen
        print("\n" + student.summary_report())

    except ValueError as ve:
        print(f"Error al crear estudiante: {ve}")


if __name__ == "__main__":
    main()
