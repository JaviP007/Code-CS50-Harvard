class Jar:
    def __init__(self, capacity=12,size=0):
        self.capacity=capacity
        self.size=size
    def __str__(self):
        return f"{self.size*'🍪'}"

    def deposit(self, n):
        if self.size+n>self.capacity:
            raise ValueError("Lleno")
        else:
            self.size=self.size+n
            return f"{self.size*'🍪'}"

    def withdraw(self, n):
        if self.size-n<0:
            raise ValueError("vacio")
        else:
            self.size=self.size-n
            return f"{self.size*'🍪'}"

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, value):
        if value <=0:
            raise ValueError("Mal")
        self._capacity = value

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,value):
        if value <0:
            raise ValueError("Mal")
        self._size=value


jar=Jar()

jar.deposit(5)

print(str(jar))
