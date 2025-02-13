class AutoComplete:
    def __init__(self):
        # Инициализация списка ключевых слов
        self.keywords = ["def", "class", "import", "from", "if", "else", "elif", "while", "for", "return"]

    def get_suggestions(self, input_text):
        suggestions = []
        for keyword in self.keywords:
            if keyword.startswith(input_text):
                suggestions.append(keyword)
        return suggestions
