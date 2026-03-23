from dataclasses import dataclass, asdict, field
import json

@dataclass
class BaseDataModel:
    """Базовый класс для всех моделей данных"""
    
    def to_dict(self):
        """Превращает объект в обычный словарь (удобно для JSON или БД)"""
        return asdict(self)

    def to_json(self):
        """Превращает объект в JSON-строку"""
        return json.dumps(self.to_dict(), ensure_ascii=False)

@dataclass
class Task(BaseDataModel):
    id: int
    title: str
    priority: str = "Medium"

@dataclass
class CalculationResult(BaseDataModel):
    x_value: float
    iterations: int
    method_name: str


if __name__ == "__main__":
    #Создаем задачу
    task = Task(1, "Сдать РГР в ОмГТУ", "High")
    
    #Создаем результат расчета (например, методом Ньютона)
    res = CalculationResult(0.577, 12, "Newton")

    print("=== Объекты как Python-классы ===")
    print(task)
    print(res)

    print("\n=== Экспорт в JSON (через базовый класс) ===")
    print(task.to_json())
    print(res.to_json())