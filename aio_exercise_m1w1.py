import math
import random

def f1_score_calc(tp, fp, fn):
    if tp <= 0 or fp <= 0 or fn <=0:
        print('tp and fp and fn must be greater than zero')
        return
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fb, int):
        if type(tp) != int:
            print('tp must be int')
        if type(fp) != int:
            print('fp must be int')    
        if type(fn) != int:
            print('fn must be int')
        return
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1score = 2 * (precision * recall)/(precision + recall)   
    print(f'Precision is {precision}\n\
            Recall is {recall}\n\
            F1-score is {f1score}')

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def activation_functions():
    x = input('x =')
    activation_function = input('Input activation Function (sigmoid|relu|elu):')
    if is_number(x):
        x = float(x)
        if activation_function == 'sigmoid':
            return 1 / (1 + math.exp(-x))
        elif activation_function == 'relu':
            return max(0,x)
        elif activation_function == 'elu':
            if x <= 0:
                return 0.01 * (math.exp(x) - 1)
            else:
                return x
        else:
            print(f'{activation_function} is not supported')
    else:
        print('x must be a number')
        
def reg_loss_function():
    '''
    Hàm tính toán loss cho các mô hình hồi quy
    '''
    num_samples = input('Input number of samples (integer number) which are generated:') #Số lượng sample
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return
    loss_name = input('Input loss name:') #Loss function muốn sử dụng (MAE, MSE, RMSE)
    predict = random.uniform(0,10)
    target = random.uniform(0,10)
    MAE_Total = 0
    MSE_Total = 0
    for sample in range (0,num_samples):
        mae=target-predict
        mse=(target-predict)**2
        MAE_Total += mae
        MSE_Total += mse
    RMSE_Total = math.sqrt(MSE_Total)
    if loss_name == 'MAE':
        print(f'loss name: {loss_name}, sample: {num_samples}, pred: {predict}, target: {target}, loss: {MAE_Total/num_samples}')
    if loss_name == 'MSE':
        print(f'loss name: {loss_name}, sample: {num_samples}, pred: {predict}, target: {target}, loss: {MSE_Total/num_samples}')
    if loss_name == 'RMSE':
        print(f'loss name: {loss_name}, sample: {num_samples}, pred: {predict}, target: {target}, loss: {RMSE_Total/num_samples}')

def factorial(x):
    fct = 1
    if x == 0:
        return fct
    if x != 0:
        for i in range(1, x+1):
            fct *= i
        return fct

def approx_sin(x, n):
    sinx = 0
    for i in range (0, n+1):
        fctl = factorial(2*i+1)
        sinx = sinx + ((-1)**i)*(x**(2*i+1))/fctl
    return sinx

def approx_cos(x, n):
    cosx = 0
    for i in range (0, n+1):
        fctl = factorial(2*i)
        cosx = cosx +((-1)**i)*(x**(2*i))/fctl
    return cosx

def approx_sinh(x, n):
    sinhx = 0
    for i in range (0, n+1):
        fctl = factorial(2*i+1)
        sinhx = sinhx + (x**(2*i+1))/fctl
    return sinhx

def approx_cosh(x, n):
    coshx = 0
    for i in range (0, n+1):
        fctl = factorial(2*i)
        coshx = coshx +(x**(2*i))/fctl
    return coshx

def nd_nre_single_sample(y, y_hat, n, p):
    md_nre = ((y**(1/n))-(y_hat**(1/n)))**p
    return md_nre