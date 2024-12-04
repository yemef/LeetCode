# class myHouse:
#     def __init__(self,name):
#         self.toyname=name

#     def accessToKitchen(self):
#         print(f"hey there your key is {self.toyname}")

# house=myHouse("32_forest_view_key")
# a=house.accessToKitchen()
# print(a)

class Solution:
    def mergeAlternatively(self,word1: str,word2: str)-> str:
        i,j=0,0
        res=[]
        while i<len(word1) and j<len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)
    
solution=Solution()
ans=solution.mergeAlternatively("abc","def")
print(ans)
