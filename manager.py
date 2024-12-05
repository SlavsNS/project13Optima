
import json
import os
from character import Character

class CharacterManager:
    def __init__(self):
        self.characters = []
        self.data_file = "data.json"
        self.load_characters()

    def load_characters(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                data = json.load(file)
                self.characters = [Character.from_dict(c) for c in data]
        else:
            self.characters = []

    def save_characters(self):
        with open(self.data_file, "w") as file:
            json.dump([c.to_dict() for c in self.characters], file, indent=4)

    def add_character(self):
        print("Adding a new character.")
        name = input("Enter character name: ").strip()
        age = input("Enter character age: ").strip()
        description = input("Enter character description: ").strip()
        image_url = input("Enter character image URL (optional): ").strip()
        self.characters.append(Character(name, age, description, image_url))
        print(f"Character {name} added successfully!")

    def list_characters(self):
        if not self.characters:
            print("No characters available.")
            return
        print("List of characters:")
        for index, character in enumerate(self.characters, start=1):
            print(f"{index}. {character}")

    def run(self):
        while True:
            print("\nCharacter Manager")
            print("1. View all characters")
            print("2. Add a new character")
            print("3. Save characters")
            print("4. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.list_characters()
            elif choice == "2":
                self.add_character()
            elif choice == "3":
                self.save_characters()
                print("Characters saved successfully!")
            elif choice == "4":
                print("Exiting Character Manager.")
                break
            else:
                print("Invalid choice. Please try again.")
