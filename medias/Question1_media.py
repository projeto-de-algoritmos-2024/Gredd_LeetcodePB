class Solution(object):
    def doesValidArrayExist(self, derived):
        n = len(derived)

    # O array `derived` determina restrições para o array original.
    # Vamos assumir que original[0] = 0 e simular o resto do array.

        def simulate_with_first_value(first_value):
            original = [0] * n
            original[0] = first_value

            # Derivar os elementos restantes de `original` com base em `derived`
            for i in range(1, n):
                original[i] = derived[i - 1] ^ original[i - 1]

            # Verificar se a condição circular é satisfeita
            return (original[-1] ^ original[0]) == derived[-1]

        # Verificar para os dois possíveis valores de original[0]
        return simulate_with_first_value(0) or simulate_with_first_value(1)

 
