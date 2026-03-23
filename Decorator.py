"хотим добавить новые функции для события в календаре (пометки вроде СРОЧНО и ВАЖНО)"
class AbstractTask:
    def render(self) -> str:
        raise NotImplementedError()

class SimpleTask(AbstractTask):
    def __init__(self, text: str):
        self._text = text

    def render(self) -> str:
        return self._text



class TaskDecorator(AbstractTask):
    def __init__(self, task: AbstractTask):
        self._wrapped_task = task

    def render(self) -> str:
        return self._wrapped_task.render()


class ImportantDecorator(TaskDecorator):
    """Добавляет статус важности"""
    def render(self) -> str:
        return f" ВАЖНО: {super().render()} "

class NotificationDecorator(TaskDecorator):
    """Добавляет пометку об уведомлении"""
    def render(self) -> str:
        return f"{super().render()} [Звуковой сигнал включен]"

class LogDecorator(TaskDecorator):
    """Добавляет время создания (имитация логирования)"""
    def render(self) -> str:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M")
        return f"({now}) {super().render()}"



if __name__ == "__main__":
    print("=== Создание кастомных задач ===\n")

    #Просто задача
    task = SimpleTask("Подготовить отчет по Численным методам")
    print(f"1. Обычная: {task.render()}")

    #Делаем её важной
    important_task = ImportantDecorator(task)
    print(f"2. С декором: {important_task.render()}")

    #Добавляем уведомление К УЖЕ важной задаче (Матрешка!)
    full_task = NotificationDecorator(important_task)
    print(f"3. Двойной декор: {full_task.render()}")

    #А теперь всё сразу + время (Лог)
    super_task = LogDecorator(NotificationDecorator(ImportantDecorator(SimpleTask("Экзамен в ОмГТУ"))))
    print(f"4. Комбо: {super_task.render()}")