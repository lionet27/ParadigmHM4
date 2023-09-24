import random
import statistics
import math
from scipy.stats import pearsonr



def correlation_pirs(arrx, arry):
    assert len(arrx)==len(arry), "Списки разной длины"
    sum_diff = sum(map(lambda x, y: (x-statistics.mean(arrx))*(y-statistics.mean(arry)), arrx, arry))
    return round(sum_diff/math.sqrt(( sum(map(lambda x: ((x-statistics.mean(arrx))**2), arrx))* sum(map(lambda y: ((y-statistics.mean(arry))**2), arry)))),4)

def main():
    array_x, array_y = [], []
    for i in range(7):
        array_x.append(random.randint(0, 100))
        array_y.append(random.randint(0, 100))
    print(f'Array of X: {array_x} \nArray of Y: {array_y}')
    print(f'\ncorrelation_pirs = {correlation_pirs(array_x, array_y)}')
    # Проверка корреляции Пирсона с помощью функции pearsonr из scipy.stats
    print(f'\ncorrelation_pirs = {pearsonr(array_x, array_y)}')
    
   


if __name__ == "__main__":
    main()