import random
import matplotlib.pyplot as plt
import numpy as np

def completa_album(N, n):

    album = set() # album esta novo

    pacotes = 0
    while len(album) < N:
        pacote = {random.randint(1,N) for i in range(n)} # compro n figurinhas e colo no algum  
        pacotes += 1
        album.update(pacote) # atualiza o album com as figurinhas novas

    return pacotes

albuns = [completa_album(670,5) for i in range(10000)]

plt.hist(albuns)
plt.grid(True)
plt.show()

media = np.mean(albuns)
desvio = np.std(albuns)

print("Média de Pacotes:", media)
print("desvio padrão de Pacotes:", desvio)