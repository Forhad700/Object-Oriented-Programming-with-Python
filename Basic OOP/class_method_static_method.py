class MathUtils:
    @classmethod
    def factorial(cls, n):
        if n==0:
            return 1
        else:
            return n * cls.factorial(n-1)
    
    @staticmethod
    def even(n):
        return n%2==0
    

print(MathUtils.factorial(4))
print(MathUtils.even(20))