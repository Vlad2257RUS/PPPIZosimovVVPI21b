class FileHandler:
    """
    Класс для работы с файлами.

    Этот класс предоставляет функции для открытия и сохранения файлов.

    Методы:
        open_file(file_path): Открытие файла и чтение его содержимого.
        save_file(file_path, content): Сохранение содержимого в файл.
    """

    def open_file(self, file_path):
        """Открытие файла и чтение его содержимого."""
        with open(file_path, 'r') as file:
            return file.read()

    def save_file(self, file_path, content):
        """Сохранение содержимого в файл."""
        with open(file_path, 'w') as file:
            file.write(content)

