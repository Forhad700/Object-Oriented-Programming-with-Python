# # Public 
# class Encap:
#     a = 5

#     def display(self):
#         print("Public Class")

# e = Encap()
# print("a: ", e.a)
# e.display()



# Private 
class Encap:
    __a = 5

    def display(self):
        print("Hello")

e = Encap()
print("a: ", e.a)




# class Encap:
#     __a = 5

#     def display(self):
#         print("Hello")
#         print("a: ", self.__a)

# e = Encap()
# e.display()




# class Encap:
#     __a = 5

#     def __display(self):
#         print("Hello")

# e = Encap()
# e.display()