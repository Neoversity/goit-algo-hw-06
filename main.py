import task1
import task2
import task3

def main():
    while True:
        print("\nВиберіть завдання:")
        print("1. Завдання 1")
        print("2. Завдання 2")
        print("3. Завдання 3")
        print("4. Вихід")
        
        choice = input("Введіть номер завдання: ")

        if choice == "1":
            task1.run()
        elif choice == "2":
            task2.run()
        elif choice == "3":
            task3.run()
        elif choice == "4":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
