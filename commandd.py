"Случай управления умной розеткой удаленно, кнопки включить, выключить и перезагрузить"
class Server:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"[СЕРВЕР {self.name}] Питание подано. Загрузка ОС...")

    def turn_off(self):
        self.is_on = False
        print(f"[СЕРВЕР {self.name}] Завершение работы. Питание отключено.")


class Command:
    def execute(self): pass
    def undo(self): pass


class TurnOnCommand(Command):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.turn_on()

    def undo(self):
        print(f"[UNDO] Отмена включения сервера {self.server.name}...")
        self.server.turn_off()

class TurnOffCommand(Command):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.turn_off()

    def undo(self):
        print(f"[UNDO] Отмена выключения сервера {self.server.name}...")
        self.server.turn_on()

class RemoteControl:
    def __init__(self):
        self._history = []

    def press_button(self, command):
        command.execute()
        self._history.append(command)

    def press_undo(self):
        if self._history:
            cmd = self._history.pop()
            cmd.undo()
        else:
            print("История команд пуста!")



if __name__ == "__main__":
    #Создаем наш сервер
    omgtu_server = Server("Core-Main-01")
    remote = RemoteControl()

    print("--- Управляем сервером ---")
    
    #Включаем
    on_cmd = TurnOnCommand(omgtu_server)
    remote.press_button(on_cmd)

    # Выключаем (например, для тестов)
    off_cmd = TurnOffCommand(omgtu_server)
    remote.press_button(off_cmd)

    print("\n--- Ой, сервер должен быть включен! Жмем UNDO ---")
    remote.press_undo() #должен снова включить сервер

    print("\n--- Еще раз UNDO (возвращаемся в исходное состояние) ---")
    remote.press_undo() #Должен выключить сервер