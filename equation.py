import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Функция для нахождения корня."""
    return x**3 - 2*x**2 + x + 1

def f_prime(x):
    """Первая производная функции."""
    return 3*x**2 - 4*x + 1

def find_root(A, B, R, E, Nmax):
    """Поиск корня методом касательных."""
    f_A = f(A)
    f_B = f(B)
    n = 0
    
    if f_A * f_B > 0:
        print("Корень отсутствует, L = -1")
        return -1, 0

    while n < Nmax:
        X1 = A - f(A) / f_prime(A)
        f_X1 = f(X1)
        n += 1
        
        if abs(f_X1) <= E:
            print(f"Корень найден: X = {X1}, L = 1, итераций = {n}")
            return X1, n
        
        if abs(X1 - A) < R:
            print("Условие по R выполнено, L = 0")
            return X1, n
        
        A = X1
    
    print("Достигнуто максимальное количество итераций, n =", n)
    return X1, n

def main():
    """Основная функция программы."""
    # Автоматическое определение диапазона
    x_values = np.linspace(-3, 3, 100)
    y_values = f(x_values)
    
    # Определяем границы A и B
    A = -3
    B = 3
    
    # Проверка наличия корня в диапазоне
    if np.all(y_values > 0) or np.all(y_values < 0):
        print("Корень отсутствует в заданном диапазоне.")
        return
    
    # Устанавливаем параметры для метода касательных
    R = 1e-5
    E = 1e-5 
    Nmax = 100

    root, iterations = find_root(A, B, R, E, Nmax)

    # Построение графика функции
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label='f(x) = x^3 - 2x^2 + x + 1', color='blue')
    plt.axhline(0, color='black', lw=0.5, ls='--')  # Горизонтальная линия y=0
    plt.axvline(0, color='black', lw=0.5, ls='--')  # Вертикальная линия x=0
    
    # Отметить найденный корень на графике
    if root != -1:
        plt.plot(root, f(root), 'ro', label=f'Корень: X = {root:.4f}')
    
    plt.title('График функции и найденный корень')
    plt.xlabel('X')
    plt.ylabel('f(X)')
    plt.legend()
    plt.grid()
    plt.xlim(-3, 3)
    plt.ylim(-5, 5)
    plt.show()


