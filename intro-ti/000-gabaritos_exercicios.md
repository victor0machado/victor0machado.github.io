# Gabaritos dos exercícios resolvidos

### Índice

* [Nota de aula 02](#nota-de-aula-02-algoritmos-e-lógica-de-programação002-algoritmosmd)

## [Nota de aula 02: Algoritmos e Lógica de Programação](./002-algoritmos.md)

1. Faça um procedimento `maior` que receba dois números e retorne o maior deles.

**SOLUÇÃO:** Veja que não usamos aqui a instrução "senão", uma vez que, se o `x` for maior que `y`, o procedimento já é encerrado e nunca executará a instrução 2.

```
PROCEDIMENTO maior(x, y)
-----------------------------
# Entrada: parâmetros x e y são números.
# Saída: o maior dentre x e y.
-----------------------------
1. Se x > y, encerre o procedimento e retorne x.
2. Encerre o procedimento e retorne y.
```

2. Faça um procedimento `fatorial` que receba um número (assumindo inteiro positivo) e devolva o fatorial dele.

**SOLUÇÃO:** A lógica aqui é que o fatorial de um número é igual ao produto de todos os inteiros, de 1 até o número. Existem algoritmos mais elegantes que essa solução, incluindo recursividade, mas para o propósito desta aula, este algoritmo é preciso e eficiente o suficiente.

```
PROCEDIMENTO fatorial(x)
-----------------------------
# Entrada: parâmetro x é um número inteiro positivo.
# Saída: o fatorial de x.
-----------------------------
1. Atribua 1 para a variável fat.
2. Para i = 1 até x, faça:
  2.1. Atribua i * fat para a variável fat.
3. Encerre o procedimento e retorne fat.
```

3. Faça um procedimento `maximo` que receba um arranjo de números e o número de elementos deste arranjo e retorne o maior valor contido no arranjo.

**SOLUÇÃO:** Podemos aqui fazer algo parecido com o algoritmo `busca_linear` que temos na nota de aula. No entanto, ao contrário do algoritmo de busca, este sempre retorna um elemento do arranjo e não pode ter menos que `n` iterações (descontando a iteração do primeiro elemento, que está sendo feita na instrução 1).

```
PROCEDIMENTO maximo(A, n)
-----------------------------
# Entrada:
#   - A: um arranjo de números.
#   - n: o valor do maior índice de A, maior que zero.
# Saída: o elemento de maior valor contido em A.
-----------------------------
1. Atribua A[0] para a variável max.
2. Para i = 1 até n, faça:
  2.1. Se A[i] > max, atribua A[i] para max.
3. Encerre o procedimento e retorne max.
```

4. Faça um procedimento `contagem_regressiva` que receba um número (assumindo inteiro positivo) e exiba na tela uma contagem regressiva deste número até zero, inclusive.

**SOLUÇÃO:** Podemos usar aqui tanto a instrução "enquanto" quanto a instrução "para cada". Preferi usar a enquanto para não precisar criar novas variáveis dentro do procedimento.

```
PROCEDIMENTO contagem_regressiva(x)
-----------------------------
# Entrada: parâmetro x é um número inteiro positivo.
# Saída: Nenhuma.
-----------------------------
1. Enquanto x >= 0, faça:
  1.1. Exiba x na tela.
  1.2. Atribua o valor x - 1 a x.
3. Encerre o procedimento.
```
