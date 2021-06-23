print ('-'*20)
print('analisador de triângulos')
print('-'*20)
r1 = float(input('Primeito segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))
if r1< r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' Os segmentos de reta acima poderão formar um triângulo')
else:
    print('Os segmentos de reta acima não poderão formar um triângulo ')