import numpy as np
import os
import sys
from scipy.stats import sem
import matplotlib.pyplot as plt
import matplotlib

def HDX(ps, bk, nt, pa, kdd, dt1, dt2, dt3, dt4,dt4_k, dt1_2, dt2_2, dt3_2, dt4_2, dt5_2, dt13, dt23, dt33, dt43,dt53, dt14, dt24, dt34, dt44,dt54):
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
    print(x1)

    dt1=open(dt1)
    dt1 = dt1.read()
    dt1=dt1.split('\n')
    dt2=open(dt2)
    dt2 = dt2.read()
    dt2=dt2.split('\n')
    dt3=open(dt3)
    dt3 = dt3.read()
    dt3=dt3.split('\n')
    dt4=open(dt4)
    dt4 = dt4.read()
    dt4=dt4.split('\n')
    dt4_k=open(dt4_k)
    dt4_k = dt4_k.read()
    dt4_k=dt4_k.split('\n')
    d1=[]
    d2=[]
    d3=[]
    d4=[]
    d4_k=[]
    res1=[]
    #out=open(filename, 'a')
    #outhdx=open(datafile, 'a')
    for i in dt1:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d1.append(x)
    for i in dt2:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d2.append(x)
    for i in dt3:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d3.append(x)
    for i in dt4:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d4.append(x)
    for i in dt4_k:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d4_k.append(x)
    d1.pop()
    d2.pop()
    d3.pop()
    d4.pop()
    d4_k.pop()
    d1_in=np.array(d1)
    d2_in=np.array(d2)
    d3_in=np.array(d3)
    d4_in=np.array(d4)
    d4_k_in=np.array(d4_k)
    m1=d1_in[:,0]
    m2=d2_in[:,0]
    m3=d3_in[:,0]
    m4=d4_in[:,0]
    m4_k=d4_k_in[:,0]
    err1=d1_in[:,1]
    err2=d2_in[:,1]
    err3=d3_in[:,1]
    err4=d4_in[:,1]
    err4_k=d4_k_in[:,1]
    m1=np.array(m1)
    m2=np.array(m2)
    m3=np.array(m3)
    m4=np.array(m4)
    m4_k=np.array(m4_k)
    err1=np.array(err1)
    err2=np.array(err2)
    err3=np.array(err3)
    err4=np.array(err4)
    err4_k=np.array(err4_k)
    print(m1)
    print(m2)


    dt1_2=open(dt1_2)
    dt1_2 = dt1_2.read()
    dt1_2=dt1_2.split('\n')
    dt2_2=open(dt2_2)
    dt2_2 = dt2_2.read()
    dt2_2=dt2_2.split('\n')
    dt3_2=open(dt3_2)
    dt3_2 = dt3_2.read()
    dt3_2=dt3_2.split('\n')
    dt4_2=open(dt4_2)
    dt4_2 = dt4_2.read()
    dt4_2=dt4_2.split('\n')
    dt5_2=open(dt5_2)
    dt5_2 = dt5_2.read()
    dt5_2=dt5_2.split('\n')
    d1_2=[]
    d2_2=[]
    d3_2=[]
    d4_2=[]
    d5_2=[]
    for i in dt1_2:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d1_2.append(x)
    for i in dt2_2:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d2_2.append(x)
    for i in dt3_2:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d3_2.append(x)
    for i in dt4_2:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d4_2.append(x)
    for i in dt5_2:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d5_2.append(x)

    d1_2.pop()
    d2_2.pop()
    d3_2.pop()
    d4_2.pop()
    d5_2.pop()
    d12_in=np.array(d1_2)
    d22_in=np.array(d2_2)
    d32_in=np.array(d3_2)
    d42_in=np.array(d4_2)
    d52_in=np.array(d5_2)
    m12=d12_in[:,0]
    m22=d22_in[:,0]
    m32=d32_in[:,0]
    m42=d42_in[:,0]
    m52=d52_in[:,0]
    err12=d12_in[:,1]
    err22=d22_in[:,1]
    err32=d32_in[:,1]
    err42=d42_in[:,1]
    err52=d52_in[:,1]
    m12=np.array(m12)
    m22=np.array(m22)
    m32=np.array(m32)
    m42=np.array(m42)
    m52=np.array(m52)
    err12=np.array(err12)
    err22=np.array(err22)
    err32=np.array(err32)
    err42=np.array(err42)
    err52=np.array(err52)
    print(np.size(m22), np.size(x2))

    dt13=open(dt13)
    dt13 = dt13.read()
    dt13=dt13.split('\n')
    dt23=open(dt23)
    dt23 = dt23.read()
    dt23=dt23.split('\n')
    dt33=open(dt33)
    dt33 = dt33.read()
    dt33=dt33.split('\n')
    dt43=open(dt43)
    dt43 = dt43.read()
    dt43=dt43.split('\n')
    dt53=open(dt53)
    dt53 = dt53.read()
    dt53=dt53.split('\n')
    d13=[]
    d23=[]
    d33=[]
    d43=[]
    d53=[]
    for i in dt13:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d13.append(x)
    for i in dt23:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d23.append(x)
    for i in dt33:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d33.append(x)
    for i in dt43:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d43.append(x)
    for i in dt53:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d53.append(x)
    d13.pop()
    d23.pop()
    d33.pop()
    d43.pop()
    d53.pop()
    d13_in=np.array(d13)
    d23_in=np.array(d23)
    d33_in=np.array(d33)
    d43_in=np.array(d43)
    d53_in=np.array(d53)
    m13=d13_in[:,0]
    m23=d23_in[:,0]
    m33=d33_in[:,0]
    m43=d43_in[:,0]
    m53=d53_in[:,0]
    err13=d13_in[:,1]
    err23=d23_in[:,1]
    err33=d33_in[:,1]
    err43=d43_in[:,1]
    err53=d53_in[:,1]
    m13=np.array(m13)
    m23=np.array(m23)
    m33=np.array(m33)
    m43=np.array(m43)
    m53=np.array(m53)
    err13=np.array(err13)
    err23=np.array(err23)
    err33=np.array(err33)
    err43=np.array(err43)
    err53=np.array(err53)

    dt14=open(dt14)
    dt14 = dt14.read()
    dt14=dt14.split('\n')
    dt24=open(dt24)
    dt24 = dt24.read()
    dt24=dt24.split('\n')
    dt34=open(dt34)
    dt34 = dt34.read()
    dt34=dt34.split('\n')
    dt44=open(dt44)
    dt44 = dt44.read()
    dt44=dt44.split('\n')
    dt54=open(dt54)
    dt54 = dt54.read()
    dt54=dt54.split('\n')
    d14=[]
    d24=[]
    d34=[]
    d44=[]
    d54=[]
    for i in dt14:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d14.append(x)
    for i in dt24:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d24.append(x)
    for i in dt34:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d34.append(x)
    for i in dt44:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d44.append(x)
    for i in dt54:
        i=i[:-1]
        a=i.split()
        x=[]
        for j in a:
            x.append(float(j))
        d54.append(x)
    d14.pop()
    d24.pop()
    d34.pop()
    d44.pop()
    d54.pop()
    d14_in=np.array(d14)
    d24_in=np.array(d24)
    d34_in=np.array(d34)
    d44_in=np.array(d44)
    d54_in=np.array(d54)
    m14=d14_in[:,0]
    m24=d24_in[:,0]
    m34=d34_in[:,0]
    m44=d44_in[:,0]
    m54=d54_in[:,0]
    err14=d14_in[:,1]
    err24=d24_in[:,1]
    err34=d34_in[:,1]
    err44=d44_in[:,1]
    err54=d54_in[:,1]
    m14=np.array(m14)
    m24=np.array(m24)
    m34=np.array(m34)
    m44=np.array(m44)
    m54=np.array(m54)
    err14=np.array(err14)
    err24=np.array(err24)
    err34=np.array(err34)
    err44=np.array(err44)
    err54=np.array(err54)
    plot4(x1, x2, x3, x4, x5, m1, m2, m3, m4, m4_k, err1, err2, err3, err4,err4_k, m12, m22, m32, m42,m52, err12, err22, err32, err42, err52,m13, m23, m33, m43, m53, err13, err23, err33, err43, err53, m14, m24, m34, m44,m54, err14, err24, err34, err44,err54)
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
    #print(y1_pf, "\n" , y1_in)
    #hdx_all=np.column_stack([f2, hdx])
    #np.savetxt(out, hdx_all, fmt=['%10s','%5.4s'])
    #outhdx.write(str(hdx))
    #outhdx.write("\n")
    #outhdx.close()
    #out.close()
    #f.write(str(dat))
    
   #return y1_pf, x1_pf
def plot(x, y, z):
    fig, (axs1, axs2) = plt.subplots(1, 2,figsize=(20, 20))
    axs1.errorbar(x, y, yerr=z, xerr=None)
    axs2.errorbar(x+0.5, y, yerr=z, xerr=None)
    plt.show()

def plot4(x1, x2, x3, x4,x5, m1, m2, m3, m4, m4_k, z1, z2, z3, z4, z4_k, m12, m22, m32, m42,m52, z12, z22, z32, z42,z52, m13, m23, m33, m43,m53, z13, z23, z33, z43,z53, m14, m24, m34, m44,m54, z14, z24, z34, z44,z54):
    import matplotlib
    fig, axs = plt.subplots(2, 2, sharex=False, sharey=False,figsize=(12, 9))
    #plt.rcParams["figure.autolayout"] = True
    #rc('text', usetex=True)
    axs[0, 0].errorbar(x1, m1, yerr=z1, ls='--', lw=2.5, color='black', marker='^')
    axs[0, 0].errorbar(x2, m2, yerr=z2, ls='--', lw=2.5, color='blue', marker='o')
    axs[0, 0].errorbar(x3, m3, yerr=z3, ls='--', lw=2.5, color='red', marker='s')
    axs[0, 0].errorbar(x4, m4, yerr=z4, ls='--', lw=2.5, color='brown', marker='*')
    axs[0, 0].errorbar(x5, m4_k, yerr=z4_k, ls='--', lw=2.5, color='green', marker='x')
    
    axs[0, 1].errorbar(x1, m12, yerr=z12, ls='--', lw=2.5, color='black', marker='^', label=r'$\bf{PS}$')
    axs[0, 1].errorbar(x2, m22, yerr=z22, ls='--', lw=2.5, color='blue',marker='o', label=r'$\bf{BK}$')
    axs[0, 1].errorbar(x3, m32, yerr=z32, ls='--', lw=2.5, color='red', marker='s', label=r'$\bf{Nt17}$')
    axs[0, 1].errorbar(x4, m42, yerr=z42, ls='--', lw=2.5, color='brown', marker='*', label=r'$\bf{PA}$')
    axs[0, 1].errorbar(x5, m52, yerr=z52, ls='--', lw=2.5, color='green', marker='x', label=r'$\bf{KDD}$')
    

    axs[0, 0].set_yticklabels(axs[0,1].get_yticks(), weight='bold',fontsize=16)
    axs[0,0].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
    axs[0, 0].set_xticklabels(axs[0,1].get_xticks(), weight='bold',fontsize=16)
    axs[0,0].xaxis.set_major_formatter(plt.FormatStrFormatter('%d'))
    

    axs[0, 1].set_yticklabels(axs[0,1].get_yticks(), weight='bold',fontsize=16)
    axs[0,1].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
    axs[0, 1].set_xticklabels(axs[0,1].get_xticks(), weight='bold',fontsize=16)
    axs[0,1].xaxis.set_major_formatter(plt.FormatStrFormatter('%d'))

    axs[1, 0].set_yticklabels(axs[0,1].get_yticks(), weight='bold',fontsize=16)
    axs[1,0].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
    axs[1, 0].set_xticklabels(axs[0,1].get_xticks(), weight='bold',fontsize=16)
    axs[1,0].xaxis.set_major_formatter(plt.FormatStrFormatter('%d'))

    axs[1, 1].set_yticklabels(axs[0,1].get_yticks(), weight='bold',fontsize=16)
    axs[1,1].yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
    axs[1, 1].set_xticklabels(axs[0,1].get_xticks(), weight='bold',fontsize=16)
    axs[1,1].xaxis.set_major_formatter(plt.FormatStrFormatter('%d'))

    axs[1, 0].errorbar(x1, m13, yerr=z13, ls='--', lw=2.5, color='black', marker='^')
    axs[1, 0].errorbar(x2, m23, yerr=z23, ls='--', lw=2.5, color='blue',marker='o')
    axs[1, 0].errorbar(x3, m33, yerr=z33, ls='--', lw=2.5, color='red', marker='s')
    axs[1, 0].errorbar(x4, m43, yerr=z43, ls='--', lw=2.5, color='brown', marker='*')
    axs[1, 0].errorbar(x5, m53, yerr=z53, ls='--', lw=2.5, color='green', marker='x')
    axs[0, 1].legend(loc='upper right', frameon=False, bbox_to_anchor=(0.8, 1.2), ncol=5,fontsize=16)

    axs[1, 1].errorbar(x1, m14, yerr=z14, ls='--', lw=2.5, color='black', marker='^')
    axs[1, 1].errorbar(x2, m24, yerr=z24, ls='--', lw=2.5, color='blue',marker='o')
    axs[1, 1].errorbar(x3, m34, yerr=z34, ls='--', lw=2.5, color='red', marker='s')
    axs[1, 1].errorbar(x4, m44, yerr=z44, ls='--', lw=2.5, color='brown', marker='*')
    axs[1, 1].errorbar(x5, m54, yerr=z54, ls='--', lw=2.5, color='green', marker='x')
    
    axs[0, 0].set_ylabel('ln(PF)', fontsize=16, fontweight='bold')
    axs[0, 1].set_ylabel('HDx', fontsize=16, fontweight='bold')
    axs[1, 0].set_xlabel('Resid', fontsize=16, fontweight='bold')
    axs[1, 0].set_ylabel('ln(PF)', fontsize=16, fontweight='bold')
    axs[1, 1].set_xlabel('Resid', fontsize=16, fontweight='bold')
    axs[1, 1].set_ylabel('HDx', fontsize=16, fontweight='bold')
    axs[0, 0].set_title('A', fontsize=16, fontweight='bold', loc='left')
    axs[0, 1].set_title('B', fontsize=16, fontweight='bold', loc='left')
    axs[1, 0].set_title('C', fontsize=16, fontweight='bold', loc='left')
    axs[1, 1].set_title('D', fontsize=16, fontweight='bold', loc='left')
    for axis in ['top','bottom','left','right']:
        axs[1,1].spines[axis].set_linewidth(2.0)
    axs[1,1].tick_params(width=2.0)


    for axis in ['top','bottom','left','right']:
        axs[0,0].spines[axis].set_linewidth(2.0)
    axs[0,0].tick_params(width=2.0)


    for axis in ['top','bottom','left','right']:
        axs[0,1].spines[axis].set_linewidth(2.0)
    axs[0,1].tick_params(width=2.0)


    for axis in ['top','bottom','left','right']:
        axs[1,0].spines[axis].set_linewidth(2.0)
    axs[1,0].tick_params(width=2.0)
    #plt.tight_layout()

    resolution = 720
    plt.savefig("pf_kint_hdx_m3_m4.png", format="png", dpi=resolution)
    #axs[0, 1].errorbar(x2, y, yerr=z)
    #axs[0, 1].set_title('Axis [0, 1]')
    #axs[1, 0].errorbar(x, y, yerr=z)
    #axs[1, 0].set_title('Axis [1, 0]')
    #axs[1, 1].errorbar(x, y, yerr=z)
    #axs[1, 1].set_title('Axis [1, 1]')
    plt.show()
if __name__ == '__main__':
    ps='pS_s2_1-500_bb_shpdG_8.3.dat'
    #bk='bk_s1_1-500_bb_shpdG_8.3.dat'
    bk='x2.txt'
    nt='nt17_s1_1-500_bb_shpdG_8.3.dat'
    pa='polyA_s3_1-500_bb_shpdG_8.3.dat'
    kdd='kdd_r.dat'


    dt1 = 'pS_avg_error_shwdg_8.3.dat.txt'
    dt2 = 'bk_avg_error_shwdg_8.3.dat.txt'
    dt3= 'nt17_avg_error_shwdg_8.3.dat.txt'
    dt4='pA_avg_error_shwdg_8.3.dat.txt'
    dt4_k='dkdd_avg_error_shwdG_8.3.dat.txt'
    
    dt1_2='pS_avg_error_shwpf_6.5_8.3.dat.txt'
    dt2_2='bk_avg_error_kint_shwpf_6.5_8.3.dat.txt'
    dt3_2='nt17_avg_error_shwpf_6.5_8.3.dat.txt'
    dt4_2='pA_avg_error_shwpf_6.5_8.3.dat.txt'
    dt5_2='dkdd_avg_error_shwpf_8.3.6.50_30.dat.txt'
    
    dt13 = 'pS_avg_error_shpdg_8.3.dat.txt'
    dt23 = 'bk_avg_error_shpdg_8.3.dat.txt'
    dt33= 'nt17_avg_error_shpdg_8.3.dat.txt'
    dt43='pA_avg_error_shpdg_8.3.dat.txt'
    dt53='dkdd_avg_error_shpdg_8.3.dat.txt'
    
    dt14 = 'pS_avg_error_shpf_6.5_8.3.dat.txt'
    dt24 = 'bk_avg_error_kint_shppf_6.5_8.3.dat.txt'
    dt34= 'nt17_avg_error_shpf_6.5_8.3.dat.txt'
    dt44='pA_avg_error_shpf_6.5_8.3.dat.txt'
    dt54='dkdd_avg_error_shppf_8.3.6.50_30.dat.txt'
    HDX(ps,bk,nt,pa,kdd, dt1, dt2, dt3, dt4,dt4_k, dt1_2, dt2_2, dt3_2, dt4_2, dt5_2, dt13, dt23, dt33, dt43,dt53, dt14, dt24, dt34, dt44,dt54)
        #plot(HDX(data_pf, dt1, da2))




