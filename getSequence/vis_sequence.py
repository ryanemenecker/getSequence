import matplotlib.pyplot as plt
import metapredict as meta
import numpy as np
from goose import analyze
'''
code for visualization of sequences where seq is first pulled from uniprot
'''
def visualize_sequence(sequence, show_patterning=['Q']):
    if len(sequence) > 1520:
        raise Exception('Unable to show sequences with lengths greater than 1520.')

    AA_COLOR = {'Y':'#ff9d00',
                'W':'#ff9d00',
                'F':'#ff9d00',
                'A':'#171616',
                'L':'#171616',
                'M':'#171616',
                'I':'#171616',
                'V':'#171616',
                'Q':'#04700d',
                'N':'#04700d',
                'S':'#04700d',
                'T':'#04700d',
                'H':'#04700d',
                'G':'#04700d',
                'E':'#ff0d0d',
                'D':'#ff0d0d',
                'R':'#2900f5',
                'K':'#2900f5',
                'C':'#ffe70d',
                'P':'#cf30b7'}

    dims=(10, 8.8)
    fig = plt.figure(figsize=dims)
    custom_plot=plt.subplot(400,1,(1, 45))

    if len(show_patterning)>5:
        raise Exception('Can only show a maximum of 5 residues for patterning.')

    custom_plot_title = 'Patterning for residues '
    custom_plot_legend_title = 'Legend'
    for res in show_patterning:
        custom_plot_title+=f' {res}'

    y_axis=custom_plot.get_yaxis()
    y_axis.set_visible(False) 
    custom_plot.set_title(custom_plot_title)

    custom_plot_legend=plt.subplot(400, 1, (73, 84))
    custom_plot_legend.set_title(custom_plot_legend_title)
    custom_plot_legend.set_xlim(0, 10)
    custom_plot_legend.set_ylim(0, 1)    

    y_axis=custom_plot_legend.get_yaxis()
    y_axis.set_visible(False) 
    x_axis=custom_plot_legend.get_xaxis()
    x_axis.set_visible(False)

    custom_plot.set_xlim(0, len(sequence))
    curlinewidth = 555/len(sequence)

    custom_colors = ['#13b7f2','#ff620d', '#ffcb0d', '#ff0d0d', '#0b199c']
    
    sequence_colored = plt.subplot(400, 1, (180, 379))
    sequence_colored.axis('off')

    start_pos=0.1
    color_dict={}
    for cols in range(0, len(show_patterning)):
        curcol = custom_colors[cols]
        cur_aa = show_patterning[cols]
        color_dict[cur_aa]=curcol
        custom_plot_legend.text(start_pos, 0.15, f'{cur_aa} = ', fontsize=16, color='black')
        custom_plot_legend.axvline(start_pos+1, color=curcol, linewidth=40)
        start_pos+=2

    
    #startloc=0.02
    startloc=-0.04
    spacing_val=0.0128

    yloc=1
    for i in range(0, len(sequence)):
        cur_res = sequence[i]
        if cur_res in show_patterning:
            custom_plot.axvline(i+0.5, color=f'{color_dict[cur_res]}', linewidth=curlinewidth)
        else:
            custom_plot.axvline(i+0.5, color='black', linewidth=curlinewidth)


        cur_color=AA_COLOR[cur_res]
        sequence_colored.text(startloc, yloc, cur_res, horizontalalignment='center', verticalalignment='top', transform=sequence_colored.transAxes, 
                font='Courier', fontsize=14, color=cur_color)
        startloc += spacing_val
        startloc = round(startloc, 4)
        res_num=i+1

        if i !=0:
            if res_num%80==0:
                yloc-=0.05
                startloc=-0.05
            if res_num%10==0:
                startloc+=0.01

    disorder_plot=plt.subplot(400,1,(104, 149))
    disorder_plot.set_title('Sequence Disorder')
    xValues = np.arange(0, len(sequence))
    yValues=meta.predict_disorder(sequence)
    disorder_plot.set_xlim(-1, len(sequence)+1)
    disorder_plot.plot(xValues, yValues, color='blue', linewidth='1.6', label = 'Disorder Scores')
    for i in [0.2, 0.4, 0.6, 0.8]:
        disorder_plot.plot([0, len(sequence)], [i, i], color="black", linestyle="dashed", linewidth="0.5")
    disorder_plot.axhline(0.5, color='black')
    disorder_plot.set_ylabel('Disorder Score')
    disorder_plot.set_xlabel('Residue')
    axs=plt.subplot(400, 1, (380, 400))
    axs.set_title('Sequence Properties')
    axs.axis('off')
    props=analyze.everything(sequence)
    table_headers=['FCR', 'NCPR', 'hydropathy', 'kappa']
    table_data= [round(props['FCR'], 5), round(props['NCPR'], 5), round(props['hydropathy'], 5), round(props['kappa'], 5)]
    all_data=[table_headers, table_data]
    the_table=axs.table(all_data, cellLoc='center', loc='center')
    plt.show()

