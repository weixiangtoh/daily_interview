"""
Given a string with the initial condition of dominoes, where:

. represents that the domino is standing still
L represents that the domino is falling to the left side
R represents that the domino is falling to the right side

Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

Example:
Input:  ..R...L..R.
Output: ..RR.LL..RR
Here is your starting point:

class Solution(object):
  def pushDominoes(self, dominoes):
    # Fill this in.

print Solution().pushDominoes('..R...L..R.')
# ..RR.LL..RR
"""
class Solution(object):
    def pushDominoes(self, dominoes):
        # Fill this in.
        # while True:
        #     result = dominoes.replace("R.L", "...").replace(".L", "LL").replace("R.","RR")
        #     if result == dominoes:
        #         break
        #     else:
        #         result = dominoes

        # return result
        
        pi,pv,ans = 0,'.',''

        for i,v in enumerate(list(dominoes)):
            if v !='.':
                if v=='L':
                    if pv == 'R':
                        ans = ans[:-1] + 'R'*((i-pi+1)//2)
                        if (i-pi+1)%2 == 1:
                            ans += ('.')
                        ans += 'L'*((i-pi+1)//2)   
                    elif pv == '.':
                        ans += 'L'*(1+i-pi)
                    else:
                        ans += 'L'*(i-pi)
                else: 
                    ans += 'R'*(i-pi) if pv=='R' else ( ('.'*(i-pi))+'R' if pv == '.' else ('.'*(i-pi-1))+'R')
                pi,pv = i,v
        return ans + ( 'R'*(i-pi) if pv == 'R' else ('.'*(i-pi + 1) if pv == '.' else '.'*(i-pi) ) )

print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR