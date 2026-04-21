import csv

FILE = "jobs.csv"

def add_job():
    company = input("Company: ")
    role = input("Role: ")
    status = input("Status (Applied/Interview/Rejected): ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([company, role, status])

    print("Job added!")


def view_jobs():
    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except:
        print("No data found")


def main():
    while True:
        print("\n1. Add Job")
        print("2. View Jobs")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            break


main()