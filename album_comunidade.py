import random
import numpy as np
from math import comb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
import argparse


class Colecao:
    def __init__(self, N, n):
        self.N = N
        self.n = n
        self.album = {}
        self.pacotes = 0

    def gera_pacote(self):
        return [random.randint(1, self.N) for i in range(self.n)]

    def compra(self, qt):
        figurinhas, i = [], 0
        while i < qt:
            figurinhas.extend(self.gera_pacote())
            i += 1

        self.pacotes += qt
        return figurinhas

    def upgrade(self, figurinhas):
        for f in figurinhas:
            try:
                self.album[f] += 1
            except KeyError as err:
                self.album[f] = 1

    def downgrade(self, figurinhas):
        for f in figurinhas:
            self.album[f] -= 1

    def compra_e_upgrade(self, qt):
        self.upgrade(self.compra(qt))


class Trade:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def check_a_from_b(self, a, b):
        return [i for i in b.keys() if b[i] > 1 and i not in a]

    def make_trade(self):
        fig_c1_from_c2 = self.check_a_from_b(self.c1.album, self.c2.album)
        fig_c2_from_c1 = self.check_a_from_b(self.c2.album, self.c1.album)

        max_size = min([len(fig_c1_from_c2), len(fig_c2_from_c1)])

        self.c1.upgrade(fig_c1_from_c2)
        self.c2.downgrade(fig_c1_from_c2)

        self.c2.upgrade(fig_c2_from_c1)
        self.c1.downgrade(fig_c2_from_c1)

        return max_size


def roda_comunidade(mu=12, sigma=4, N=670, n=5, n_colections=1):

    colecoes = [Colecao(N, n) for i in range(n_colections)]

    total_trocas = max([int(comb(n_colections, 2) / 2), n_colections - 1])

    while min([len(c.album) for c in colecoes]) < N:

        for c in colecoes:
            c.compra_e_upgrade(int(abs(random.gauss(mu, sigma))))

        for i in range(total_trocas):

            c1, c2 = np.random.choice(colecoes, 2, replace=False)

            troca = Trade(c1, c2)
            troca.make_trade()

    pacotes = [i.pacotes for i in colecoes]
    return np.mean(pacotes)

def plot_boxplot(df, x, y, title):
    plt.figure(dpi=500)
    ax = sns.boxplot(x=x, y=y, data=df)
    plt.grid(True)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.savefig(f"boxplot_copa_2022_{y}.png")

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-N", type=int, help="Tamanho do Álbum", default=670)
    parser.add_argument("-np", type=int, help="Tamanho do Pacote", default=5)
    parser.add_argument(
        "-i", type=int, help="Número de iterações por Comunidade", default=1000
    )
    parser.add_argument(
        "-c", type=int, help="Quantidade de comunidades: [1,c]", default=20
    )
    parser.add_argument(
        "--mu", type=int, help="Média de pacotes por compra", default=12
    )
    parser.add_argument(
        "--sigma", type=int, help="Desvio padrão de pacotes por compra", default=4
    )
    args = parser.parse_args()

    comunidades = {i: int(args.i) for i in range(1, args.c + 1)}

    result = {"n_comunidade": [], "media_pacotes": []}

    for k, v in tqdm(comunidades.items()):
        result["n_comunidade"] += [k for i in range(v)]
        result["media_pacotes"] += [
            roda_comunidade(
                mu=args.mu, sigma=args.sigma, N=args.N, n=args.np, n_colections=k
            )
            for i in range(v)
        ]

    df = pd.DataFrame(result)
    df["Tamanho da Comunidade"] = df["n_comunidade"]
    df["Qtde. Pacotes"] = df["media_pacotes"]
    df["Valor Gasto"] = df["media_pacotes"] * 4

    plot_boxplot(df, "Tamanho da Comunidade", "Qtde. Pacotes", "Pacotes necessários para completar álbum da copa 2022")
    plot_boxplot(df, "Tamanho da Comunidade", "Valor Gasto", "Valor gasto para completar álbum da copa 2022")

    df.to_csv("data.csv", sep="|", decimal=",")

if __name__ == "__main__":
    main()
