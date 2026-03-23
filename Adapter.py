"у нас есть календарь с задачами на день и класс Task в нем. Нам нужно добавить итерацию с учебным расписанием университета, которое выдает данные в формате json через старое API"
class MyTask:
    def __init__(self, title, time):
        self.title = title
        self.time = time

    def get_summary(self):
        return f"[{self.time}] Задача: {self.title}"

#Чужое API (это модуль расписания вуза, который нельзя менять)
class UniversityScheduleAPI:
    def get_university_lessons(self):
        return [
            {"subject": "Численные методы", "start_at": "08:00", "room": "П-302"},
            {"subject": "Философия", "start_at": "09:40", "room": "Г-212"}
        ]


"ADAPTER"
class UniversityAdapter:
    def __init__(self, lesson_dict):
        self.lesson = lesson_dict

    def get_summary(self):
        # Переводим ключи API (subject, start_at) формат (get_summary)
        return f"[{self.lesson['start_at']}] ПАРА: {self.lesson['subject']} (Ауд. {self.lesson['room']})"

class CalendarApp:
    def __init__(self):
        self.all_events = []

    def add_event(self, event):
        self.all_events.append(event)

    def show_schedule(self):
        print("--- ТВОЙ ПЛАН НА ДЕНЬ ---")
        for event in self.all_events:
            #Календарь уверен, что у всех объектов есть метод .get_summary()
            print(event.get_summary())



if __name__ == "__main__":
    app = CalendarApp()

    #Добавляем личную задачу
    my_task = MyTask("Сходить в спортзал", "18:00")
    app.add_event(my_task)

    #Теперь интегрируем расписание вуза
    api = UniversityScheduleAPI()
    lessons = api.get_university_lessons()

    for item in lessons:
        #Оборачиваем каждый словарь в Адаптер
        adapted_lesson = UniversityAdapter(item)
        app.add_event(adapted_lesson)

    #Вывод
    app.show_schedule()