class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        # Calcula o total de combustível disponível e o custo total.
        # Se o combustível total for menor que o custo total, a viagem não é possível.
        total_gas, total_cost = sum(gas), sum(cost)
        if total_gas < total_cost:
            return -1  # Retorna -1 para indicar que a viagem não é possível.

        # Inicializa em 0 o saldo de combustível acumulado (current_gas) e o ponto inicial (start).
        current_gas, start = 0, 0

        for i in range(len(gas)):
            # Atualiza o saldo de combustível no posto atual.
            current_gas += gas[i] - cost[i]

            # Verifica se o saldo ficou negativo, o que significa que houve um "atraso"
            if current_gas < 0:
                # Aqui foi onde aplicamos o conceito do "Minimize Lateness":
                # O "atraso" é resetado ao zerar o saldo acumulado e avançar o ponto de partida.
                start = i + 1
                current_gas = 0  # Zera o saldo acumulado para recomeçar do próximo posto.

        # Retorna o índice de início onde é possível completar o circuito.
        return start
