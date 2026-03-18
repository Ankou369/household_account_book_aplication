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

    expenses_data = []

    for row in cur.execute("SELECT * FROM expenses"):
        expenses_data.append(row)

    conn.close()
    return expenses_data

def delete_expense(expense_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()
    conn.close()