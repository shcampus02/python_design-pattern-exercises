"""
Übung 1 - Texteditor Un-/Redo

Das Memento-Muster ist sehr nützlich, um Un-/Redo-Funktionen zu implementieren.
In dieser Übung implementieren Sie ein einfaches Texteditor-Programm, das Un-/Redo unterstützt.

Implementieren Sie die Klassen 'TextEditor', 'EditorState' und 'EditorCaretaker'.
"""


class TextEditor:
    pass


class EditorState:
    pass


class EditorCaretaker:
    pass


if __name__ == "__main__":
    caretaker = EditorCaretaker()
    editor = TextEditor(caretaker, "First line of text.")
    editor.text = "Second line of text."
    editor.text = "Third line of text."
    print(editor.text)  # Output: "Third line of text."
    editor.undo()
    print(editor.text)  # Output: "Second line of text."
    editor.redo()
    print(editor.text)  # Output: "Third line of text."