"в данной задаче мы используем фабричный метод чтобы решать уравнения либо методом секущих либо методом ньютона "
class OptimizationMethod:
    def solve(self, function_str: str):
        raise NotImplementedError("Каждый метод должен реализовать solve()")



class NewtonMethod(OptimizationMethod):
    def solve(self, function_str: str):
        return f"[АНАЛИЗ] Решаем '{function_str}' методом Ньютона (через производные)."

class SecantMethod(OptimizationMethod):
    def solve(self, function_str: str):
        return f"[АНАЛИЗ] Решаем '{function_str}' методом Секущих (через две точки)."

class SolverFactory:
    @staticmethod
    def get_solver(method_type: str) -> OptimizationMethod:
        """Логика создания объектов спрятана здесь"""
        solvers = {
            "newton": NewtonMethod,
            "secant": SecantMethod
        }
        
        #Берем класс из словаря, если его нет — кидаем ошибку
        solver_class = solvers.get(method_type.lower())
        
        if solver_class:
            return solver_class()
        else:
            raise ValueError(f"Ошибка: Метод '{method_type}' еще не реализован!")



if __name__ == "__main__":
    #вот это ввел пользователь
    requested_methods = ["newton", "secant", "unknown"]
    equation = "x^2 - 4 = 0"

    print("=== Запуск Системы Вычислений ===\n")

    for method in requested_methods:
        try:
            #Мы не знаем, какой класс создастся
            solver = SolverFactory.get_solver(method)
            result = solver.solve(equation)
            print(f"Запрос '{method}': {result}")
            
        except ValueError as e:
            print(f"Запрос '{method}': {e}")