import os
import seaborn as sn
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.patches import Rectangle

nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
heat_dict = {'T': 1, 'H': 2, 'E': 3, 'C': 4, 'G': 5, 'B': 6, 'I':7}


def seperate_x(file,resid):

    x = []
    cnt = 0
    rows = []
    resid=int(resid)

    for line in file:

        if line[0] not in nums:
            cnt = 0
            rows = []
            continue

        item = list(map(str, line.split()))
        item[0] = int(item[0])
        item[-1] = heat_dict[item[-1]]
        rows.append(item)
        cnt += 1
        if cnt == resid:
            x.append(rows)
            cnt = 0
            rows = []
    #print(x[0])
    return x


def plot_util(type_, y, title, f1,f2, resid):
    resid=int(resid)

    if type_ == 'scatter':
        
        new_x = []
        new_y = []
        name = []

        cnt = 1
        for j in y:
            a = set(j)
            new_x += [cnt]*len(a)
            a = list(a)
            for i in a:
                if i == 1:
                    name.append('T')
                elif i == 2:
                    name.append('H')
                elif i == 3:
                    name.append('E')
                elif i == 4:
                    name.append('C')
                elif i == 5:
                    name.append('G')
                elif i == 6:
                    name.append('B')
                elif i == 7:
                    name.append('I')
            new_y += a

            cnt += 1

        df = pd.DataFrame({'X': new_x,
                   'Y': new_y,
                   'z': name})
        
        groups = df.groupby('z')
        fig, ax1=plt.subplots(figsize=(7,6))
        for name, group in groups:
            plt.plot(group.X, group.Y, marker='o', linestyle='', markersize=3, label=name)
        plt.xlabel('Frames', weight='bold', fontsize=16)
        plt.ylabel('Helical Content', weight='bold', fontsize=16)
        plt.xticks(weight='bold', fontsize=13)
        plt.yticks(weight='bold',  fontsize=13)
        plt.tick_params(width=2)
        lp = {'weight':'bold'}
        plt.legend(fontsize=14, prop=lp, loc='upper right', frameon=False)
        plt.title(t, weight='bold', fontsize=14, loc='left')
        resolution=1200
        f1=f1
        [x.set_linewidth(2.0) for x in ax1.spines.values()]
        plt.savefig(f1, format="png", dpi=resolution)
        
        plt.show()

    elif type_ == 'heatmap':
        colors = ['green', "blue",'white','#d3d3d3', "red"]
        cmap = LinearSegmentedColormap.from_list("blue_white_red", colors)
        mat = []
        for item in y:
            y_cnt = []
            for i in range(1, 8):
                y_cnt.append(item.count(i))
            mat.append(y_cnt)
        #print(mat)
        #print(np.array(y))

        mat = np.array(mat).reshape((len(mat[0]), len(mat)))
        fig=plt.figure(figsize=(6,5), dpi=300)
        ax1=fig.add_subplot(111)
        #xticks=np.arange(0, 500, 100)
        #xtick_labels = [f'{int(label)}' for label in xticks]
        
        ax=sn.heatmap(np.array(y).T, cmap=cmap, yticklabels=[i for i in range(1,resid+1)], vmin=1,vmax=7,cbar_kws={"orientation": "vertical", "pad": 0.01})
        sn.color_palette('bright')
        colorbar=ax.collections[0].colorbar
        #cbar.ax.tick_params(labelsize=16)
        #bar.tick_params(labelsize=18, rotation=90, labelpad=30, weight='bold', fontsize=18)
        for t in colorbar.ax.get_yticklabels():
        	t.set_fontsize(20)
        	t.set_fontweight('bold')

        number_ticks = [1, 2, 3, 4, 5, 6, 7]
        letter_labels = ['T', 'H', 'E', 'C', 'G', 'B', 'I']
        colorbar.set_ticks(number_ticks)
        colorbar.set_ticklabels(letter_labels)
        colorbar.ax.tick_params(width=2)
        ax.set_xlabel('Time (ns)', weight='bold', fontsize=20)
        ax.set_ylabel('Residue Number', weight='bold', fontsize=20)
        xticks=np.arange(0, 501, 100)
        #xtick_labels = [f'{int(label)}' for label in xticks]
        #plt.xticks(xticks)
        #plt.xticks(weight='bold', fontsize=20, rotation=0)
        ax.set_xticks(xticks)
        ax.set_xticklabels([str(i) for i in xticks], weight='bold', fontsize=18, rotation=0)
        plt.yticks(weight='bold',  fontsize=18, rotation=0)
        plt.tick_params(width=2)
        for _, spine in ax.spines.items():
            spine.set_edgecolor('black')
            spine.set_linewidth(2)

        """pos = ax.get_position()
        rect = Rectangle((pos.x0, pos.y0), pos.width, pos.height, linewidth=2, edgecolor='black', facecolor='none', transform=plt.gcf().transFigure)
        # Add the Rectangle patch to the current figure
        ax.set_xlim(0, y.shape[1])
        ax.set_ylim(0, y.shape[0])
        """
        lp = {'weight':'bold'}
        
        #plt.legend(fontsize=14, prop=lp, loc='upper right', frameon=False)
        plt.title(title, weight='bold', fontsize=20, loc='left')
        plt.locator_params(axis='both', nbins=9)
        plt.tight_layout()
        #resolution=1200
        plt.savefig(f2, format="png", dpi=300)
        #plt.show()


if __name__ == "__main__":

    import sys
    if len(sys.argv) != 6:
        print
        print("usage: python hist_skeens.py data_AB data_CD data_AC data_BD imagefile_density.png imagefile_hist_png")
        print("[1] data1")
        print("[2] title")
        print("[3] imageoutfile name scatter")
        print("[4] imageoutfile name heatmap")
        print("[5] residue number")
        sys.exit()
    else:
        fl = sys.argv[1]
        title = sys.argv[2]
        fig1 = sys.argv[3]
        fig2=sys.argv[4]
        resid=sys.argv[5]


        file = open(fl, 'r').readlines()
        x = seperate_x(file,resid)
        y = []
        for i in x:
            y_val = []
            for j in i:
                y_val.append(j[-1])
            y.append(y_val)
    #print(y)


        plot_util('heatmap',y,title,fig1,fig2,resid)
        #plot_util('scatter', y,t, fig1,fig2,resid)
