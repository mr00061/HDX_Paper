import numpy as np
import os
import sys

def HDX(data_pf, data_in, filename, datafile):
    f=os.path.basename(data_pf)+'-'+os.path.basename(data_in)+'.'+'txt'
    f2=os.path.basename(data_pf)+'-'+os.path.basename(data_in)
    data_pf=open(data_pf)
    data_pf = data_pf.read()
    data_pf=data_pf.split('\n')
    data_pf=data_pf[1:]
    data_in=open(data_in)
    data_in = data_in.read()
    data_in=data_in.split()
    d2=[]
    d1=[]
    out=open(filename, 'a')
    outhdx=open(datafile, 'a')
    for i in data_in:
        d2.append(float(i))
    
    for i in data_pf:
        i=i[:-1]
        a=i.split()
        b=[]
        for j in a:
            b.append(float(j))
        d1.append(b)
    d1.pop()
    d1_pf=np.array(d1)
    y1_pf=d1_pf[:,1]
    x1_pf=d1_pf[:,0]
    d2_in=np.array(d2)
    y1_in=d2_in
    ratio=np.array(y1_in/y1_pf)
    print(ratio)
    hdx_resid=np.array(1-(np.exp(-1*ratio)))
    hdx=np.sum(hdx_resid)
    dat=np.column_stack([x1_pf, hdx_resid])
    #print(y1_pf, "\n" , y1_in)
    hdx_all=np.column_stack([f2, hdx])
    np.savetxt(f, dat, fmt=['%d','%5.4f'])
    np.savetxt(out, hdx_all, fmt=['%10s','%5.4s'])
    outhdx.write(str(hdx))
    outhdx.write("\n")
    outhdx.close()
    out.close()
    
    return y1_pf, x1_pf
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 5:
        print
        print("usage: python intrinsicrateseq.py [1] [2] [3] [4]")
        print("[1] Datafile from intrinsic rate")
        print("[2] Data filename from MD analysis")
        print("[3] Write filename for HDx contribution per residue")
        print("[3] write datafile for individual for statistical calculation")
        sys.exit()
    else:
        data_in = sys.argv[1]
        data_pf = sys.argv[2]
        filename = sys.argv[3]
        datafile=sys.argv[4]
        print(data_pf)
        
        HDX(data_pf, data_in, filename, datafile)




