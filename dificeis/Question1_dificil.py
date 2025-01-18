class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        if n == 0:
            return 0

        