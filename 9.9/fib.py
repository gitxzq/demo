#-*-coding:utf-8-*-

# class fib():
#     def __init__(self):
#         self.a,self.b=0,1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a,self.b=self.b,self.a+self.b
#         if self.a>1000:
#             raise StopIteration()
#         return self.a

class fib(object):
    def __getitem__(self, item):
        if isinstance(item,int):
            a,b=1,1
            for x in range(item):
                a,b=b,a+b
            return a
        if isinstance(item,slice):
            start=item.start
            stop=item.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L


f=fib()
print(f[6])
print(f[0:6])


# for n in fib():
#     print(n)