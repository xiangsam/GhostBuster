from sympy import *
import numpy as np


pi = 3.1415926
epsilon = 1e-6
alpha = 0.0001


def fix_a(N, x_t, f_init):
    ak = []
    for k in range(N):
        tmp = 0
        for t in range(N):
            tmp += x_t[t] * exp(I * -f_init[k] * 2 * pi * t / N)
            print(tmp)
        tmp = tmp / N
        ak.append(tmp)
    return ak

def fix_f(N, a_k, x_t, f_init):
    f = []  #f0,f1,f2...
    f_sym = []  #Symbol(f0 f1 f2...)
    value = []  #(f0:f_init[0]),(f1:f_init[1])
    f_value = np.array(f_init)
    for i in range(N):
        f.append("f" + str(i))
        f_sym.append(Symbol(f[i]))
        value.append((f_sym[i],f_value[i]))

    E = 0   #Error function
    for t in range(N):
        tmp = 0
        for k in range(N):
            tmp += a_k[k] * exp(I * f_sym[k] * 2 * pi * t / N)
        E += (x_t[t] - tmp)**2 #abs??
    # ltera = np.array(f_init)
    while(True):    #lterative
        delta= []
        for k in range(N):
            dfk = diff(E,f_sym[k]).subs(value)
            delta.append(re(dfk))
        gradient = -np.array(delta)
        print((np.sum(np.square(gradient))) ** 0.5)
        if((np.sum(np.square(gradient))) ** 0.5 < epsilon):
            break
        f_value = f_value + alpha * gradient
        # print(value)
        value = []
        for i in range(N):  #更新value值
            value.append((f[i], f_value[i]))
    return f_value




if __name__ == '__main__':
    N = 3
    x_t = [1,2,3]
    f_init = [1,2,3]
    a_k = [1,2,3]
    # x = Symbol("x")
    # y = Symbol("y")
    # z = exp(I * x * 2 * pi * 3/ N) + exp(I * y * 3 * pi * 3/ N)
    # d = diff(Abs(z),x).subs([(x,1),(y,1)])
    # print(d)
    print(fix_f(N, a_k, x_t, f_init))