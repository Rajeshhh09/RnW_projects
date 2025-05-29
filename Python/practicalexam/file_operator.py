from datetime import datetime
import os

print("Welome to Personal Journal Manager!")
print("Please Select an option:\n ")
class Journalmanager:

    def __init__(self,journals):
        self.journals = journals
        
    def add_journals(self,content):
        now = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        try:
            with open("journal_file.txt","a") as f:
                f.write(f"[{now}] {content}\n")
        except FileExistsError:
            print("File not found!!")
        print("Entry Added Successfully!\n")

    def view_journals(self):
        with open("journal_file.txt","r") as f:
            data = f.read()
            if data.strip() == "":
                print("Journal is Empty")
            else:
                print("Your Journal:\n")
                print(data)       

    def search_journals(self,keyword):
        found = False
        try:
            with open("journal_file.txt","r") as f:
                for line in f:
                    if keyword.lower() in line.lower():
                        print(line.strip()) 
                        found = True
            if not found:
                print("no matching entry found!")
        except FileNotFoundError:
            print("there is no journal in this file")

    def delete_journal(self):
        if os.path.exists(self.journals):
            confirm = input("are you sure you want to delete ALL JOURNALS ? (yes/no)")
            if confirm.lower() == "yes":
                print("All your journals have been deleted.")
                open("journal_file.txt" ,"w").close()
            else:
                print("Deletion Cancelled")
        else:
            print("Output(If the file does not exist):")
            print("no journal entries to delete.")


journal = Journalmanager("journal_file.txt")                        

while True:
    print("1. Add a new Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("User Input: ")

    match choice:
        case '1':
            entry = input("Enter your Journal entry:\n")
            journal.add_journals(entry)

        case '2':
            print("Output (If the file exists):")
            print("Your Journal Entries: ")
            print("-"*60)
            journal.view_journals() 

        case '3':

            keyword = input("Enter keyword or date to search: ")  
            print("Output (If a Match is Found):")
            print("Matching Entries:")
            print("-"*60)        
            journal.search_journals(keyword)

        case '4':
            
            journal.delete_journal()

        case '5':
            print("Exiting...")
            break
        case _:
            print("invalid case!! try again.")
