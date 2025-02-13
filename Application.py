class Application:
    def __init__(self, platform):
        self.platform = platform
        if platform == "web":
            self.init_web_app()
        elif platform == "desktop":
            self.init_desktop_app()

    def init_web_app(self):
        print("Инициализация веб-приложения")

    def init_desktop_app(self):
        print("Инициализация настольного приложения")

    def run(self):
        print(f"Запуск приложения на платформе: {self.platform}")

# Изменение в другой ветке
