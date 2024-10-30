import numpy as np
import os
import sys
from scipy.stats import sem
import matplotlib.pyplot as plt
import matplotlib
def HDX(ps, bk, nt, pa, kdd):

    import os
    ps=open(ps)
    ps =ps.read()
    ps=ps.split('\n')
    print(ps)
    r1=[]
    for i in ps:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        r1.append(x)
    bk=open(bk)
    bk = bk.read()
    bk=bk.split('\n')
    r2=[]
    for i in bk:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        r2.append(x)
    nt=open(nt)
    nt =nt.read()
    nt=nt.split('\n')
    r3=[]
    for i in nt:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        r3.append(x)
    pa=open(pa)
    pa = pa.read()
    pa=pa.split('\n')
    r4=[]
    for i in pa:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        r4.append(x)
    kdd=open(kdd)
    kdd = kdd.read()
    kdd=kdd.split('\n')
    r5=[]
    for i in kdd:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        r5.append(x)
    r1.pop()
    r2.pop()
    r3.pop()
    r4.pop()
    r5.pop()
    print(r3)
    x1_in=np.array(r1)
    x2_in=np.array(r2)
    x3_in=np.array(r3)
    x4_in=np.array(r4)
    x5_in=np.array(r5)
    x1=x1_in[:,0]
    x2=x2_in[:,0]
    x3=x3_in[:,0]
    x4=x4_in[:,0]
    x5=x5_in[:,0]
    x3=np.array(x3-370)
    y1=x1_in[:,1]
    y2=x2_in[:,1]
    y3=x3_in[:,1]
    y4=x4_in[:,1]
    y5=x5_in[:,1]
    
    plot4(x1, x2, x3, x4, x5, y1, y2, y3, y4, y5)

def plot4(x1, x2, x3, x4, x5, y1, y2, y3, y4, y5):
        fig, ax1=plt.subplots(figsize=(6,5))
        plt.plot(x1, y1, linestyle='', linewidth=2 ,markersize=6, color='black', marker='^', label='PS')
        plt.plot(x2, y2, linestyle='', markersize=6,linewidth=2 , color='blue', marker='o',label='BK')
        plt.plot(x3, y3, linestyle='', markersize=6,linewidth=2 , color='red', marker='s',label='Nt17')
        plt.plot(x4, y4, linestyle='', markersize=6,linewidth=2 , color='brown', marker='*',label='PA')
        plt.plot(x5, y5, linestyle='', markersize=6,linewidth=2 , color='green', marker='x',label='KDD')
        plt.xlabel('Residue ID', weight='bold', fontsize=16)
        plt.ylabel('Dihedral /(Omega)', weight='bold', fontsize=16)
        plt.xticks(weight='bold', fontsize=16)
        plt.xticks(np.arange(min(x1), max(x1)+1, 2))
        plt.yticks(weight='bold',  fontsize=16)
        plt.tick_params(width=2)
        lp = {'weight':'bold'}
        plt.legend(fontsize=16, prop=lp, loc='upper right', frameon=False)
        #plt.title(t, weight='bold', fontsize=14, loc='left')
        resolution=720
        #f1=f1
        [x.set_linewidth(2.0) for x in ax1.spines.values()]
        plt.savefig('OmegaDihedral.png', format="png", dpi=resolution)
        
        plt.show()




if __name__ == '__main__':
    ps='omega_polyS_rc.dat'
    #bk='bk_s1_1-500_bb_shpdG_8.3.dat'
    bk='omega_bk_rc.dat'
    nt='omega_nt17_rc.dat'
    pa='omega_PA_rc.dat'
    kdd='dkdd_omega.dat'

    HDX(ps,bk,nt,pa,kdd)

    


    
