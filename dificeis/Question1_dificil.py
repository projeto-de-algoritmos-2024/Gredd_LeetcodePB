class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0
        # Array para armazenar a quantidade de doces que cada criança receberá
        candies = [1] * n

        # Passo 1: Varredura da esquerda para a direita
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Passo 2: Varredura da direita para a esquerda
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Soma total dos doces
        return sum(candies)
        