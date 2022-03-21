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

5. Uma loja de tintas possui galões de 18 litros que custam R$80.00 a unidade, e latas de 3.6 litros que custam R$25.00 a unidade. É conhecido que essa marca de tintas consome aproximadamente um litro para cada 6 metros quadrados de parede. Considere que um cliente da loja apresenta uma `área` a ser pintada, e que, por segurança, adotamos 10% de margem de segurança, ou seja, compramos sempre, pelo menos, 10% a mais de tinta do que o suficiente para cobrir `área`. Desenvolva um algoritmo para um procedimento `otimiza_tinta` que receba `area` e determine a melhor combinação de galões e latas a serem compradas, de forma que o preço seja sempre o menor.

**SOLUÇÃO:** Rapidamente podemos identificar que um galão (R$4.44/litro) é mais econômico que uma lata (R$6,94/litro). Além disso, vemos que se estivermos falando de um valor superior a 10.8 litros (3 latas) e inferior a 18 litros, também é mais vantajoso comprar um galão. Portanto, precisamos comprar quantos galões inteiros forem necessários, e obter o que restar. Desse resto, compramos em latas até um total de 10.8 litros, ou adicionamos mais um galão à nossa conta. Colocando no formato de um algoritmo, temos o seguinte:

```
PROCEDIMENTO otimiza_tinta(area)
-----------------------------
# Entrada: parâmetro area é um número positivo.
# Saída: um par [g, l], indicando o número de galões e 
#   latas necessários para compra, respectivamente.
-----------------------------
1. Atribua 1.1 * area / 6 para a variável tinta.
2. Atribua a parte inteira da operação tinta / 18 para a variável galoes.
3. Atribua tinta - galoes * 18 para a variável tinta.
4. Se tinta < 10.8, faça:
  4.1. Atribua tinta / 3.6, arredondando para cima, para a variável latas.
5. Senão, faça:
  5.1. Atribua galoes + 1 para a variável galoes.
  5.2. Atribua 0 para a variável latas.
6. Encerre o procedimento e retorne o par [galoes, latas].
```

6. Desenvolva um procedimento `inverte_arranjo` que inverta os elementos de um arranjo `A`, de índice máximo `n`. Por exemplo, o retorno do procedimento com um arranjo `[1, 2, 3]` seria `[3, 2, 1]`.

**SOLUÇÃO:** Para que o algoritmo não inverta o arranjo duas vezes, é necessário que a estrutura de repetição só vá até o meio do arranjo. Observe que, se o arranjo possui um número ímpar de elementos (ou seja, se `n` é par), não precisamos executar o algoritmo de troca para o elemento do meio. Para executar a troca, criamos uma variável `temp`, que armazena um dos valores para que a troca seja possível.

```
PROCEDIMENTO inverte_arranjo(A, n)
-----------------------------
# Entrada:
#   - A: um arranjo de números.
#   - n: o valor do maior índice de A, maior que zero.
# Saída: o arranjo A, com os elementos invertidos.
-----------------------------
1. Atribua para x a parte inteira de n / 2.
2. Se n é par, atribua x - 1 para a variável x.
3. Para cada i = 0, 1, ..., x faça:
  3.1. Atribua A[i] para uma variável temp.
  3.2. Atribua A[n - i] para A[i].
  3.3. Atribua temp para A[n - i].
4. Encerre o procedimento e retorne A.
```

7. Elabore um procedimento que implemente o algoritmo de **busca binária**, aplicado para localizar valores em arranjos ordenados. O procedimento deve devolver o índice do arranjo em que foi encontrado o valor, ou -1 caso o valor não tenha sido encontrado. O conceito do algoritmo é o seguinte:

    * Para um determinado arranjo, vá até o meio deste e leia o valor do elemento.
    * Se o valor procurado for igual ao valor do elemento, encerre a busca.
    * Se o valor procurado for maior que o valor do elemento, continue procurando na metade maior do arranjo.
    * Se o valor procurado for menor que o valor do elemento, continue procurando na metade menor do arranjo.
    * Se todo o arranjo tiver sido percorrido e não for encontrado o valor, retorne um erro.

Considere por exemplo o arranjo `[1, 4, 5, 16, 20, 25, 33]` e queremos procurar um valor `4`. Temos a seguinte execução:

* Olhamos para o meio do arranjo, ou `16`.
* `4` é menor que `16`,  então continuamos procurando na primeira parte do arranjo, `[1, 4, 5]`.
* Agora olhamos para a metade da primeira parte do arranjo, que seria `4`.
* `4` é igual a `4`, então retornamos esse valor e encerramos a busca.

```
PROCEDIMENTO busca_binaria(A, inicio, fim, x)
-----------------------------
# Entrada:
#   - A: um arranjo de números.
#   - inicio: índice em que o algoritmo deve buscar no arranjo.
#   - fim: índice até onde o algoritmo deve buscar no arranjo.
#   - x: o valor a ser procurado.
# Saída: O índice em que o valor foi localizado, ou -1 caso
#   o valor não tenha sido encontrado.
-----------------------------
1. Atribua para y a parte inteira de (inicio + fim) / 2.
2. Se A[y] = x, encerre o procedimento e retorne y.
3. Se inicio = fim, encerre o procedimento e retorne -1.
4. Se A[y] < x, então faça:
  4.1. Encerre o procedimento e retorne busca_binaria(A, y + 1, fim, x).
5. Encerre o procedimento e retorne busca_binaria(A, inicio, y - 1, x).
```
