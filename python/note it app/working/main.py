import json
import tkinter as tk
import os

class Note:
    def __init__(self, title, content):
        """
        Initialize a Note object with a title and content.
        
        Args:
            title (str): The title of the note.
            content (str): The content of the note.
        
        Raises:
            TypeError: If title or content is not a string.
            ValueError: If title or content is empty.
        """
        if not isinstance(title, str) or not isinstance(content, str):
            raise TypeError("Title and content must be strings")
        if not title or not content:
            raise ValueError("Title and content cannot be empty")
        self.title = title
        self.content = content

    def __str__(self):
        """
        Return a human-readable string representation of the note.
        
        Returns:
            str: A string representation of the note.
        """
        return f"Title: {self.title}\nContent: {self.content}"

    def __repr__(self):
        """
        Return a string representation of the note that can be used to recreate the object.
        
        Returns:
            str: A string representation of the note.
        """
        return f"Note('{self.title}', '{self.content}')"

    def to_json(self):
        """
        Serialize the note data to JSON format.
        
        Returns:
            str: The note data serialized to JSON format.
        """
        e = json.dumps({"title": self.title, "content": self.content})

    @classmethod
    def from_json(cls, json_data):
        """
        Deserialize the note data from JSON format and create a Note object.
        
        Args:
            json_data (str): The note data in JSON format.
        
        Returns:
            Note: A Note object created from the deserialized data.
        """
        data = json.loads(json_data)
        title = data.get('title')
        content = data.get('content')
        return cls(title, content)

class NoteItApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Create the note list
        self.note_list = tk.Listbox(self)
        self.note_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the note editor
        self.note_editor = tk.Text(self)
        self.note_editor.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create the save and load buttons
        self.save_button = tk.Button(self, text="Save", command=self.save_notes)
        self.save_button.pack(side=tk.BOTTOM)
        self.load_button = tk.Button(self, text="Load", command=self.load_notes)
        self.load_button.pack(side=tk.BOTTOM)

        # Bind the note list to the note editor
        self.note_list.bind("<<ListboxSelect>>", self.on_note_selected)

        # Load the notes from the JSON file
        self.load_notes()

    def on_note_selected(self, event):
        # Get the selected note
        selected_note = self.note_list.get(event.widget.curselection())

        # Load the note content into the note editor
        self.note_editor.delete(1.0, tk.END)
        self.note_editor.insert(1.0, selected_note.content)

    def save_notes(self):
        # Get the note title and content from the note editor
        note_title = self.note_editor.get("1.0", tk.END).strip()
        note_content = self.note_editor.get("1.0", tk.END)

        # Create a new note
        note = Note(note_title, note_content)

        # Add the note to the note list
        self.note_list.insert(tk.END, note_title)

        # Save the notes to the JSON file
        with open("notes.json", "w") as f:
            json.dump(self.notes, f)

    def load_notes(self):
        # Check if the file exists
        if os.path.exists("notes.json"):
            try:
                # Load the notes from the JSON file
                with open("notes.json", "r") as f:
                    self.notes = json.load(f)
            except json.JSONDecodeError:
                # Handle JSONDecodeError exception
                print("Error: Invalid JSON file format")
                return
        else:
            # Handle the scenario where the file does not exist
            print("Notes file does not exist.")
            return

        # Clear the note list
        self.note_list.delete(0, tk.END)

        # Add the notes to the note list
        for note in self.notes:
            if hasattr(note, 'title'):
                self.note_list.insert(tk.END, note.title)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteItApp(root)
    app.pack()
    root.mainloop()
