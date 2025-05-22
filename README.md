# AED2: Problema da interseção eficiente entre dois arrays ordenados.

## Participantes
1. Camila Alves
2. Felipe Mitsuo
3. Eraldo Botelho
4. Clarissa Berlim
5. João Coutinho


## Introdução e Descrição do Problema
O trabalho teve como objetivo desenvolver um algoritmo eficiente para encontrar a interseção entre dois arrays ordenados. O problema consiste em identificar todos os elementos que aparecem simultaneamente em dois arrays ordenados. Foi fornecido um exemplo prático: para os arrays [1, 3, 4, 5, 7, 9, 11, 11] e [3, 5, 6, 7, 8, 9, 9, 11], o algoritmo deve retornar [3, 5, 7, 9, 11]. A implementação feita considerou versões com e sem repetição no resultado.

## Implementações
Duas versões do algoritmo foram desenvolvidas. A primeira permite a repetição de elementos na saída, refletindo a quantidade de vezes que aparecem em ambos os arrays. A segunda versão elimina repetições, garantindo que cada elemento comum apareça apenas uma vez na interseção resultante. Ambas as versões foram avaliadas quanto à sua eficiência.

## Análise Teórica - Teorema Mestre
A análise de complexidade do algoritmo foi feita utilizando o Teorema Mestre. A ideia central foi dividir o array A em duas partes e realizar busca binária no array B. Como cada nível da recursão faz duas chamadas e executa uma busca binária (complexidade O(log m)), obteve-se a recorrência:

T(n) = 2T(n/2) + O(log m)

Resultando em tempo total: T(n) = Θ (n.log m)

## Análise do Desempenho
Foram realizados testes com diferentes tamanhos de entrada, variando de 10 até 1.000.000 elementos. Os tempos de execução foram medidos para as duas versões do algoritmo. Observou-se que para entradas pequenas o tempo foi praticamente desprezível, mas para entradas grandes, a versão com repetição mostrou-se levemente mais eficiente até 100.000 elementos, sendo superada pela versão sem repetição a partir de 1.000.000 de elementos.

## Conclusão
A implementação e análise do algoritmo de interseção entre listas ordenadas permitiram compreender melhor os impactos de diferentes abordagens na eficiência computacional. A escolha entre permitir ou não repetições deve considerar o objetivo da aplicação. A análise teórica se mostrou coerente com os testes práticos, validando a utilização do Teorema Mestre na previsão da complexidade do algoritmo.


## Licença
Este projeto está licenciado sob a licença MIT.
