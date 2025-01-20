class Solution(object):
    def minPatches(self, nums, n):
        """
        Este método calcula o número mínimo de números adicionais (patches) 
        necessários para garantir que seja possível formar todos os números 
        do intervalo [1, n] usando os números disponíveis na lista nums.

        A lógica utilizada segue o conceito de *Coin Changing*, onde:
        - Os números disponíveis em nums são tratados como "moedas".
        - O objetivo é cobrir todos os valores no intervalo [1, n] usando 
          essas "moedas" e adicionando novas "moedas" (patches) quando necessário.

    
        """
        i, patches, covered = 0, 0, 0  # Inicializa índices e variáveis auxiliares.
        N = len(nums)  # Número total de elementos em nums.

        while covered < n:
            # coin representa o próximo valor mínimo que precisa ser coberto.
            coin = covered + 1

            if i < N and nums[i] <= coin:
                # Usa a "moeda" atual de nums para expandir o alcance.
                covered += nums[i]
                i += 1  # Avança para a próxima "moeda".
            else:
                # Adiciona um "patch" equivalente ao menor valor necessário.
                patches += 1
                covered += coin  # Expande o alcance com a "moeda fictícia".

        return patches