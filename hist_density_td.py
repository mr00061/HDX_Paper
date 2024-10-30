import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl


def process_data(dt1, dt2, dt3, fig1, fig2, fig3, title):
    dt1=open(dt1)
    dt1 = dt1.read()
    dt1=dt1.split('\n')
    d1=[]
    for i in dt1:
        i=i[:-1]
        a=i.split()
        x11=[]
        for j in a:
            x11.append(float(j))
        d1.append(x11)
    
    d1.pop()
    d1_in=np.array(d1)
    x1=d1_in[:,0]
    y1=d1_in[:,1]
    x1=np.array(x1)
    y1=np.array(y1)

    dt2=open(dt2)
    dt2 = dt2.read()
    dt2=dt2.split('\n')
    d2=[]
    for i in dt2:
        i=i[:-1]
        a12=i.split()
        x12=[]
        for j12 in a12:
            x12.append(float(j12))
        d2.append(x12)
    
    d2.pop()
    d2_in=np.array(d2)
    x2=d2_in[:,0]
    y2=d2_in[:,1]
    x2=np.array(x2)
    y2=np.array(y2)

    dt3=open(dt3)
    dt3 = dt3.read()
    dt3=dt3.split('\n')
    d3=[]
    for i in dt3:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d3.append(x)
    
    d3.pop()
    d3_in=np.array(d3)
    x3=d3_in[:,0]
    y3=d3_in[:,1]
    x3=np.array(x3)
    y3=np.array(y3)

    f1=fig1
    f2=fig2
    f3=fig3
    t=title
    plot_density(y1, y2, y3,f1,t)
    plot_hista(y1, y2, y3, f2,t)
    plot_td(x1,y1, x2,y2, x3,y3,f3,t)


def plot_density(y1,y2,y3,f1,t):
    fig, ax=plt.subplots(figsize=(7,6))
    #ax.hist(y, label='AB', density=True)
    #bin_height,bin_boundary = np.histogram(y,bins=300)
    df1=pd.DataFrame(y1, columns=list('A'))
    X1=df1['A']
    df2=pd.DataFrame(y2, columns=list('B'))
    X2=df2['B']
    df3=pd.DataFrame(y3, columns=list('C'))
    X3=df3['C']
    sns.kdeplot(X1, label='s1', linewidth=3.0, color='black', cut=0)
    sns.kdeplot(X2, label='s2', linewidth=3.0, color='blue',cut=0)
    sns.kdeplot(X3, label='s3', linewidth=3.0, color='brown',cut=0)
    plt.xlabel('Radius of Gyration /(Angstrom)', weight='bold', fontsize=14)
    plt.ylabel('Density', weight='bold', fontsize=14)
    plt.xticks(weight='bold', fontsize=14)
    plt.yticks(weight='bold', fontsize=14)
    #rc('box', linewidth=2)
    plt.tick_params(width=2)
    #plt.axhline(linewidth=2)
    #mpl.rcParams['axes.linewidth'] =1
    [x.set_linewidth(2.0) for x in ax.spines.values()]
    f1=f1
    plt.legend(fontsize=14, loc='upper right', frameon=False)
    plt.title(t, weight='bold', fontsize=14, loc='left')
    resolution=1200
    plt.savefig(f1, format="png", dpi=resolution)
    plt.show()


def plot_hista(y1, y2, y3,f2,t):
    fig, ax=plt.subplots(figsize=(7,6))


    bin_height1,bin_boundary1 = np.histogram(y1,bins=300)
    width1=bin_boundary1[1]-bin_boundary1[0]
    bin_height1=bin_height1/float(max(bin_height1))
    center1=(bin_boundary1[:-1]+bin_boundary1[1:])/2

    bin_height2,bin_boundary2 = np.histogram(y2,bins=300)
    width2=bin_boundary2[1]-bin_boundary2[0]
    bin_height2=bin_height2/float(max(bin_height2))
    center2=(bin_boundary2[:-1]+bin_boundary2[1:])/2  

    bin_height3,bin_boundary3 = np.histogram(y3,bins=300)
    width3=bin_boundary3[1]-bin_boundary3[0]
    bin_height3=bin_height3/float(max(bin_height3))
    center3=(bin_boundary3[:-1]+bin_boundary3[1:])/2

    plt.bar(center1, bin_height1,width=width1, linewidth=4, zorder=2, color='black', label="s1")
    plt.bar(center2, bin_height2,width=width2, linewidth=4, zorder=2, color='blue', label="s2")
    plt.bar(center3, bin_height3,width=width3, linewidth=4, zorder=2, color='brown', label="s3")
    plt.xlabel('Radius of Gyration /(Angstrom)', weight='bold', fontsize=14)
    plt.ylabel('Frequency', weight='bold', fontsize=14)
    plt.xticks(weight='bold', fontsize=14)
    plt.yticks(weight='bold', fontsize=14)
    plt.title(t, weight='bold', fontsize=14, loc='left')
    #rc('box', linewidth=2)
    plt.tick_params(width=2)
    #plt.axhline(linewidth=2)
    #mpl.rcParams['axes.linewidth'] =1
    [x.set_linewidth(2.0) for x in ax.spines.values()]
    f2=f2
    plt.legend(fontsize=14, loc='upper right', frameon=False)
    resolution=1200
    plt.savefig(f2, format="png", dpi=resolution)
    plt.show()
    
def plot_td(x1,y1,x2,y2,x3,y3,f3,t):
    fig, ax = plt.subplots(figsize=(7,6))
    plt.plot(x1,y1, label='s1', linewidth=2.5, color='black')
    plt.plot(x2,y2, label='s2', linewidth=2.5, color='blue')
    plt.plot(x3,y3, label='s3', linewidth=2.5, color='brown')
    plt.ylabel('Radius of Gyration /(Angstorm)', weight='bold', fontsize=14)
    plt.xlabel('Time /(ns)', weight='bold', fontsize=14)
    plt.xticks(weight='bold', fontsize=14)
    plt.yticks(weight='bold', fontsize=14)
    plt.tick_params(width=2)
    plt.title(t, weight='bold', fontsize=14, loc='left')
    [x.set_linewidth(2) for x in ax.spines.values()]
    f3=f3
    plt.legend(fontsize=14, loc='upper right', frameon=False)
    resolution=1200
    plt.savefig(f3, format="png", dpi=resolution)
    plt.show()


if __name__ == '__main__':
    
    import sys
    if len(sys.argv) != 8:
        print
        print("usage: python hist_skeens.py data_AB data_CD data_AC data_BD imagefile_density.png imagefile_hist_png")
        print("[1] simulation1 data1")
        print("[2] simulation2 data2")
        print("[3] simulation3 data3")
        print("[4] savefigure_density")
        print("[5] savefigure_hist")
        print("[6] savefigure_td")
        print("[7] set title")
        sys.exit()
    else:
        dt1 = sys.argv[1]
        dt2 = sys.argv[2]
        dt3 = sys.argv[3]
        fig1 = sys.argv[4]
        fig2=sys.argv[5]
        fig3=sys.argv[6]
        title=sys.argv[7]
        process_data(dt1, dt2, dt3, fig1, fig2, fig3, title)
    #dt1='tet_r2_5A_AB.dat'
    #dt2='tet_r2_5A_CD.dat'
    #dt3='tet_r2_5A_AC.dat'
    #dt4='tet_r2_5A_BD.dat'
    #process_data(dt1, dt2, dt3, dt4, fig1, fig2)