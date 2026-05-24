class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #WRONG LOGIC - BUT INITIAL OWN PSEDOCODE: bcs i thought that the substr must be sorted l
        #like ascending, it can be just any substring within string which is non repepating chars


        #initialize l ptr at 0, r ptr at 1
        #count = 0
        #while(r <len(s)): 
        #   count=max(count, new_count)
            #check ascii of l,r chars: if ascii l>r, l=r then r++ and new_count+=1
            #if ascii of l<r, r++ and new_count+=1
            #if ascii l= ascii r then l=r then new_count+=1
        #return count


        charSet = set()
        l=0
        count=0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            
            charSet.add(s[r])
            count=max(count,r-l+1)

        return count

                

            


        







        