# -*- coding: utf-8 -*-
"""
Created on Tue May 24 07:31:17 2022

@author: Salih Ömer Ongün
"""
my_name = "Salih Omer Ongun"
my_id = "200102002003"
my_email = "s.ongun2020@gtu.edu.tr"


class Graph():
    def __init__(self):
        self.adj={}
        self. vertices=None
        self.gtype=None
    def add_edge(self,u,v):
        if str(u) not in self.adj.keys():
            self.adj[u]=[]
        self.adj[u].append(v)  



def Dir_cyclic_or_acyclic(Graph):
    if Graph.gtype!="d":
        return None
    for i in Graph.vertices:
        path=[]
        myvert={}
        path.append(i)
        myvert[i]=[] 
        x=i
        while True:
            if Graph.adj[x]==None:
                path.pop()
                while True:
                    if path==[]:
                        break
                    if len(Graph.adj[path[-1]])<=len(myvert[path[-1]]):
                        path.pop()  
                    elif len(Graph.adj[path[-1]])>len(myvert[path[-1]]):
                        y=myvert[path[-1]][-1]
                        y1=Graph.adj[path[-1]].index(y)
                        x=Graph.adj[path[-1]][y1+1]
                        myvert[path[-1]].append(x)
                        path.append(x)
                        break        
            if path==[]:
                break
            if Graph.adj[x]==None:
                continue
            for j in path:
                if path.count(j)>1:
                    return True
            path.append(Graph.adj[x][0])
            if x not in myvert.keys():
                myvert[x]=[]
            if Graph.adj[x][0] not in myvert[x]:    
                myvert[x].append(Graph.adj[x][0])    
            x=Graph.adj[x][0]  
    return False   

    
def UnDir_cyclic_or_acyclic(Graph):
    if Graph.gtype!="u":
        return None
    for i in Graph.vertices:
        visited=[]
        pardict={}
        visited.append(i)
        pardict[Graph.adj[i][0]]=i
        x=Graph.adj[i][0]
        visited.append(x)
        while True:
            mystr="not detect"
            y=0
            for j in Graph.adj[x]:
                y+=1
                if j not in visited:
                    visited.append(j)
                    pardict[j]=x
                    x=j
                    mystr="detect"
                    break
                if y==len(Graph.adj[x]) and j in visited and pardict[x]!=j:
                    return True
            if mystr=="detect":
                continue
            elif mystr=="not detect":
                break                
    return False    

def T_sort(Graph):
    if Graph.gtype!="d" or Dir_cyclic_or_acyclic(Graph)!=False:
        return None
    path=[]
    visited=[]
    myadj={}
    for j in Graph.adj:
        if Graph.adj[j]!=None:
            myadj[j]=[]
    for i in Graph.vertices:
        if i in visited:
            continue
        if Graph.adj[i]==None:
            continue
        path.append(i)
        say=0
        yaz=""
        for j in Graph.adj[i]:
            say+=1
            if j not in visited:
                x=j
                break
            if say==len(Graph.adj[i]):
                yaz="not detect"
                break
        if yaz=="not detect":
            continue
        while True:
            write=""
            if x not in visited:
                path.append(x)
            if Graph.adj[x]==None:
                path.pop()
                visited.append(x)
                while True:
                    if path==[]:
                        break
                    say=0
                    write=""
                    for j in Graph.adj[path[-1]]:
                        say+=1
                        if j not in visited:
                            x=j
                            write="detect"
                            break
                        if say==len(Graph.adj[path[-1]]):
                            write="not detect"
                            visited.append(path[-1])
                            path.pop()
                        if write=="not detect":
                            break
                    if write=="detect":
                        break        
            if write=="detect":
                continue                
            if path==[]:
                break                
            if Graph.adj[path[-1]]!=None:
                say=0
                for j in Graph.adj[path[-1]]:
                    say+=1
                    if j not in visited:
                        x=j
                        break
                    if say==len(Graph.adj[path[-1]]):
                        visited.append(path[-1])
                        path.pop()
                        break
            if path==[]:
                break         
    visited.reverse()
    return visited      
            








