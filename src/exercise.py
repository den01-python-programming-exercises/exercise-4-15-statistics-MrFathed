from statistics import Statistics

def main():
    #write your code below this line
    stats = Statistics()
    evens = Statistics()
    odds = Statistics()

    while True:
        number = int(input())

        if number == -1:
            break

        stats.add_number(number)

        if number % 2 == 0:
            evens.add_number(number)
        else:
            odds.add_number(number)

    print("Sum: " + str(stats.sum))
    print("Sum of even numbers: " + str(evens.sum))
    print("Sum of odd numbers: " + str(odds.sum))

if __name__ == '__main__':
    main()
