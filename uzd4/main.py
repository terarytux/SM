import matplotlib.pyplot as plt

from uzd4.util import *
from uzd4.config import *


# function = lambda x: x*math.e**(2*x)
# a = 0
# b = 4

# ---------------------------------------------------------------------------------------------------------------------

N = init_N
results = [(N, simpsons_method(function, a, b, N), -1, -1)]
N *= 2
second_result = simpsons_method(function, a, b, N)
results.append((N, second_result, runge_error(results[-1][1], second_result, 4), -1))
N *= 2

while N <= end_N:
    result = simpsons_method(function, a, b, N)
    error = runge_error(results[-1][1], result, 4)
    results.append((N, result, error, results[-1][2] / error))
    N *= 2

print("{:-<80}".format(""))
print("{:-^80}".format(" Simpsono metodas "))
print("{:-<80}".format(""))

print("{:^9} | {:^19} | {:^19} | {:^19} |".format("N", "S_N", "Rungės paklaida", "Paklaidos pokytis"))
print("{:-<77}".format(""))
for result in results:
    print("{:>9d} | {:>19.12f} | {:>19.12f} | {:>19.12f} |".format(result[0], result[1], result[2], result[3]))

# ---------------------------------------------------------------------------------------------------------------------

N = init_N
results = [(N, gauss_quadrature_3(function, a, b, N), -1, -1)]
N *= 2
second_result = gauss_quadrature_3(function, a, b, N)
results.append((N, second_result, runge_error(results[-1][1], second_result, 6), -1))
N *= 2

while N <= end_N:
    result = gauss_quadrature_3(function, a, b, N)
    error = runge_error(results[-1][1], result, 6)
    results.append((N, result, error, results[-1][2] / error))
    N *= 2

print("{:-<80}".format(""))
print("{:-^80}".format(" Gauso kvadratūros metodas (3 eilės) "))
print("{:-<80}".format(""))

print("{:^9} | {:^19} | {:^19} | {:^19} |".format("N", "S_N", "Rungės paklaida", "Paklaidos pokytis"))
print("{:-<77}".format(""))
for result in results:
    print("{:>9d} | {:>19.12f} | {:>19.12f} | {:>19.12f} |".format(result[0], result[1], result[2], result[3]))

# ---------------------------------------------------------------------------------------------------------------------

print("{:-<80}".format(""))
print("{:-^80}".format(" Dvipakopis Rungės-Kutos metodas (sigma = 1) "))
print("{:-<80}".format(""))

h = max_h

last_result = runge_kutta_midpoint(function2, start, end, h, u0)
last_error = -1
while h >= min_h:
    new_result = runge_kutta_midpoint(function2, start, end, h/2, u0)
    error = runge_error(last_result[-1][1], new_result[-1][1], 2)
    if last_error != -1:
        print("h = {}, Paskutinis taškas ({}, {}), Paklaida = {}, Paklaidos pokytis = {}".format(h, last_result[-1][0], last_result[-1][1], error, last_error/error))
    else:
        print("h = {}, Paskutinis taškas ({}, {}), Paklaida = {}".format(h, last_result[-1][0], last_result[-1][1], error, last_error/error))

    x, y = zip(*last_result)
    plt.plot(x, y, 'b')
    h /= 2
    last_result = new_result
    last_error = error

plt.xlabel("x")
plt.ylabel("u")


plt.show()
