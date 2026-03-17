from db.database import get_connection

def add_expense(date, item, price):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO expenses (date,item,price) VALUES (?,?,?)",
        (date, item, price)
    )

    conn.commit()
    conn.close()

def show_expenses():

    conn = get_connection()
    cur = conn.cursor()

    for row in cur.execute("SELECT * FROM expenses"):
        print(row)

    conn.close()