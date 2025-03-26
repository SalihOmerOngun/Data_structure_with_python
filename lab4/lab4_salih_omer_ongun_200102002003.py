# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:36:32 2022

@author: Salih Ömer Ongün
"""

my_name = "Salih Omer Ongun"
my_id = "200102002003"
my_email = "s.ongun2020@gtu.edu.tr"

import hashlib

import avlgtu

import bstgtu

from collections import deque

class Graph():
    def __init__(self):
        self.adj={}
        
    def add_edge(self,u,v):
        if str(u) not in self.adj.keys():
            self.adj[u]=[]
        self.adj[u].append(v)   
        
class BFSResult():
    def __init__(self):
        self.level={}
        self.parent={}    
        
def problem1(filename):
    c=[]
    k=[]
    for i in range(0,4096):
        m=avlgtu.AVL()
        k.append(m)
    with open(filename,"r") as f:
        for i in f:
            b=i.strip("\n").split()
            c.append(b)
            x=str(b[0])+str(b[1])+str(b[2])
            x1=hashlib.md5(str(x).encode("utf-8")).hexdigest()
            x2=x1[-3:]
            x3=int(str(x2),16)
            k[x3].insert(x)
            y=k[x3].find(x)
            y.color=b[3]
            y.fuel=b[4]
            y.engine=b[5]
    return k        
        
def problem2(vertices,edg):
    m=Graph()
    vertlist=[]
    for i in edg:
        for j in i:
            if j not in vertlist:
                vertlist.append(j)
    for i in vertlist:
        for j in edg:
            if i in j:
                if j.index(i)==0:
                    m.add_edge(j[0], j[1])
                if j.index(i)==1:    
                    m.add_edge(j[1], j[0]) 
    return m               
              
                
def problem3(vertices,edg):
    m=Graph()
    vertlist=[]
    for i in edg:
        for j in i:
            if j not in vertlist:
                vertlist.append(j)
    for i in vertlist:
        k=0
        for j in edg:
            k+=1
            if i in j:
                if j.index(i)==0:
                    m.add_edge(j[0], j[1])
            if k==len(edg) and i not in m.adj.keys():
                m.adj[i]=None
    return m                            
            
def problem4(g,s):
    r=BFSResult()
    r.parent={s:None}
    r.level={s:0}
    queue=deque()
    queue.append(s)
    while queue:
        u=queue.popleft()
        if g.adj[u]==None:
            continue
        for n in g.adj[u]:
            if n not in r.level:
                r.parent[n]=u
                r.level[n]=r.level[u]+1
                queue.append(n)
    return r 

def problem5(vert,edg,s,o,ty="u"):
    sourcelist=[]
    if ty=="d":
        g=problem3(vert, edg)
        b=problem4(g,s)
        sourcelist.append(o)
        if o not in b.level.keys():
            return "INF212"
        while True:
            sourcelist.append(b.parent[o])
            k=b.parent[o]
            o=k
            if s in sourcelist:
                sourcelist.reverse()
                return sourcelist
            if s not in sourcelist and None in sourcelist:
                return "INF212"
    if ty=="u":
        g=problem2(vert, edg)
        b=problem4(g,s)
        sourcelist.append(o)
        while True:
            sourcelist.append(b.parent[o])
            k=b.parent[o]
            o=k
            if s in sourcelist:
                sourcelist.reverse()
                return sourcelist
            if s not in sourcelist and None in sourcelist:
                return "INF212"   
    else:
        return None         
