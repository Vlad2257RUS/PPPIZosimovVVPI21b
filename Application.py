class Application:
    """
    Класс приложения.

    Этот класс отвечает за инициализацию и запуск приложения на различных платформах.

    Атрибуты:
        platform (str): Платформа, на которой будет работать приложение ("web" или "desktop").
    """

    def __init__(self, platform):
        self.platform = platform
        if platform == "web":
            self.init_web_app()
        elif platform == "desktop":
            self.init_desktop_app()

    def init_web_app(self):
        """Инициализация веб-приложения."""
        print("Инициализация веб-приложения")

    def init_desktop_app(self):
        """Инициализация настольного приложения."""
        print("Инициализация настольного приложения")

    def run(self):
        """Запуск приложения."""
        print(f"Запуск приложения на платформе: {self.platform}")
