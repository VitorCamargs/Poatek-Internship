def get_average(students: list[tuple[str, int, int]]) -> float:
    """
    Calculates the average height of students in the list

    :param students: List of Tuples (Name, Height, Age)
    :return: Average Height
    """
    age_sum = 0
    for student in students:
        age_sum += student[1]
    average = age_sum / len(students)
    return average


def get_shorter_than(students: list[tuple[str, int, int]], height: float, age: int = 13) -> list[tuple[str, int, int]]:
    """
    Filter the given list of students returning only the ones that are over the age and shorter than average

    :param students: List of Tuples (Name, Height, Age)
    :param height: Average Height of the list
    :param age: Minimum age, fixed at 13
    :return: Filtered list of students
    """
    shorter = []
    shorter.extend([student for student in students if (student[2] > age and student[1] < height)])
    return shorter


if __name__ == '__main__':
    students_list = [('Bruno', 170, 14), ('Leonardo', 174, 21), ('Juan', 156, 12), ('Juliana', 166, 13), ('Wagner',
                                                                                                          184, 17),
                     ('Micaela', 172, 18), ('Bento', 150, 14), ('Lucia', 162, 13), ('Pedro', 169, 14), ('Carla',
                                                                                                        158, 16)]

    height_average = get_average(students_list)
    shorter_than = get_shorter_than(students_list, height_average)
    number_of_students_shorter = len(shorter_than)

    print(f'There are {number_of_students_shorter} students over the age of 13 shorter than the average ({height_average}):\n {shorter_than}')
