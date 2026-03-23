"пример с магазином"
"после покупки чего-либо склад должен собрать и упаковать товар, бухгалтерия выставить счет или чек и отправить на почту"
class MessageBus:
    def __init__(self):
        self._listeners = {}

    def subscribe(self, event_type, callback):
        """Подписываем службу на тип события"""
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)

    def publish(self, event_type, data):
        """Рассылаем данные всем, кто слушает этот тип события"""
        if event_type in self._listeners:
            for listener in self._listeners[event_type]:
                listener(data)


def warehouse_service(order_data):
    print(f"[СКЛАД] Товар '{order_data['item']}' зарезервирован.")

def delivery_service(order_data):
    print(f"[ДОСТАВКА] Создан маршрут для {order_data['address']}.")

def email_service(order_data):
    print(f"[EMAIL] Чек отправлен на почту клиента.")


if __name__ == "__main__":
    #центральный узел связи
    bus = MessageBus()

    #Регистрируем службы (они подписываются на событие order_placed)
    bus.subscribe("order_placed", warehouse_service)
    bus.subscribe("order_placed", delivery_service)
    bus.subscribe("order_placed", email_service)

    print(" МАГАЗИН: ОФОРМЛЕНИЕ ЗАКАЗА\n")

    #Имитируем покупку
    new_order = {
        "id": 101,
        "item": "Ноутбук",
        "address": "г. Омск, пр. Мира, 11"
    }

    #Публикуем событие. 
    bus.publish("order_placed", new_order)