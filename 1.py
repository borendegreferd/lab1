'''
Дан радиус окружности. Найти длину окружности и площадь круга.
'''
import math
rad=int(input())
print('Длина {:.3f}\nПлощадь {:.3f}'.format(math.pi * rad**2, 2 * math.pi * rad))