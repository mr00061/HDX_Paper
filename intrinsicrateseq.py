import os, sys, posix, re
from collections import defaultdict
import numpy as np
import glob
import math
cur_dir = os.getcwd()
prefix = cur_dir.split("/")[-3]
constR = 1.987/1000




#Make dictionary of sequence
AA_3to1 = {'GLY':'G', 'ALA':'A', 'VAL':'V', 'LEU':'L', 'ILE':'I',
           'MET':'M', 'PHE':'F', 'TRP':'W', 'PRO':'P', 'SER':'S',
           'THR':'T', 'CYS':'C', 'TYR':'Y', 'ASN':'N', 'GLN':'Q',
           'ASP':'D', 'GLU':'E', 'LYS':'K', 'ARG':'R', 'HIS':'H',
           'NTR':'X', 'CTR':'Z'}
AA_1to3 = {'G':'GLY', 'A':'ALA', 'V':'VAL', 'L':'LEU', 'I':'ILE',
           'M':'MET', 'F':'PHE', 'W':'TRP', 'P':'PRO', 'S':'SER',
           'T':'THR', 'C':'CYS', 'Y':'TYR', 'N':'ASN', 'Q':'GLN',
           'D':'ASP', 'E':'GLU', 'K':'LYS', 'R':'ARG', 'H':'HIS',
           'X':'NTR', 'Z':'CTR'}
def sequence_kint(pD_corr, myTempC, seq, timeUnit, filename, filenamecopy):
    myTemp = float(myTempC) + 273.0
    outfile=open(filename, 'w')
    outfilec=open(filenamecopy, 'w')
    pD_corr = float(pD_corr)
    seq = seq.replace("\n", '')
    if re.search('sec', timeUnit):
        timeUnitFactor = 1/60
    else:
        timeUnitFactor = 1.0
    
    Calc_condition = """
    /////////////////////////////////////////////////////////
    Temperature = %s K
    pD_corr = %s
    Time Unit = %s
    Sequence = %s
    /////////////////////////////////////////////////////////
    """ % (myTemp, pD_corr, timeUnit, seq)
    print(Calc_condition)
    log_AB_LR_dic = {
    #residue: [AL, AR, BL, BR ],
    'ALA': [0.00, 0.00, 0.00, 0.00],
    'ARG': [-0.59, -0.32, 0.08, 0.22],
    'ASN': [-0.58, -0.13, 0.49, 0.32],
    'ASPd': [0.9, 0.58, -0.30, -0.18], #D(COO-)
    'ASPp': [-0.9, -0.12, 0.69, 0.6], #D(COOH)
    'CYS' :[-0.54, -0.46, 0.62, 0.55],
    'GLY': [-0.22, 0.22, 0.27, 0.17],
    'GLN': [-0.47, -0.27, 0.06, 0.20],
    'GLUd': [-0.9, 0.31, -0.51, -0.15], #E(COO-)
    'GLUp': [-0.6, -0.27, 0.24, 0.39], #E(COOH)
    'HISd': ['NA', 'NA', -1.0, 0.14],
    'HISp': [-0.8, -0.51, 0.8, 0.83],
    'ILE': [-0.91, -0.59, -0.73, -0.23],
    'ILE': [-0.91, -0.59, -0.73, -0.23],
    'LEU': [-0.57, -0.13, -0.58, -0.21],
    'LYS': [-0.56, -0.29, -0.04, 0.12],
    'MET': [-0.64, -0.28, -0.01, 0.11],
    'PHE': [-0.52, -0.43, -0.24, 0.06],
    'PRO': ['NA', -0.19, 'NA', -0.24], #P-trans
    #’PROc’: [’NA’, -0.85, ’NA’, 0.60], #P-cis
    'SER': [-0.44, -0.39, 0.37, 0.30],
    'THR': [-0.79, -0.47, -0.07, 0.20],
    'TRP': [-0.40, -0.44, -0.41, -0.11],
    'TYR': [-0.41, -0.37, -0.27, 0.05],
    'VAL': [-0.74, -0.30, -0.70, -0.14],
    'NTR': ['NA', -1.32, 'NA', 1.62],
    'CTRd': [0.96, 'NA', -1.8, 'NA'],
    'CTRp': [0.05, 'NA', 'NA', 'NA']
    }

    #titrable_res_dic = {'ASP':4.50, 'GLU':4.50, 'HIS':6.75, 'CTR':3.720}
    titrable_res_dic = {'GLU':4.50}

    Ea_A = 15.0; Ea_B = 2.6; Ea_W = 13.0
    logkA_ref = math.log10((timeUnitFactor)*10**2.04) #1/(M*min)
    logkB_ref = math.log10((timeUnitFactor)*10**10.36) #1/(M*min)
    logkW_ref = math.log10((timeUnitFactor)*10**-1.5)
    
    pkD = 15.05
    pOD_corr = pkD-pD_corr
    seq_NH = 'x'.join(seq)
    for k, v in enumerate(seq_NH):
        logk_acid = 0; logk_base =0; logk_wat = 0; logk_int = 0
        if v == 'x':
            res_R = AA_1to3[seq_NH[k - 1]]
            res_L = AA_1to3[seq_NH[k + 1]]
            special_res = titrable_res_dic.keys()
            for s_res in special_res:
                if res_R == s_res:
                    if pD_corr <= titrable_res_dic[s_res]:
                        res_R = res_R + 'p'
                    else:
                        res_R = res_R + 'd'
                if res_L == s_res:
                    if pD_corr <= titrable_res_dic[s_res]:
                        res_L = res_L + 'p'
                    else:
                        res_L = res_L + 'd'
                if log_AB_LR_dic[res_L][0] == 'NA':
                    logA_L = 0.0
                else:
                    logA_L = log_AB_LR_dic[res_L][0]
                if log_AB_LR_dic[res_R][1] == 'NA':
                    logA_R = 0.0
                else:
                    logA_R = log_AB_LR_dic[res_R][1]
                if log_AB_LR_dic[res_L][2] == 'NA':
                    logB_L = 0.0
                else:
                    logB_L = log_AB_LR_dic[res_L][2]
                if log_AB_LR_dic[res_R][3] == 'NA':
                    logB_R = 0.0
                else:
                    logB_R = log_AB_LR_dic[res_R][3]
            TempFactor = (1.0/myTemp - 1.0/293.0)/constR
            logk_acid = (logkA_ref + logA_L + logA_R - pD_corr)
            logk_base = (logkB_ref + logB_L + logB_R - pOD_corr)
            logk_wat = (logkW_ref + logB_L + logB_R)
            k_acid = (10**(logk_acid)) * (math.exp(-Ea_A*TempFactor))
            k_base = (10**(logk_base)) * (math.exp(-Ea_B*TempFactor))
            k_wat = (10**(logk_wat)) * (math.exp(-Ea_W*TempFactor))
            k_int = (k_acid + k_base + k_wat)
            if res_L == 'PRO' or res_L == 'PRO':
                print(AA_3to1[res_R[:3]]+'-NH-'+ AA_3to1[res_L[:3]])
                outfile.write(AA_3to1[res_R[:3]]+'-NH-'+ AA_3to1[res_L[:3]])
                #x=0
                #outfilec.write('{:5.4f}'.format(x) +"\n")
            else:
                print(AA_3to1[res_R[:3]]+'-NH-'+ AA_3to1[res_L[:3]], '{:5.4f}'.format(k_int), "1/"+str(timeUnit))
                outfile.write(AA_3to1[res_R[:3]]+'-NH-'+ AA_3to1[res_L[:3]]+"\t" + '{:5.4f}'.format(k_int) +"\t"+"1/"+str(timeUnit)+"\n")
                outfilec.write('{:5.4f}'.format(k_int) +"\n")
    outfile.close()
    outfilec.close()
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 7:
        print
        print("usage: python intrinsicrateseq.py [1] [2] [3] [4]")
        print("[1] pD_corr")
        print("[2] Temperature in Celcius")
        print ("[3] sequence with 1-letter AA")
        print ("[4] time unit (min or sec)")
        print
        sys.exit()
    else:
        pD_corr = sys.argv[1]
        myTempC = sys.argv[2]
        seq = sys.argv[3]
        timeUnit = sys.argv[4]
        filename=sys.argv[5]
        filenamecopy=sys.argv[6]
        sequence_kint(pD_corr, myTempC, seq, timeUnit, filename, filenamecopy)
