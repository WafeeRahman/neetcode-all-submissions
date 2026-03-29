class Solution:
    def simplifyPath(self, path: str) -> str:
        stack =[]

        i = 0
        while i < len(path):
            j=i
            while j < len(path) and path[j] == "/":
                j+=1
            
            i=j
            while j < len(path) and path[j] != "/":
                j+=1
            
            dirname = path[i:j]
            print(dirname)
            if dirname == "..":
                if stack:
                    stack.pop()
            elif dirname == ".":
                None
            else:
                if dirname != '':
                    stack.append(dirname)
            print(stack)
            
            i=j
        
        res = "/"
        for i in range(len(stack)):
            dirname = stack[i]
            if i!=len(stack)-1:
                res+=dirname+"/"
            else:
                res+=dirname
        
        return res


        