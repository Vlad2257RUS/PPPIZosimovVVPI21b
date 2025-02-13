class ChangeHistory:
    def __init__(self):
        self.history = []
        self.current_index = -1

    def add_version(self, text):
        # Добавление новой версии
        self.history.append(text)
        self.current_index = len(self.history) - 1

    def undo(self):
        if self.current_index > 0:
            self.current_index -= 1
        return self.history[self.current_index] if self.history else None

    def redo(self):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
        return self.history[self.current_index] if self.history else None
