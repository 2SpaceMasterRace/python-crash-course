from typing import List


def preprocess_data() -> None:
    complete_list: List[List[str]] = []
    int_list: List[List[int]] = []
    coloumn_1: List[int] = []
    coloumn_2: List[int] = []

    with open("input.txt", "r", encoding="utf-8") as f:
        complete_list: List[str] = [line.split() for line in f]

    int_list = [list(map(int, row)) for row in complete_list]

    # turn this to list comphrehension
    for row in int_list:
        coloumn_1.append(row[0])
        coloumn_2.append(row[1])

    coloumn_1.sort()
    coloumn_2.sort()

    subtract_list = [abs(id_2 - id_1) for id_1, id_2 in zip(coloumn_1, coloumn_2)]
    print(sum(subtract_list))
