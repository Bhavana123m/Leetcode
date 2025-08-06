class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_binary = ""
        while n>0:
            reverse_binary+=str((n%2))
            n = n//2
        reverse_binary += '0' * (32 - len(reverse_binary))

        result = 0
        reverse_binary = reverse_binary[::-1]
        for i in range(32):
            result+=int(reverse_binary[i])*(pow(2,i))
        return result

        # while