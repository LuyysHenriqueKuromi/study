n = float(input('Digite uma distância em metros: '))
print('A medida de {}m corresponde a \n{}km \n{}hm \n{:.1f}dam \n{}dm \n{}cm \n{}mm'.format(n, n*0.001, n*0.01, n*0.1, n*10, n*100, n*1000))
