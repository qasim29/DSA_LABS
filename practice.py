# # nums = [2,4,8,2]

# # def get(nums):
# #     if(len(nums)>=3):
# #         i,j,k=0,1,2
# #         count=0
# #         temp1=k
# #         temp2=j
# #         while(i!=len(nums)-3):
# #             if(j==len(nums)-2):
# #                 j=temp2+1
# #                 temp2=j
# #                 i+=1
# #                 k-=1
# #             if(k==len(nums) and j<len(nums)-2):
# #                 k=temp1+1
# #                 temp1=k
# #                 j+=1

# #             if((nums[i]*nums[j]*nums[k])%2==0 and k>j>i):
# #                 count+=1
# #             k+=1
# #     return count


# # print(get(nums))











# class Stack:
#     def _init_(self):
#         self.list = []
#         self.count = 0
#     def push(self,val):
#         self.list.append(val)
#         self.count += 1
#     def pop(self):
#         if(self.count != 0):
#             self.count -= 1
#             return self.list.pop()
#     def size(self):
#         return self.count
#     def top(self):
#         if(self.size() != 0):
#             return self.list[-1]
#     def isEmpty(self):
#         if(self.size() == 0):
#             return True
#         else:
#             return False

# def main():
#     op = ['+','-','*','/','^','(',')']
#     lp = ['+','-']
#     hp1 = ['*','/']
#     hp2 = ['^']
#     hp3 = ['(']
#     stack = Stack()
#     string = input("Enter expression : ")
#     for i in string:
#         if((ord(i)>=65 and ord(i)<=90) or 
#           (ord(i)>=97 and ord(i)<=122) or 
#           (ord(i)>=48 and ord(i)<=57)):
#             print(i,end = " ")
#         elif(i in op ):
#             if(stack.isEmpty() or  stack.top() == '('):
#                 stack.push(i)
#             elif(stack.top() in lp and((i in hp1) or (i in hp2) or (i in hp3))):
#                 stack.push(i)
#             elif (stack.top() in hp1 and ((i in hp2) or (i in hp3))):
#                 stack.push(i)
#             elif (stack.top() in hp2 and (i in hp3)):
#                 stack.push(i)
#             elif(i in lp and (stack.top() in lp or stack.top() in hp1 or stack.top() in hp2)):
#                 while(stack.top() in lp or stack.top() in hp1 or stack.top() in hp2):
#                     print(stack.pop(),end = " ")
#                 stack.push(i)
#             elif(i in hp1 and (stack.top() in hp1 or stack.top() in hp2)):
#                 while(stack.top() in hp1 or stack.top() in hp2):
#                     print(stack.pop(),end = " ")
#                 stack.push(i)
#             elif(stack.top() in hp2 and i in hp2):
#                 stack.push(i)
#             elif(i == ')'):
#                 while(stack.top() != '('):
#                     print(stack.pop(),end = " ")
#                 stack.pop()
#         else:
#             print("Invalid expression")
#     i=0
#     while(i<=stack.size()):
#         print(stack.pop(), end=" ")
#         i+=1


# main()






class Stack:
    """(LIFO) queuing policy implemented using python list."""

    def __init__(self):
        self.list = []

    def push(self, item):
        """Push 'item' onto the stack."""
        self.list.append(item)

    def pop(self):
        """Pop the most recently pushed item from the stack."""
        return self.list.pop()

    def top(self):
        """Return the last element."""
        return self.list[-1]

    def is_empty(self):
        """Returns true if the stack is empty."""
        return len(self.list) == 0


def depth_first_search(graph, start):
    stack = Stack()
    stack.push(start)
    path = []

    while not stack.is_empty():
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.push(neighbor)

    return path


def main():
    adjacency_matrix = {
        1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [6],
        5: [6],
        6: [7],
        7: []
    }
    dfs_path = depth_first_search(adjacency_matrix, 1)
    print(dfs_path)


if __name__ == '__main__':
    main()
