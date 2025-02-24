class ChangeHistory:
    """
    Класс для отслеживания истории изменений текста.

    Этот класс позволяет добавлять версии текста и управлять историей изменений.

    Атрибуты:
        history (list): Список версий текста.
        current_index (int): Индекс текущей версии.
    """

    def __init__(self):
        self.history = []
        self.current_index = -1

    def add_version(self, text):
        """Добавление новой версии текста."""
        self.history.append(text)
        self.current_index = len(self.history) - 1

    def undo(self):
        """Отмена последнего изменения."""
        if self.current_index > 0:
            self.current_index -= 1
        return self.history[self.current_index] if self.history else None

    def redo(self):
        """Повтор последнего изменения."""
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
        return self.history[self.current_index] if self.history else None
