from expense import add_expense, show_expenses

while True:

    print("1 追加")
    print("2 表示")
    print("3 終了")

    choice = input("選択: ")

    if choice == "1":
        date = input("日付: ")
        item = input("項目: ")
        price = int(input("金額: "))
        add_expense(date, item, price)

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        break
