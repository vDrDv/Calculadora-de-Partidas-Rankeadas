# Calculadora de Partidas Ranqueadas

## Instruções para entrega

1. **O Que deve ser utilizado**
   - Variáveis
   - Operadores
   - Laços de repetição
   - Estruturas de decisões
   - Funções

## Objetivo

Criar uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador e, em seguida, retorna o resultado para uma variável. O saldo de Ranqueadas deve ser calculado por meio da fórmula (vitórias - derrotas).

   - Se o número de vitórias for menor que 10 = Ferro
   - Se o número de vitórias estiver entre 11 e 20 = Bronze
   - Se o número de vitórias estiver entre 21 e 50 = Prata
   - Se o número de vitórias estiver entre 51 e 80 = Ouro
   - Se o número de vitórias estiver entre 81 e 90 = Diamante
   - Se o número de vitórias estiver entre 91 e 100 = Lendário
   - Se o número de vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final, deve-se exibir uma mensagem:

"O Herói tem um saldo de **{saldoVitorias}** e está no nível de **{nivel}**."

## Exemplo de Uso

```python
# Exemplo de chamada da função
saldoVitorias = calcular_saldo_ranqueadas(75, 20)
print("O Herói tem um saldo de", saldoVitorias, "e está no nível de", obter_nivel(saldoVitorias))
