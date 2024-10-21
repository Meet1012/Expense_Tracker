import argparse
import json
import time
import pandas as pd
from datetime import datetime

json_file = open("expense.json", "r+")
try:
    expense = json.load(json_file)
except json.JSONDecodeError:
    expense = []


def add(desc, amount):
    created = datetime.now().strftime("%d-%m-%Y")
    if len(expense) == 0:
        lastID = 0
    else:
        lastID = expense[-1]["ID"]
    new = {"ID": lastID + 1, "Date": created,
           "Description": desc, "Amount": amount}
    expense.append(new)
    json_file.seek(0)
    json.dump(expense, json_file)
    json_file.truncate()
    time.sleep(1)
    print("[+] Expense Added [+]")


def delete(id):
    for i in expense:
        if i["ID"] == id:
            expense.remove(i)
            time.sleep(1)
            print("[+] Expense Deleted [+]")
            break
    else:
        print("[-] Expense not Found [-]")
    json_file.seek(0)
    json.dump(expense, json_file)
    json_file.truncate()


def update(id, desc, amount):
    for i in expense:
        if i["ID"] == id:
            if desc == None:
                i["Amount"] = amount
            elif amount == None:
                i["Description"] = desc
            else:
                i["Amount"] = amount
                i["Description"] = desc
            print("[+] Updated Successfully [+]")
            break
    else:
        print("[-] Expense Not Found [-]")
    json_file.seek(0)
    json.dump(expense, json_file)
    json_file.truncate()


def summary(month=None):
    month_name = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    total = 0
    if month:
        for i in expense:
            if int(i["Date"][3:5]) == month:
                total += i["Amount"]
        print(f"Total Expenses for {month_name[month]} are: {total}")
    else:
        for i in expense:
            total += i["Amount"]
        print(f"Total Expenses are : {total}")


def display():
    df = pd.DataFrame(expense)
    print(df.to_string(index=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("func", type=str)
    parser.add_argument("--description", type=str)
    parser.add_argument("--amount", type=int)
    parser.add_argument("--id", type=int)
    parser.add_argument("--month", type=int)
    parsed = parser.parse_args()
    # arg = json.dumps(parsed, indent=3)
    if parsed.func == "add":
        add(parsed.description, parsed.amount)
    elif parsed.func == "delete":
        delete(parsed.id)
    elif parsed.func == "update":
        update(parsed.id, parsed.description, parsed.amount)
    elif parsed.func == "summary":
        if parsed.month:
            summary(parsed.month)
        else:
            summary()
    elif parsed.func == "list":
        display()
    else:
        print("[-] Wrong Format Kindly go through the Readme file [-]")
