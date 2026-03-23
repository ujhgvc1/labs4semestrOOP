"создаем модель спортивных часов которые управляются тремя кнопками"
class WatchState:
    def press_main_button(self, watch):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")
    def press_reset_button(self, watch):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")



class IdleState(WatchState):
    def press_main_button(self, watch):
        print("[СТАРТ] Секундомер запущен!")
        watch.set_state(TrackingState())

    def press_reset_button(self, watch):
        print("[ИНФО] Сбрасывать нечего, мы на нуле.")

class TrackingState(WatchState):
    def press_main_button(self, watch):
        print("[ПАУЗА] Тренировка приостановлена.")
        watch.set_state(PausedState())

    def press_reset_button(self, watch):
        print("[КРУГ] Отметка времени сохранена.")

class PausedState(WatchState):
    def press_main_button(self, watch):
        print("[ПРОДОЛЖИТЬ] Снова бежим!")
        watch.set_state(TrackingState())

    def press_reset_button(self, watch):
        print("[СБРОС] Все данные стерты. Возврат в режим ожидания.")
        watch.set_state(IdleState())



class SportWatch:
    def __init__(self):
        self._state = IdleState()

    def set_state(self, state):
        """Смена состояния"""
        self._state = state

    def main_button(self):
        self._state.press_main_button(self)

    def reset_button(self):
        self._state.press_reset_button(self)

watch = SportWatch()
watch.main_button()   # Нажали Старт -> Tracking
watch.reset_button()  # Нажали Круг
watch.main_button()   # Нажали Пауза -> Paused
watch.reset_button()  # Нажали Сброс -> Idle