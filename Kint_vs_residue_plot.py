import numpy as np
import os
import sys
from scipy.stats import sem
import matplotlib.pyplot as plt
import matplotlib
def HDX(ps, bk, nt, pa, kdd,ps1,bk1,nt1,pa1,kdd1):

    import os
    ps=open(ps)
    ps =ps.read()
    ps=ps.split('\n')
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
    ps1=open(ps1)
    ps1 =ps1.read()
    ps1=ps1.split('\n')
    r11=[]
    for i in ps1:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        r11.append(x)
    bk1=open(bk1)
    bk1 = bk1.read()
    bk1=bk1.split('\n')
    r21=[]
    for i in bk1:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        r21.append(x)
    nt1=open(nt1)
    nt1 =nt1.read()
    nt1=nt1.split('\n')
    r31=[]
    for i in nt1:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        r31.append(x)
    pa1=open(pa1)
    pa1 = pa1.read()
    pa1=pa1.split('\n')
    r41=[]
    for i in pa1:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        r41.append(x)
    kdd1=open(kdd1)
    kdd1 = kdd1.read()
    kdd1=kdd1.split('\n')
    r51=[]
    for i in kdd1:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        r51.append(x)
    r11.pop()
    r21.pop()
    r31.pop()
    r41.pop()
    r51.pop()
    y1=np.array(r11)
    y2=np.array(r21)
    y3=np.array(r31)
    y4=np.array(r41)
    y5=np.array(r51)

    plot4(x1, x2, x3, x4, x5, y1, y2, y3, y4, y5)

def plot4(x1, x2, x3, x4, x5, y1, y2, y3, y4, y5):
        fig, ax1=plt.subplots(figsize=(6,5))
        plt.plot(x1, y1, linestyle='--', linewidth=2.5 ,markersize=6, color='black', marker='^', label='PS')
        plt.plot(x2, y2, linestyle='--', markersize=6,linewidth=2.5 , color='blue', marker='o',label='BK')
        plt.plot(x3, y3, linestyle='--', markersize=6,linewidth=2.5 , color='red', marker='s',label='Nt17')
        plt.plot(x4, y4, linestyle='--', markersize=6,linewidth=2.5 , color='brown', marker='*',label='PA')
        plt.plot(x5, y5, linestyle='--', markersize=6,linewidth=2.5 , color='green', marker='x',label='KDD')
        plt.xlabel('Residue ID', weight='bold', fontsize=18)
        plt.ylabel('Intrinsic Rate (/s)', weight='bold', fontsize=18)
        plt.xticks(weight='bold', fontsize=18)
        plt.xticks(np.arange(min(x1), max(x1)+1, 2))
        plt.yticks(weight='bold',  fontsize=18)
        plt.tick_params(width=2.0)
        lp = {'weight':'bold'}
        plt.legend(fontsize=18, prop=lp, loc='upper right', frameon=False, bbox_to_anchor=(0.95,1.1), ncol=5)
        #plt.title(t, weight='bold', fontsize=14, loc='left')
        resolution=720
        plt.tight_layout()
        #f1=f1
        [x.set_linewidth(2.0) for x in ax1.spines.values()]
        plt.savefig('kint.png', format="png", dpi=resolution)
        
        plt.show()




if __name__ == '__main__':
    ps='pS_s2_1-500_bb_shpdG_8.3.dat'
    bk='bk_s1_1-500_bb_shpdG_8.3.dat'
    nt='nt17_s1_1-500_bb_shpdG_8.3.dat'
    pa='polyA_s3_1-500_bb_shpdG_8.3.dat'
    kdd='kdd_s1_1-500_bb_shpdG_8.3.dat'
    
    ps1='ps_6.5_30_data.txt'
    bk1='bk_6.5_30_data.txt'
    nt1='nt_6.5_30_data.txt'
    pa1='pA_6.5_30_data.txt'
    kdd1='kdd_6.5_30_copy.txt'
    HDX(ps,bk,nt,pa,kdd,ps1,bk1,nt1,pa1,kdd1)

    


    
