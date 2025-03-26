# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 07:37:38 2022

@author: Salih Ömer Ongün
"""

my_name = "Salih Omer Ongun"
my_id = "200102002003"
my_email = "s.ongun2020@gtu.edu.tr"

import avlgtu

import time

import bstgtu



def reltime(t,tbase='070000'):
    if tbase[0]==0:    
        a=int(tbase[1])
    elif tbase[0]!=0:
        a=int(tbase[0:2])
    if tbase[2]==0:    
        b=int(tbase[3])
    elif tbase[2]!=0:
        b=int(tbase[2:4])
    if tbase[4]==0:    
        c=int(tbase[5])
    elif tbase[4]!=0:
        c=int(tbase[4:6])
    sntbase=a*3600+b*60+c
    if t[0]==0:    
        a1=int(t[1])
    elif t[0]!=0:
        a1=int(t[0:2])
    if t[2]==0:    
        b1=int(t[3])
    elif t[2]!=0:
        b1=int(t[2:4])
    if t[4]==0:    
        c1=int(t[5])
    elif t[4]!=0:
        c1=int(t[4:6])
    snt=a1*3600+b1*60+c1
    return snt-sntbase    


def read2tree(filename, TreeType,tbase='070000', tceil='220000'):
    a=[]
    c=[]
    if TreeType=="BST": 
        m=bstgtu.BST()
    if TreeType=="AVL":
        m=avlgtu.AVL()
    with open(filename,"r") as f:
        for i in f:
            b=i.strip("\n").split()
            c.append(b)
            x=reltime(b[0],tbase)
            a.append(x)
    for i in range(0,len(a)):
        m.insert(a[i])
        node=m.find(a[i])
        node.gtu=float(c[i][1])
    return m



def maximum(node):
    if node.right!=None:
        while True:
            if node.right!=None:
                node=node.right
                continue
            else:
                return node
    else:
        return node


def predecessor(node):
    k=node
    if node.left!=None:
        node=node.left
        while True:
            if node.right!=None:
                node=node.right
                continue
            else: 
                return node
    else:
        while True:
            if k.parent.key!=None:
                k=k.parent
                continue
            else:
                if node==k.minimum():
                    return None
                else:
                    break
        if node.parent.key!=None:
            while True:
                if node.parent.key>node.key:
                    node=node.parent
                    continue
                else:
                    return node.parent


def writelist(tree,tlo=None,thi=None,tbase="070000",tceil="220000"):
    if tlo==None:
        tlo=tbase
    if thi==None:
        thi=tceil
    p=reltime(tlo,tbase)
    p1=reltime(thi,tbase)    
    x=[]
    a=tree.root
    b=a.minimum()
    if b.key>=p and b.key<=p1:    
        x.append(b.key)
    while True:
       if b.successor().key!=None: 
           c=b.successor()
           b=c
           if c.key>=p and c.key<=p1:
               x.append(c.key)
       else:
           break
    return x  

def dyna_int_updater(IntValue,tdo,tup,innode,nxsmaller,nxlarger):
    if nxsmaller!=None and nxlarger.key!=None:
        newınt=IntValue+(nxlarger.key-innode.key)*(innode.gtu-nxsmaller.gtu)/3600
    elif nxsmaller!=None and nxlarger.key==None:
        newınt=IntValue+(tup-innode.key)*(innode.gtu-nxsmaller.gtu)/3600
    elif nxsmaller==None and nxlarger.key!=None:
        newınt=IntValue+(nxlarger.key)*(innode.gtu-nxlarger.gtu)/3600  
    elif nxsmaller==None and nxlarger.key==None:
        newınt=IntValue+((tup-tdo)*innode.gtu/3600)
    return newınt 


def mydyna_int_updater(IntValue,tdo,tup,innode,nxsmaller,nxlarger,tbase="070000",tceil="220000"):
    p=reltime(tup,tbase)
    p1=reltime(tdo,tbase)
    if nxsmaller!=None and nxlarger.key!=None:
        newınt=IntValue+(nxlarger.key-innode.key)*(innode.gtu-nxsmaller.gtu)/3600
    elif nxsmaller!=None and nxlarger.key==None:
        newınt=IntValue+(p-innode.key)*(innode.gtu-nxsmaller.gtu)/3600
    elif nxsmaller==None and nxlarger.key!=None:
        newınt=IntValue+(nxlarger.key-p1)*(innode.gtu-nxlarger.gtu)/3600  
    elif nxsmaller==None and nxlarger.key==None:
        newınt=IntValue+((p-p1)*innode.gtu/3600)
    return newınt  


def GTU_tree_rad_calc(MTree, tlo=None,thi=None, tbase="070000",tceil="220000"):
    if tlo==None:
        tlo=tbase
    if thi==None:
        thi=tceil
    m=time.perf_counter_ns()
    p=reltime(tlo,tbase)
    p1=reltime(thi,tbase)
    x=writelist(MTree,tlo,thi,tbase,tceil)
    a=0
    b=[]
    for i in range(0,len(x)):
        if len(x)!=1:
            if i==0:
                k=(x[1]-p)*MTree.find(x[0]).gtu
                a+=k/3600
                b.append(a)
                continue
            elif i!=len(x)-1 and i!=0:
                k=(x[i+1]-x[i])*MTree.find(x[i]).gtu
                a+=k/3600
                b.append(a)
            elif i==len(x)-1:
                k1=p1-x[-1]
                k=k1*MTree.find(x[-1]).gtu
                a+=k/3600
                b.append(a)
        elif len(x)==1:
            k1=reltime(thi,tlo)
            k=k1*MTree.find(x[0]).gtu
            a+=k/3600
            b.append(a)
    n=time.perf_counter_ns()        
    return a,b,n-m
         
def GTU_tree_dyna_add(filename, MTree,IntValue=0, tlo=None, thi=None,tbase="070000", tceil="220000"):
    a=[]
    c=[]
    d=[]
    if tlo==None:
        tlo=tbase
    if thi==None:
        thi=tceil
    p=reltime(tlo,tbase)
    p1=reltime(thi,tbase)    
    m=time.perf_counter_ns()    
    with open(filename,"r") as f:
        for i in f:
            b=i.strip("\n").split()
            c.append(b)
            x=reltime(b[0],tbase)
            a.append(x)
    for i in range(0,len(a)):
        if a[i]<p or a[i]>p1:
            continue
        else:
            MTree.insert(a[i])
            node=MTree.find(a[i])
            node.gtu=float(c[i][1])
            x=GTU_tree_rad_calc(MTree,tlo,thi,tbase,tceil)[0]
            IntValue=x
            d.append(IntValue)
    n=time.perf_counter_ns()  
    return d[-1],d,n-m   


def GTU_int_calc(filename, TreeType,tlo=None, thi=None,tbase="070000", tceil="220000"):
    s=time.perf_counter_ns()
    if tlo==None:
        tlo=tbase
    if thi==None:
        thi=tceil    
    p=reltime(tlo,tbase)
    p1=reltime(thi,tbase)    
    a=[]
    c=[]
    d=[]
    value=0
    if TreeType=="BST": 
        m=bstgtu.BST()
    if TreeType=="AVL":
        m=avlgtu.AVL()
    with open(filename,"r") as f:
        for i in f:
            b=i.strip("\n").split()
            c.append(b)
            x=reltime(b[0],tbase)
            a.append(x)
    for i in range(0,len(a)):
        if a[i]<p or a[i]>p1:
            continue
        else:
            m.insert(a[i])
            node=m.find(a[i])
            node.gtu=float(c[i][1])   
            value=mydyna_int_updater(value, tlo, thi, node, predecessor(node), node.successor(),tbase,tceil)
            d.append(value)
    n=time.perf_counter_ns()    
    return d[-1],d,n-s     






