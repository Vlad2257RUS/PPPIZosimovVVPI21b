class AutoComplete:
    """
    Класс автозаполнения.

    Этот класс предоставляет функции автозаполнения для языков программирования.

    Атрибуты:
        keywords (list): Список ключевых слов для автозаполнения.
    """

    def __init__(self):
        self.keywords = ["def", "class", "import", "from", "if", "else", "elif", "while", "for", "return"]

    def get_suggestions(self, input_text):
        """
        Получение предложений по автозаполнению.

        Аргументы:
            input_text (str): Вводимый текст для получения предложений.

        Возвращает:
            list: Список предложений по автозаполнению.
        """
        suggestions = []
        for keyword in self.keywords:
            if keyword.startswith(input_text):
                suggestions.append(keyword)
        return suggestions
