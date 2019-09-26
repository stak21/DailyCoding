 def reverse(self, x: int) -> int:
        temp = 0
        digit = 10
        signed = 1
        
        if x < 0:
            signed = -1
            x *= -1
            
        while x > 0:
            t = x % 10
            x //= 10
            temp *= digit
            temp += t
            
        temp *= signed
        if(abs(temp) > (2 ** 31 - 1)):
            return 0
        return temp
