import numpy as np
import matplotlib.pyplot as plt

# Задаем параметры
frequencies = [10e3, 5e3, 2e3]  # частоты в Гц
amplitude = 5  # амплитуда
duration = 1e-3  # длительность в секундах
sampling_step = 1e-6  # шаг моделирования в секундах
t = np.arange(0, duration, sampling_step)  # временной массив

# Генерация треугольного сигнала с частотой 10 кГц
triangle_signal = amplitude * (2 * np.abs(2 * (t * frequencies[0] % 1) - 1))

# Определение запрещенной зоны
lower_bound = 2
upper_bound = 4

# Инициализация выходного сигнала
output_signal = np.zeros_like(triangle_signal)

# Генерация выходного сигнала на основе запрещенной зоны
output_signal[triangle_signal > upper_bound] = amplitude
output_signal[triangle_signal < lower_bound] = 0

# Визуализация сигналов
plt.figure(figsize=(12, 6))

# Исходный треугольный сигнал
plt.subplot(2, 1, 1)
plt.plot(t * 1e3, triangle_signal, label='Треугольный сигнал', color='blue')
plt.axhline(y=lower_bound, color='red', linestyle='--', label='Нижняя граница')
plt.axhline(y=upper_bound, color='green', linestyle='--', label='Верхняя граница')
plt.title('Исходный треугольный сигнал с запрещенной зоной')
plt.xlabel('Время (мс)')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid()

# Выходной сигнал
plt.subplot(2, 1, 2)
plt.plot(t * 1e3, output_signal, label='Выходной сигнал', color='orange')
plt.title('Выходной сигнал логического каскада')
plt.xlabel('Время (мс)')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()