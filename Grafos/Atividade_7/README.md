### Exercicio Beecrowd (2440)

# Famílias de Troia


A Guerra de Troia pode ter sido um grande conflito bélico entre gregos e troianos, possivelmente ocorrido entre 1300 a.C. e 1200 a.C. (fim da Idade do Bronze no Mediterrâneo). Recentemente foram encontradas inscrições numa caverna a respeito de sobreviventes. Após um trabalho árduo, arqueólogos descobritam que as incrições descreviam relações de parentesco numa certa população. Cada item da inscrição indicavam duas pessoas que pertenciam a uma mesma família. 

Seu problema é determinar quantas famílias distintas existem.




### Entrada

O arquivo de entrada consiste de M + 1 (1 ≤ M ≤ 105) linhas. A primeira linha do arquivo de entrada contém um inteiro positivo N (1 ≤ N ≤ 5 x 104), que indica o número de elementos da comunidade, numerados de 1 a N. As demais M linhas do arquivo de entrada contêm, cada uma, dois inteiros. Cada inteiro identifica um elemento da comunidade. Cada linha indica que os dois indivíduos pertencem a uma mesma família.



### Saída


A saída deve conter apenas uma linha contendo um único inteiro, que é o número de famílias.



## Exemplo:

### Entrada 1:

```
4 4
1 2
2 3
3 4
4 1

```
______________
### Saída 1:
```
1

```

### Entrada 2:

```
8 10
1 2
2 3
3 6
6 5
5 4
4 3
6 7
7 8
8 1
1 5

```
______________
### Saída 2:
```
1

```

### Entrada 3:

```
9 8
1 2
2 3
3 6

```
______________
### Saída 3:
```
3

```