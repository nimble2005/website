'''
The program is to sum up the pv-EOS from different structures of Vanadium.
12.08.2021
NBY
'''
from matplotlib import pyplot as plt
import numpy as np
import sys
sys.path.append("/home/nby/study/NBY-Lib/")
sys.path.append("/home/nby/study/vanadium-new/")
from nbyplot import myplot, myfig_setup, myscatter, nbymarker, nbycolor
import units
from exp_data_pv_reduce import exp_bcc, exp_bcc2, exp_bcc3
from exp_data_pv_reduce import exp_bcc4_1, exp_bcc4_2, exp_bcc5
from exp_data_pv_reduce import exp_rh, exp_rh2, exp_rh3, exp_rh5


def main():
    # ----------- Theoretical Data from either DIA or EEA ----------
    fileloc = "/home/nby/study/vanadium-new/SUST/pv-data/"
    bcc_rh0 = np.loadtxt(fileloc + "rh0-sv-300K-reduced.dat")
    bcc_meam = np.loadtxt(fileloc + "bcc-meam-300K-reduced.dat")
    bcc_md = np.loadtxt(fileloc + "bcc-md-300K.dat")
    vol0_meam = np.float64(14.029214094494863)
    bcc_md[:, 1] /= vol0_meam
    # ------------- calculate the difference between DIA and MD-----
    meam_v = bcc_meam[:, 0]
    meam_p = bcc_meam[:, 1]
    stat = np.array([np.float64(0.) for i in range(len(bcc_md[:, 1]))])
    ncount = 0
    for i, j in zip(bcc_md[:, 0], bcc_md[:, 1]):
        md_v = j
        md_p = i
        dia_v = meam_v[np.abs(meam_v-md_v) < np.float64(1e-4)][0]
        dia_p = meam_p[np.abs(meam_v-md_v) < np.float64(1e-4)][0]
        stat[ncount] = ((dia_p - md_p) / md_p) * 100
        # print(md_v, dia_v, md_p, ((dia_p - md_p) / md_p) * 100)
        ncount += 1
    # print(np.average(stat))
    # print(np.std(stat))
    # ------------ Plot Procedure ----------------------------------
    plimit = 320
    nsel3 = np.where(bcc_rh0[:, 1] < plimit)[0][0]
    nsel5 = np.where(bcc_meam[:, 1] < plimit)[0][0]
    fig, ax = plt.subplots(figsize=(8, 6))
    myplot(ax, bcc_rh0[nsel3:, 1], bcc_rh0[nsel3:, 0],
           {"color": nbycolor[0], "linestyle": "--",
            "label": "DIA"})
    # -------------------- inset plot --------------------------------
    plimit_sub = np.float64(60.)  # pressure upper limit
    ax_sub = fig.add_axes([0.53, 0.5, 0.35, 0.35])
    nsel_sub = np.where(bcc_rh0[:, 1] < plimit_sub)[0][0]
    myplot(ax_sub, bcc_rh0[nsel_sub:, 1], bcc_rh0[nsel_sub:, 0],
           {"color": nbycolor[0], "linestyle": "--"})
    myscatter(ax_sub, exp_bcc[0, :], exp_bcc[1, :],
              {"color": "blue",
               "marker": nbymarker[0], "s": 50})
    myscatter(ax_sub, exp_bcc3[0, :], exp_bcc3[1, :],
              {"color": "slateblue",
               "marker":  nbymarker[3], "s": 50})
    myscatter(ax_sub, exp_bcc2[0, :], exp_bcc2[1, :],
              {"color": "steelblue",
               "marker":  nbymarker[1], "s": 50})
    myscatter(ax_sub, exp_bcc5[0, :], exp_bcc5[1, :],
              {"color": "slategrey",
               "marker": "d", "s": 50})
    myscatter(ax_sub, exp_bcc4_1[0, :], exp_bcc4_1[1, :],
              {"color": "springgreen",
               "marker": "^", "s": 50})
    myscatter(ax_sub, exp_bcc4_2[0, :], exp_bcc4_2[1, :],
              {"color": "springgreen",
               "marker": "^", "s": 50})
    ax_sub.set_xticks(np.array([0, 20, 40, 60]))
    ax_sub.set_xlim(-0.01, plimit_sub+0.1)
    ax_sub.set_ylim(0.79, 1.0)
    Fontname = "Times New Roman"
    Fontweight = "bold"
    Fontsize = 15
    ax_sub.set_xlabel(r"Pressure (GPa)", fontsize=Fontsize,
                      fontname=Fontname, fontweight=Fontweight)
    ax_sub.set_ylabel(r"Volume ($V/V_0$)", fontsize=Fontsize,
                      fontname=Fontname, fontweight=Fontweight)
    # ax_sub.legend(loc=(0.42, 0.62), fontsize=11)
    ax_sub.grid(which="both", linestyle=":")
    ax_sub.tick_params(labelsize=12)
    # ---------------- calculate difference of the inset ----------
    # nsum = np.float64(0)
    nsum = []
    ncount = 0
    plimit_sub2 = np.float64(20.)
    for i, j in zip(exp_bcc[0, :], exp_bcc[1, :]):
        if i > plimit_sub2:
            continue
        ncount += 1
        nsum.append(np.abs(bcc_rh0[bcc_rh0[:, 1] < i][0][0] - j) / j)
    for i, j in zip(exp_bcc3[0, :], exp_bcc3[1, :]):
        if i > plimit_sub2:
            continue
        ncount += 1
        nsum.append(np.abs(bcc_rh0[bcc_rh0[:, 1] < i][0][0] - j) / j)
    for i, j in zip(exp_bcc2[0, :], exp_bcc2[1, :]):
        if i > plimit_sub2:
            continue
        ncount += 1
        nsum.append(np.abs(bcc_rh0[bcc_rh0[:, 1] < i][0][0] - j) / j)
    for i, j in zip(exp_bcc4_1[0, :], exp_bcc4_1[1, :]):
        if i > plimit_sub2:
            continue
        ncount += 1
        nsum.append(np.abs(bcc_rh0[bcc_rh0[:, 1] < i][0][0] - j) / j)
    for i, j in zip(exp_bcc4_2[0, :], exp_bcc4_2[1, :]):
        if i > plimit_sub2:
            continue
        ncount += 1
        nsum.append(np.abs(bcc_rh0[bcc_rh0[:, 1] < i][0][0] - j) / j)
    for i, j in zip(exp_bcc5[0, :], exp_bcc5[1, :]):
        if i > plimit_sub2:
            continue
        ncount += 1
        nsum.append(np.abs(bcc_rh0[bcc_rh0[:, 1] < i][0][0] - j) / j)
    # ------------------ with mcmahone for P>60 ------------------
    nsum = []
    ncount = 0
    for i, j in zip(exp_bcc4_1[0, :], exp_bcc4_1[1, :]):
        if i > plimit_sub2:
            ncount += 1
            nsum.append(np.abs(bcc_rh0[bcc_rh0[:, 1] < i][0][0] - j) / j)
            # print(i, j, bcc_rh0[bcc_rh0[:, 1] < i][0])
    for i, j in zip(exp_bcc4_2[0, :], exp_bcc4_2[1, :]):
        if i > plimit_sub2:
            ncount += 1
            nsum.append(np.abs(bcc_rh0[bcc_rh0[:, 1] < i][0][0] - j) / j)
            # print(i, j, bcc_rh0[bcc_rh0[:, 1] < i][0])
    # ------------------ with akahama for P>60 ------------------
    nsum = []
    ncount = 0
    for i, j in zip(exp_bcc5[0, :], exp_bcc5[1, :]):
        if i > plimit_sub2:
            # print(i, j)
            ncount += 1
            nsum.append(np.abs(bcc_rh0[bcc_rh0[:, 1] < i][0][0] - j) / j)
            # print(i, j, bcc_rh0[bcc_rh0[:, 1] < i][0])
    # ------------------ with akahama for whole range of P --------
    nsum = []
    ncount = 0
    for i, j in zip(exp_bcc5[0, :], exp_bcc5[1, :]):
        ncount += 1
        nsum.append(np.abs(bcc_rh0[bcc_rh0[:, 1] < i][0][0] - j) / j)
        # print(i, j, bcc_rh0[bcc_rh0[:, 1] < i][0])
    # --------------- Experiment Results --------------------------
    myscatter(ax, exp_bcc[0, :], exp_bcc[1, :],
              {"color": "blue",
               "marker": nbymarker[0], "s": 50,
               "label": r"Ding et al.(2007)"})
    # myscatter(ax, exp_rh[0, :], exp_rh[1, :],
    #           {"color": "white", "edgecolors": "blue",
    #            "marker":  nbymarker[0], "s": 50})
    myscatter(ax, exp_bcc3[0, :], exp_bcc3[1, :],
              {"color": "slateblue",
               "marker":  nbymarker[3], "s": 50,
               "label": r"Errandonea et al.(2019)"})
    # myscatter(ax, exp_rh3[0, :], exp_rh3[1, :],
    #           {"color": "white", "edgecolors": "slateblue",
    #            "marker":  nbymarker[3], "s": 50})
    myscatter(ax, exp_bcc2[0, :], exp_bcc2[1, :],
              {"color": "steelblue",
               "marker":  nbymarker[1], "s": 50,
               "label": r"Daniele et al.(2016)"})
    # myscatter(ax, exp_rh2[0, :], exp_rh2[1, :],
    #           {"color": "white", "edgecolors": "steelblue",
    #            "marker":  nbymarker[1], "s": 50})
    myscatter(ax, exp_bcc5[0, :], exp_bcc5[1, :],
              {"color": "slategrey",
               "marker": "d", "s": 50,
               r"label": "Akahama et al.(2021)"})
    myscatter(ax, exp_bcc4_1[0, :], exp_bcc4_1[1, :],
              {"color": "springgreen",
               "marker": "^", "s": 50,
               "label": "Stevenson et al.(2021)"})
    myscatter(ax, exp_bcc4_2[0, :], exp_bcc4_2[1, :],
              {"color": "springgreen",
               "marker": "^", "s": 50})
    ax.arrow(80+10, 0.92, 20, 0., color="plum",
             head_width=0.02, head_length=7.)
    myplot(ax, [1, 80], [0.8, 0.8],
           {"color": "plum", "linestyle": ":", "linewidth": 2.5})
    myplot(ax, [80, 80], [0.8, 0.99],
           {"color": "plum", "linestyle": ":", "linewidth": 2.5})
    myplot(ax, [1, 80], [0.99, 0.99],
           {"color": "plum", "linestyle": ":", "linewidth": 2.5})
    myplot(ax, [1, 1], [0.99, 0.8],
           {"color": "plum", "linestyle": ":", "linewidth": 2.5})
    ax.text(175, 0.5, r"$T=300K$", color="black",
            fontsize=25, fontname="Times New Roman")
    ax.set_xlim(-0.01, plimit)
    ax.set_ylim(0.48, 1.0)
    Fontname = "Times New Roman"
    Fontweight = "bold"
    Fontsize = 12
    ax.set_xlabel(r"Pressure (GPa)", fontsize=Fontsize+10,
                  fontname=Fontname, fontweight=Fontweight)
    ax.set_ylabel(r"Volume ($V/V_0$)", fontsize=Fontsize+8,
                  fontname=Fontname, fontweight=Fontweight)
    ax.legend(loc=(0.01, 0.02), fontsize=11.5)
    ax.grid(which="both", linestyle=":")
    ax.tick_params(labelsize=15)
    fig.savefig("./v.png", dpi=300,
                bbox_inches="tight")
    # plt.show()
    plt.close(fig)


if __name__ == '__main__':
    main()
