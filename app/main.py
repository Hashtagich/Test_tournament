from random import shuffle
from time import sleep, time
from typing import Tuple, List, Optional


def read_file_to_list(file_path: str = '../file/tasks.txt') -> List[str]:
    """Открывает текстовый файл и возвращает список строк."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines = [line.strip().capitalize() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


def save_to_txt(list_tasks: List[str], file_name: str = 'Task Top.txt') -> None:
    """Сохраняет данные из переданного списка list_tasks текстовый файл с названием file_name."""
    with open(file_name, 'w', encoding='utf-8') as file:
        for task in list_tasks:
            file.write(task + '\n')


def split_into_pairs(input_list: List[str]) -> List[Tuple[str, Optional[str]]]:
    """Разбивает список на пары."""
    pairs = []
    for ind in range(0, len(input_list), 2):
        if ind + 1 < len(input_list):
            pairs.append((input_list[ind], input_list[ind + 1]))
        else:
            pairs.append((input_list[ind], None))
    return pairs


def battle(num_tour: int, pair: Tuple[str, Optional[str]]) -> None:
    """Проводит битву между парами задач и возвращает победителя."""
    if pair[1] is None:
        new_list.append(pair[0])

    else:
        print(f'\nТур №{num_tour}')
        print("Выберите одну из задач:")
        print(f"1: {pair[0]}")
        print(f"2: {pair[1]}")

        while True:
            choice = input("Введите 1 или 2 для выбора: ")
            if choice in ('1', '2'):
                break
            print("\nНекорректный ввод. Пожалуйста, введите 1 или 2.")

        if choice == '1':
            new_list.append(pair[0])
            top_list.insert(0, pair[1])
        else:
            new_list.append(pair[1])
            top_list.insert(0, pair[0])


if __name__ == "__main__":
    top_list, new_list, ture = [], [], 1
    lines_list = read_file_to_list()
    shuffle(lines_list)
    tasks = split_into_pairs(lines_list)

    print('Добро пожаловать в Test Tournament!\n')
    sleep(1)
    start_time = time()

    while not (len(tasks) == 1 and tasks[0][1] is None):
        new_list = []
        for i in tasks:
            battle(num_tour=ture, pair=i)
            # print('Проверочные данные', f' new_list {new_list}', f' top_list{top_list}', sep='\n')

        shuffle(new_list)
        tasks = split_into_pairs(new_list)
        ture += 1

    top_list.insert(0, new_list[0])
    save_to_txt(file_name='../file/Tasks Top.txt', list_tasks=top_list)

    end_time = time()
    elapsed_time = end_time - start_time

    # Преобразуем время в часы, минуты и секунды
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)

    print('\nБатл завершен')
    print(f'Вы затратили {int(hours)}:{int(minutes):02}:{int(seconds)}')
    print(f"\nОкончательный победитель: {top_list[0]}")
    print('\nТоп лист успешно сохранён в файл "Tasks Top" и представлен ниже.\n')

    for num, item in enumerate(top_list):
        print(f'№{num + 1} - {item}')

    sleep(20)
