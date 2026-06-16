class Solution:
    def processStr(self, s: str) -> str:
        result=""
        for i in s:
            if i.islower():
                result+=i
            elif(i=="*"):
                result= result[:-1]
            elif(i=="#"):
                k= result
                result+=k
            else:
                result= "".join(reversed(result))
        return result