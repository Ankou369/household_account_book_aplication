import tkinter

def create_header(header):
    title = tkinter.Label(header,
                        text="家計簿アプリ",
                        font=("Noto Sans JP", 24, "bold"),
                        bg="#2f6fbd",
                        fg="white")
    title.pack(pady=(30,5))

    subtitle = tkinter.Label(header,
                        text="支出管理ページ",
                        font=("Noto Sans JP", 12),
                        bg="#2f6fbd",
                        fg="white")
    subtitle.pack()