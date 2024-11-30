import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Функция для интегрирования."""
    return np.cos(x)

def simpsons_rule(a, b, tol):
    """Вычисление определенного интеграла методом Симпсона."""
    n = 2  # Начинаем с 2, чтобы n было четным
    h = (b - a) / n
    integral_old = (h / 3) * (f(a) + f(b) + 4 * f(a + h))
    
    while True:
        n *= 2
        h = (b - a) / n
        integral_new = (h / 3) * (f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + 
                                  2 * sum(f(a + i * h) for i in range(2, n, 2)))
        
        if abs(integral_new - integral_old) < tol:
            break
        
        integral_old = integral_new
    
    return integral_new, n

def plot_function(a, b):
    """Построение графика функции f(x)."""
    x = np.linspace(a, b, 100)
    y = f(x)
    
    plt.plot(x, y, label='f(x) = cos(x)')
    plt.title('График функции f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.show()

def main():
    """Основная функция программы."""
    a = float(input("Введите нижний предел A: "))
    b = float(input("Введите верхний предел B: "))
    tol = float(input("Введите абсолютную погрешность R (от 0.0001 до 0.01): "))
    
    if not (0.0001 <= tol <= 0.01):
        print("Погрешность должна быть в пределах от 0.0001 до 0.01.")
        return
    
    integral_value, intervals = simpsons_rule(a, b, tol)
    print(f"Значение определенного интеграла: {integral_value}")
    print(f"Количество интервалов, использованных для вычисления: {intervals}")
    
    plot_function(a, b)
