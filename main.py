"""
main.py
---------
This is the entry point of the application.
The menu system works here and calls other modules according to the requests from the user.
"""

from storage import load_notes, save_notes
from utils import now_iso, next_id
import storage
print("STORAGE MODULE PATH:", storage.__file__)
print("RUNNING FILE:", __file__)



def print_menu():
    # Shows the user the main menu
    print("\n--- File Reading/Writing: Notes Application ---")
    print("1) Add note")
    print("2) List notes")
    print("3) Delete note")
    print("4) Search in notes")
    print("5) Exit")

def add_note():
    # It takes notes from the user and saves them to a file
    notes = load_notes()
    text = input("Not: ").strip()
    if not text:
        print("Blank notes cannot be added..")
        return
    
    note = {"id": next_id(notes), "text": text, "created_at": now_iso()}
    notes.append(note)
    save_notes(notes)
    print(f"Note added (id={note["id"]})")

def list_notes():
    # Lists all saved notes
    notes = load_notes()
    if not notes:
        print("No notes yet.")
        return

    print("\n--- Notes ---")
    for n in notes:
        note_id = n.get("id", "?")
        text = n.get("text", "")
        created = n.get("created_at", "unknown")

        print(f"[{note_id}] {text} ({created})")


def delete_notes():
    # Deletes notes based on ID
    notes = load_notes()
    if not notes:
        print("There are no notes to erase..")
        return
    
    try:
        note_id = int(input("Note ID to be deleted: ").strip())
    except ValueError:
        print("Invalid id.")
        return
    
    new_notes =[n for n in notes if n["id"] != note_id]
    if len(new_notes) == len(notes):
        print("No records were found with this ID..")
        return
    
    save_notes(new_notes)
    print("Note deleted.")

def search_notes():
    # Searches within notes based on keywords
    notes = load_notes()
    if not notes:
        print("There are no notes to look for..")
        return
    
    q = input("search word: ").strip().lower()
    if not q:
        print("No empty searches.")
        return
    
    results = [n for n in notes if q in n["text"].lower()]
    if not results:
        print("No results found.")
        return
    
    print("\n--- Search Results ---")
    for n in results:
        print(f"[{n["id"]}] {n["text"]} ({n["created_at"]})")

def main():
    """
       Main loop:
       The program starts here and runs until the user exits. 
    """
    while True:
        print_menu()
        choice = input("Vote: ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            search_notes()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid selection.")

# When this file is executed directly, the main() function is called
if __name__ == "__main__":
    main()