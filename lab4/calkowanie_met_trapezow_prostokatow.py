def metodaTrapezow(fun, a, b, n):
    integral = 0
    dx = (b - a) / n
    for i in range(n):
        fa = a + dx * i
        fb = a + dx * (i + 1)
        integral += (fun(fa) + fun(fb)) / 2 * dx
    return integral

mt = metodaTrapezow(lambda x: x + 2, 1.0, 4.0, 3)
print(mt)


def metodaProstokatow(fun, a, b, n):
  integral = 0
  dx = (b - a) / n
  for i in range(n):
    fa = a + dx * i
    fb = a + dx * (i + 1)
    integral += fun((fa + fb)/2) * dx
  return integral


mp = metodaProstokatow(lambda x: x + 2, 1.0, 4.0, 3)
print(mp)