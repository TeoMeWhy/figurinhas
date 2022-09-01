# Álbuns da Copa 2022

Projetinho maroto com objetivo de estimar o número de pacotes necessários para completar o álbum da copa de 2022.

## Processo

Para isso, consideramos algumas condições e assumimos algumas hipóteses:

1. Tamanho do álbum (N figurinhas): 670
2. Tamanho do pacote (n figurinhas): 5
3. Tamanho da comunidade, i.e. pessoas possíveis que realizarão trocas entre si: 1 (solo) a 20.
4. Quantidade de pacotes comprados entre trocas segue uma distribuição $X \sim \mathcal{N}(\mu = 12, \sigma = 4)$. Ou seja, considera-se que uma pessoa entre uma rodada de trocas e outra, compra em média 12 pacotes com desvio padrão igual 4. Valores considerados a partir do CPTK (Centro de Pesquisa Tireido Ku) em nossas lives, mas podem ser alterados para identificar possíveis alterações.
5. Geração de 1.000 (mil) iterações por comunidade, i.e., para cada configuração de comunidade são gerados 1.000 vezes, 

## Execução

Para executar o código e obter os resultados basta executar o comando abaixo:

```console
$ python album_comunidade.py
```

Caso tenha interesse em rodar com uma configuração diferente, use o compando abaixo para acessar o helper:

```console
$ python album_comunidade.py --help
usage: album_comunidade.py [-h] [-N N] [-np NP] [-i I] [-c C] [--mu MU] [--sigma SIGMA]

optional arguments:
  -h, --help     show this help message and exit
  -N N           Tamanho do Álbum
  -np NP         Tamanho do Pacote
  -i I           Número de iterações por Comunidade
  -c C           Quantidade de comunidades: [1,c]
  --mu MU        Média de pacotes por compra
  --sigma SIGMA  Desvio padrão de pacotes por compra

```

## Resultado

### Quantidade de Figurinhas

Considerando todas as simulações temos a distribuição seguindo o gráfico abaixo, para cada configuração de tamanho de comunidade distinta.

<img src="https://i.ibb.co/7yL4f1r/boxplot-copa-2022-Qtde-Pacotes.png" alt="boxplot-copa-2022-Qtde-Pacotes">

Vale ainda adicionarmos uma tabela descritiva com estatíticas sumarizadas, considerando o mínimo, média e máximo de pacotes necessários:

|Tamanho da Comunidade|Mínimo|Média|Máximo|
|---|---|---|---|
|01 | 597 | 964 | 1792 |
|02 | 458 | 637 | 1110 |
|03 | 374 | 522 | 851 |
|04 | 344 | 464 | 800 |
|05 | 315 | 421 | 631 |
|06 | 299 | 393 | 612 |
|07 | 284 | 369 | 661 |
|08 | 280 | 351 | 486 |
|09 | 278 | 338 | 479 |
|10 | 268 | 326 | 473 |
|11 | 261 | 316 | 451 |
|12 | 251 | 306 | 408 |
|13 | 249 | 300 | 399 |
|14 | 239 | 292 | 400 |
|15 | 241 | 286 | 424 |
|16 | 240 | 281 | 386 |
|17 | 233 | 275 | 407 |
|18 | 236 | 272 | 364 |
|19 | 229 | 269 | 350 |
|20 | 228 | 265 | 339 |

## Preço do Álbum


<img src="https://i.ibb.co/CMz3y0G/boxplot-copa-2022-Valor-Gasto.png" alt="boxplot-copa-2022-Valor-Gasto">


|Tamanho da Comunidade|Mínimo|Média|Máximo|
|---|---|---|---|
01|R$ 2372,00| R$ 3858,00| R$ 7168,00|
02|R$ 1834,00| R$ 2548,00| R$ 4442,00|
03|R$ 1496,00| R$ 2089,00| R$ 3406,00|
04|R$ 1376,00| R$ 1857,00| R$ 3200,00|
05|R$ 1262,00| R$ 1686,00| R$ 2524,00|
06|R$ 1196,00| R$ 1572,00| R$ 2449,00|
07|R$ 1138,00| R$ 1478,00| R$ 2647,00|
08|R$ 1122,00| R$ 1404,00| R$ 1944,00|
09|R$ 1112,00| R$ 1353,00| R$ 1916,00|
10|R$ 1072,00| R$ 1306,00| R$ 1892,00|
11|R$ 1045,00| R$ 1266,00| R$ 1804,00|
12|R$ 1007,00| R$ 1225,00| R$ 1635,00|
13|R$ 998,00| R$ 1202,00| R$ 1598,00|
14|R$ 958,00| R$ 1169,00| R$ 1602,00|
15|R$ 964,00| R$ 1145,00| R$ 1696,00|
16|R$ 962,00| R$ 1127,00| R$ 1545,00|
17|R$ 932,00| R$ 1103,00| R$ 1629,00|
18|R$ 947,00| R$ 1091,00| R$ 1456,00|
19|R$ 916,00| R$ 1077,00| R$ 1401,00|
20|R$ 912,00| R$ 1060,00| R$ 1356,00|