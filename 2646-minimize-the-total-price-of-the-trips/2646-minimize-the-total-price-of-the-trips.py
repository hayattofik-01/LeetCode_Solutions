class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        cnt=defaultdict(int)
        g=defaultdict(list)
        for x,y in edges:
            # print(x,y)
            g[x].append(y)
            g[y].append(x)
        def bfs(to,fro):
            q=deque([to])
            par=[None]*n
            par[to]=-1
            while q:
                t=q.popleft()
                for i in g[t]:
                    if par[i]==None:
                        par[i]=t
                        q.append(i)
            tt=fro
            while tt!=-1:
                cnt[tt]+=1
                tt=par[tt]
        for x,y in trips:
            bfs(x,y)
        for i in range(n):
            price[i]=cnt[i]*price[i]
        # print(price)
        def dfs(node,par):
            ans=[price[node]//2,price[node]] #cur half , not half
            for i in g[node]:
                if i!=par:
                    hlf,nhlf=dfs(i,node)
                    ans[0]+=nhlf
                    ans[1]=min(ans[1]+hlf,ans[1]+nhlf)
            return ans
        return min(dfs(0,-1))
        return 0