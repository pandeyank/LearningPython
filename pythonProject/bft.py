

def bfs(self,v):
       graph= {'a': {'b'},
                'b': {'a'},
                'c': {'a', 'b'}
                }
       visited[v]=1
       q=[]
       q.append(v)

       while q:
              x=q.pop(0)
              print(x)
              for i in self.graph(x):
                     if visited[i]==0:
                            visited[i]==1
                            q.append(i)

bfs('a')
