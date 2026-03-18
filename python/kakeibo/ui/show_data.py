import tkinter
import datetime
from db.expense  import show_expenses

def show_data(parent, expenses):
    card = tkinter.Frame(parent, bg="#e5e5e5", bd=0)
    card.pack(fill="x", pady=15)

    title_label = tkinter.Label(
        card,
        text="今月の出費",
        font=("Noto Sans JP", 16, "bold"),
    )
    title_label.pack(anchor="center", padx=20, pady=10)

    expenses_data = show_expenses()

    # テーブル用フレーム
    table_frame = tkinter.Frame(card)
    table_frame.pack(pady=(0,20))

    # ヘッダー
    headers = ["ID", "日付", "商品", "金額"]
    for col, text in enumerate(headers):
        label = tkinter.Label(table_frame, text=text, font=("Arial", 12, "bold"))
        label.grid(row=0, column=col, padx=70, pady=5)

    now = datetime.datetime.now()
    now_year = now.year
    now_month = now.month

    # データ
    for row_index, data in enumerate(expenses_data, start=1):
        values = [data[0], data[1], data[2], data[3]]
        date_str = values[1]
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")

        if date_obj.year == now_year and date_obj.month == now_month:
            for col_index, value in enumerate(values):
                label = tkinter.Label(table_frame, text=value)
                label.grid(row=row_index, column=col_index, padx=70, pady=5)