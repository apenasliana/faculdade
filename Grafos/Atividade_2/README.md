
### Exercicio RunCodes (23981)

# Construção de Estradas

O arquipélogo de Isla Bonita (atenção: esse é um nome fictício), localizado no Caribe, é um país insular que conquistou a independência recentemente. Infelizmente, Isla Bonita tem uma rede de rodovias ainda muito aquém do ideal. O governo local está preocupado com essa questão, e pretende realizar investimentos em infraestrutura rodoviária pra promover o desenvolvimento desse novo país. De fato, Isla Bonita já possui uma pequena rede de transportes que liga algumas cidades, herança de seu passado colonial. Todavia, existem outras cidades proeminentes que não são acessíveis via rodovias. Diante disso, o gabinete governamental decidiu construir, inicialmente, estradas que garantam que seja possível deslocar-se, via veículos terrestres, entre todos os pares das principais cidades do país, sem ter que utilizar outro meio de transporte (aéreo ou marítimo).

Isla Bonita possui as cidades de interesse numeradas de 1 a n, e cada cidade i possui uma posição no plano cartesiano denotada por (xi, yi). Cada estrada conecta exatamente 2 cidades. Todas as estradas (as antigas e as que serão construídas) são desenhadas em linha reta, de forma que a distância entre as cidades seja dada pela distância Euclidiana entre pontos. Considere que as distâncias Euclidianas sejam arredondadas. Sugestões podem ser vistas em C++ e em Python. Os motoristas podem se deslocar em ambos os sentidos das estradas (novas e antigas). As estradas podem se cruzar livremente entre elas. No entanto, um motorista poderá mudar da estrada A para a estrada B em uma cidade i que ele está localizado se i coincidir com o fim das estradas A e B.

O governo de Isla Bonita pretende realizar tais obras economizando o máximo de recursos. No entanto, o plano de desenvolvimento do país garante que cada cidade principal seja alcançável via transporte terrestre. Levando em conta que o custo de construção de uma rodovia é diretamente proporcional à distância entre o par de cidades que as liga, sua tarefa consiste em auxiliar os governantes de Isla Bonita à propor as ligações mais econômicas para a ilha, conectando todas as cidades principais e considerando as rodovias que já existem como fixas.

## Entrada
Cada caso de teste é composto por duas partes. Na primeira parte, descreve-se a posição no plano cartesiano de cada cidade de interesse, enquanto na segunda parte, destaca-se as cidades que já possuem ligação por meio de estrada.

Na primeira linha, indica-se o número de cidades principais n (1 ≤ n ≤ 750). As próximas n linhas contém dois inteiros, xi e yi, separados por um espaço em branco. Esses valores representam as coordenadas cartesianas de cada cidade i, i=1,...,n. Para os testes, considera-se que 0 ≤ |xi| ≤ 10.000 e 0 ≤ |y_i| ≤ 10.000. Cada cidade tem uma localização única.

A próxima linha contém o número de estradas já existentes, representado pelo número m (0 ≤ m ≤ 1.000). As próximas m linhas contém um par de inteiros separados por espaço. Cada par de inteiros indica o íncide de cada cidade conectada por uma estrada.

## Saída
A saída de seu programa deve ter o custo das novas estradas que devem ser construídas, a fim de promover a alcançabilidade entre cidades principais de Isla Bonita, minimizando o custo total.

## Exemplos

### Entrada
```
9
1 5
0 0
3 2
4 5
5 1
0 4
5 2
1 2
5 3
3
1 3
9 7
1 2
```
### Saída

```
8
```