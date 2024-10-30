import numpy as np
import os
import sys
from scipy.stats import sem
import matplotlib.pyplot as plt

def HDX(data_pf, data_in, data_in2, datafile):
    import os
    f=os.path.basename(datafile)+'.'+'txt'
    #f=os.path.basename(data_pf)+'.'+'dat'
    #f=open('datafile','w')
    data_pf=open(data_pf)
    data_pf = data_pf.read()
    data_pf=data_pf.split('\n')
    #data_pf=data_pf[1:]
    data_in=open(data_in)
    data_in = data_in.read()
    data_in=data_in.split('\n')
    data_in2=open(data_in2)
    data_in2 = data_in2.read()
    data_in2=data_in2.split('\n')
    d2=[]
    d1=[]
    d3=[]
    #out=open(filename, 'a')
    #outhdx=open(datafile, 'a')
    for i in data_in:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d2.append(x)
    for i in data_in2:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d3.append(x)   
    for i in data_pf:
        i=i[:-1]
        a=i.split()
        b=[]
        for j in a:
            b.append(float(j))
        d1.append(b)
    d1.pop()
    d2.pop()
    d3.pop()
    d1_pf=np.array(d1)
    d2_in=np.array(d2)
    d3_in=np.array(d3)
    y1=d1_pf[:,1]
    y2=d2_in[:,1]
    y3=d3_in[:,1]
    x1=d1_pf[:,0]
    y1=np.array(y1)
    y2=np.array(y2)
    merge=np.column_stack([y1, y2, y3])
    stdev=np.std(merge, axis=1)
    print(stdev)
    err=np.array(stdev/np.sqrt(3))
    merge=merge.mean(axis=1)
    #plot(x1, merge, err)
    #plot4(x1, merge, err)
    #print(merge)
    #plt.errorbar(x1, merge, yerr=err, xerr=None)
    #plt.show()
    #print(stdev)
    #print(merge)
    #print(err)
    #y1_in=d2_in
    #ratio=np.array(y1_in*1/y1_pf)
    #hdx_resid=np.array(1-(np.exp(-1*ratio)))
    #hdx=np.sum(hdx_resid)
    dat=np.column_stack([merge, err])
    #print(y1_pf, "\n" , y1_in)
    #hdx_all=np.column_stack([f2, hdx])
    np.savetxt(f, dat, fmt=['%5.4f','%5.4f'])
    #np.savetxt(out, hdx_all, fmt=['%10s','%5.4s'])
    #outhdx.write(str(hdx))
    #outhdx.write("\n")
    #outhdx.close()
    #out.close()
    #f.write(str(dat))
    #f.close()
    
   #return y1_pf, x1_pf
def plot(x, y, z):
    fig, (axs1, axs2) = plt.subplots(1, 2)
    axs1.errorbar(x, y, yerr=z, xerr=None)
    axs2.errorbar(x+0.5, y, yerr=z, xerr=None)
    plt.show()

def plot4(x, y, z):
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].errorbar(x, y, yerr=z)
    axs[0, 0].set_title('Axis [0, 0]')
    axs[0, 1].errorbar(x, y, yerr=z)
    axs[0, 1].set_title('Axis [0, 1]')
    axs[1, 0].errorbar(x, y, yerr=z)
    axs[1, 0].set_title('Axis [1, 0]')
    axs[1, 1].errorbar(x, y, yerr=z)
    axs[1, 1].set_title('Axis [1, 1]')
    plt.show()
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 5:
        print
        print("usage: python intrinsicrateseq.py [1] [2] [3] [4]")
        print("[1] simulation1 deltaG")
        print("[2] simulation2 deltaG")
        print("[3] simulation3 deltaG")
        print("[4] write datafile for individual for statistical calculation")
        sys.exit()
    else:
        data_in = sys.argv[1]
        data_pf = sys.argv[2]
        data_in2 = sys.argv[3]
        datafile=sys.argv[4]
        HDX(data_pf, data_in, data_in2, datafile)




