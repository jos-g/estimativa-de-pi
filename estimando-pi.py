# estimativa-de-pi
## importando bibliotecas 
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import statistics as stat
from scipy import stats as st
##
df = pd.read.excel('Caminho-do-arquivo') 
df.head() 
## separando em arrays
array_1 = df.iloc[:,1] 
array_2 = df.iloc[:,2]
#...

# médias
N = array_1.size
media_1 = np.sum(array_1) / N
print ("Média Coluna 1: {}".format(media_1))

# mediana
mediana_1 = np.median(array_1)
print("Mediana Coluna 1: {}".format(mediana_1))

# variância
var1 = np.var( array_1, ddof=1)
print ("Variância Coluna 1: {}".format(var1))

# Erros e Cálculo da estimativa 
sig_1 = var1/np.sqrt(N) #onde N é o número de dados da amostra
sig_2 = var2/np.sqrt(N)
sig_total= np.sqrt((sig_1)**2 + (sig_2)**2)
# erro da média
erro_media = sig_t/np.sqrt(N)
print ("Erro da média = {}".format( erro_media))
print ("Estimativa = {:.2f) ± {:.2f}".format( np.round( media_c, 2 ), np.round( erro_media_L, 2 ) ) )

# Ajuste Linear
X = np.array([x_1,x_2,x_3,...,x_n])
Y = np.array([y_1,y_2,y_3,...,y_n])
mod_linear = np.polyfit( X, Y, 1)

#Fazendo a reta do ajuste
# y = ax+b
a = float(mod_linear[0])
b = float(mod_linear[1])
y_mod = a*X + b 
print(y_mod)

#Diagrama de dispersão
plt.figure( figsize=(8,8))
plt.plot(X,Y, "o", label='Relação x= (T/2π)² e Y = L')
plt.plot(X,y_mod, "-r")
plt.xlabel("(T/2π)² (s²)")
plt.ylabel("Comprimento (m)")
plt.legend()
plt.show()

#R²
yresid = Y - y_mod
SQresid = sum(yresid**2)
y_tot   = Y - np.mean(Y)
SQtotal = sum(y_tot**2)
R2 = 1 - SQresid/SQTotal
print ('coeficiente de determinação do ajuste {:.4f}'.format(R2))


#Cálculo das incertezas em x, y, a e b  
#incerteza y
iny = np.sqrt((1/(n-2))*sum(SQresid))
print(iny)

#incerteza x 
inx = iny/a
print(inx)

#incerteza em a 
ina = (1/dp_x)*(iny/np.sqrt(n))
print(ina)

#incerteza em b
inb = sig_a*np.sqrt(sum(X**2)/n)
print (inb)

#Estimando o valor final e analisando a discrepância
vf = a
print (vf)
vr = k  #valor referencia em questão
#discrepância
dis_0 = np.sqrt((vf - k)**2))
print(dis_0)

#erro relativo
er_0 = sig_a/a
print(er_0)

#porcentagem do erro
pg = er_0 *100
print(pg)


