class Solution:
    value=0
    def romanToInt(self, ch: str) -> int:
        s = list(ch)
        Length = len(s)
        
        for i in range(Length):
            if s[i] == 'I' and i < Length-1:
                match s[i+1] :
                    case 'V':
                        self.value = self.value-1
                         
                    case "X": 
                        self.value=self.value-1
                         
                    case _ :
                        self.value=self.value+1
            elif s[i] == 'V' :
                self.value=self.value+5
            elif s[i] == 'X' and i < Length-1:
                match s[i+1] :
                    case 'L':
                        self.value = self.value-10
                        i=i+1
                    case "C": 
                        self.value=self.value-10
                        i=i+1
                    case _ :
                        self.value=self.value+10
            elif s[i] == 'L'  :
                self.value=self.value+50
            elif s[i] == 'C' and i < Length-1:
                match s[i+1] :
                    case 'D':
                        self.value = self.value-100
                         
                    case "M": 
                        self.value=self.value-100
                         
                    case _ :
                        self.value=self.value+100
            elif s[i] == 'D'  :
                self.value=self.value+500
            elif s[i] == 'M'  :
                self.value=self.value+1000
            elif i==Length-1 and(s[i]=="I" or s[i]=="X" or s[i]=="C"):
                match s[i]:
                    case 'I':
                        self.value=self.value+1
                    case 'X':
                        self.value=self.value+10
                    case 'C':
                        self.value=self.value+100

        print(self.value)
        return self.value
sol=Solution()
sol.romanToInt("LXLI")