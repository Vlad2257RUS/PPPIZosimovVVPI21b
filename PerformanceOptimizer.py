import asyncio

class PerformanceOptimizer:
    """
    Класс для оптимизации производительности.

    Этот класс предоставляет функции для кэширования данных и асинхронной обработки.

    Методы:
        cache_data(data): Кэширование данных.
        async_process(task): Асинхронная обработка задачи.
        optimize_large_files(file): Оптимизация больших файлов.
    """

    def cache_data(self, data):
        """Кэширование данных."""
        self.cache = data
        print("Данные кэшированы:", data)

    async def async_process(self, task):
        """Асинхронная обработка задачи."""
        print("Запуск асинхронной задачи...")
        await asyncio.sleep(1)  # Симуляция асинхронной работы
        print("Задача завершена:", task)

    def optimize_large_files(self, file):
        """Оптимизация больших файлов."""
        print(f"Оптимизация файла: {file}")


