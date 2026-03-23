"выбор доставки в зависимости от веса и ценгы посылки"
from abc import ABC, abstractmethod
class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight: float) -> float:
        pass



class CourierDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        # Фиксированная стоимость + 50 за кг
        return 300.0 + (weight * 50.0)

class PostDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        # Дешевле, но зависит только от веса
        return weight * 80.0

class PickUpDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        # Самовывоз всегда бесплатен
        return 0.0




class ShippingOrder:
    def __init__(self, item_name: str, weight: float):
        self.item_name = item_name
        self.weight = weight
        # По умолчанию ставим самовывоз
        self._delivery_strategy = PickUpDelivery()

    def set_delivery_strategy(self, strategy: DeliveryStrategy):
        """Метод для смены стратегии во время выполнения"""
        print(f"\nМеняем способ доставки для '{self.item_name}'...")
        self._delivery_strategy = strategy

    def calculate_total(self):
        """Вызов алгоритма через интерфейс стратегии"""
        cost = self._delivery_strategy.calculate_cost(self.weight)
        print(f"Стоимость доставки товара '{self.item_name}' (вес {self.weight} кг): {cost} руб.")


if __name__ == "__main__":
    # Создаем заказ: Ноутбук весом 2.5 кг
    my_order = ShippingOrder("Ноутбук", 2.5)

    # 1. По умолчанию (Самовывоз)
    my_order.calculate_total()

    # 2. Передумали, хотим курьером
    my_order.set_delivery_strategy(CourierDelivery())
    my_order.calculate_total()

    # 3. Дорого, выберем почту
    my_order.set_delivery_strategy(PostDelivery())
    my_order.calculate_total()