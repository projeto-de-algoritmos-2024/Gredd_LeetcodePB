class Solution(object):
    def candy(self, ratings):
        # Array para armazenar os doces, com 1 doce para cada criança inicialmente.
        arr = [1] * len(ratings)

        # Passo 1: Faz a varredura da esquerda para a direita.
        # Para garantir que cada criança com rating maior que a anterior
        # receba mais doces que ela, seguindo uma ordem crescente de prioridade.
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                arr[i] = arr[i - 1] + 1

        # Passo 2: Faz a varredura da direita para a esquerda.
        # Para garantir que cada criança com rating maior que o próximo vizinho
        # receba mais doces que ele.
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # No caso aplicamos o conceito de resolução de conflitos (do Interval Scheduling),
                # onde o valor máximo é usado para reconciliar as duas "prioridades".
                arr[i] = max(arr[i], arr[i + 1] + 1)

        # Retorna a soma total de doces distribuídos.
        return sum(arr)
