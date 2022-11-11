def define_matrix(SInputFile):  # заполнение массива числами из файла

    a = []
    isf = 0
    try:
        with open(SInputFile) as f:
            while True:
                s = f.readline()  # считываем символ

                if not s:  # выходим, если конец
                    break

                s = s.split()

                if isf == 0:
                    n = int(s[0])
                    isf += 1

                for i in range(0, len(s)):
                    if isf == 1:
                        isf += 1
                        continue
                    a.append(int(s[i]))

    except ValueError:
        print("Error: bad value.")
        f.close()
        return [-1, 0]

    except FileNotFoundError:
        print("Error: file not found.")
        return [-1, 0]

    if isf == 0:
        print("Error: file is empty.")
        return[-1, 0]

    if n <= 0:
        print("Error: n <= 0.")
        return [-1, n]

    if len(a) == 0:
        print("Error: matrix is empty.")
        return [-1, n]

    if (len(a) % (n * n)) != 0:
        print("Error: matrix not squared.")
        return [-1, n]

    if n * n != len(a):
        print("Error: no correct data - n * n != len(a)")
        return [-1, n]

    return [a, n]


def print_matrix(a, n):

    for i in range(len(a)):
        print(a[i], end = " ")
        if (i + 1) % n == 0:
            print()

    print()


def change_last_and_first(a, n):

    for i in range(n):
        tmp = a[i]
        a[i] = a[n * n - n + i]
        a[n * n - n + i] = tmp

    return a



def main():

    [arr, n] = define_matrix("1.txt")

    if not isinstance(arr, int):
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