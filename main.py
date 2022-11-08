def define_matrix(SInputFile):  # заполнение массива числами из файла

    a = []
    isf = 0

    with open(SInputFile) as f:
        while True:
            try:
                s = f.readline()  # считываем символ

                if not s:  # выходим, если конец
                    break

                s = s.split()

                if isf == 0:
                    n = int(s[0])
                    isf += 1
                else:
                    for i in range(0, len(s)):
                        a.append(int(s[i]))

            except ValueError:
                print("Error: bad value.")
                return [-1, n]
            except FileNotFoundError:
                print("Error: file not found.")
                return [-1, n]

    if (len(a) % (n * n)) != 0:
        print("Error: matrix not squared.")
        return [-1, n]

    return [a, n]


def print_matrix(a, n):

    for i in range(len(a)):
        print(a[i], end = " ")
        if (i + 1) % n == 0:
            print()

    print()


def change_last_and_first(a, n):

    for i in range(n):  # дублирую первую строку матр.
        a.append(a[i])

    # print_matrix(a, n)

    j = 0
    for i in range(n * n - n, n * n):  # вставляю значения предпоследней строки в первую
        a[j] = a[i]
        j += 1

    # print_matrix(a, n)

    for i in range(n * n - 1, n * n - n - 1, -1):  # удаляю последнюю строку
        a.pop(i)

    # print_matrix(a, n)

    return a



def main():

    [arr, n] = define_matrix("1.txt")

    if isinstance(arr, int):
        print("Error: no correct data.")
    else:
        print("-------------------")
        print("The original array:")
        print_matrix(arr, n)
        print("-------------------")

        change_last_and_first(arr, n)

        print("--------------")
        print("Changed matrix:")
        print_matrix(arr, n)
        print("--------------")

    return 0


main()