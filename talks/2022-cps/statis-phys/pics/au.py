from matplotlib import pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
import sys
sys.path.append("/home/nby/study/NBY-Lib/")
from nbyplot import myplot, myscatter, myfig_setup_notitle, nbymarker, nbycolor
import units
sys.path.append("/home/nby/study/gold/")
from exp_hugoniot import exp1_fcc, exp1_bcc
from exp_hugoniot import exp2_fcc, exp2_bcc, exp3, theo1


def main():
    Fontweight = "bold"
    Fontsize = 12
    phasecolor = {"fcc": "magenta", "bcc": "blue",
                  "hcp": "orange", "dia": "black"}
    filedir = "/home/nby/study/gold/hugoniot/"
    # fcc300k_pbesol = np.loadtxt(filedir + "FCC-300K-PBEsol.dat")
    fcc = np.loadtxt(filedir + "FCC-PAW-LDA.dat")
    fcc_cubic = np.loadtxt(filedir + "FCC-PAW-LDA-cubic.dat")
    fcc_rh = np.loadtxt(filedir + "FCC-PAW-LDA-rh.dat")
    bcc_rh = np.loadtxt(filedir + "BCC-PAW-LDA-rh.dat")
    # ----------------------------------------------------------------
    figpv, axpv = plt.subplots()
    # fcc, = myplot(axpv, fcc[:, 0], fcc[:, 1],
    #               {"color": phasecolor["fcc"],
    #                "linestyle": "-.",
    #                # "marker": "*",
    #                "linewidth": "1",
    #                "label": "FCC-LDA"})
    # fcc_cubic, = myplot(axpv, fcc_cubic[:, 0], fcc_cubic[:, 1],
    #                     {"color": phasecolor["fcc"],
    #                      "linestyle": ":",
    #                      # "marker": "D",
    #                      "linewidth": "1",
    #                      "markersize": "3",
    #                      "mfc": "none",
    #                      "label": "FCC-LDA(cubic)"})
    fcc_rh, = myplot(axpv, fcc_rh[:, 0], fcc_rh[:, 1],
                     {"color": phasecolor["fcc"],
                      "linestyle": "-.",
                      # "marker": "D",
                      "linewidth": "1.5",
                      "markersize": "3",
                      "mfc": "none",
                      "label": "DIA"})
    e1_f, = myplot(axpv, exp1_fcc[:, 0], exp1_fcc[:, 1],
                   {"linestyle": "none",
                    "marker": "+",
                    "mfc": "none",
                    "mec": phasecolor["fcc"],
                    "ms": 6,
                    "label": r"Briggs et al. Phys.Rev.Lett.(2019)"})
    e1_b, = myplot(axpv, exp1_bcc[:, 0], exp1_bcc[:, 1],
                   {"linestyle": "none",
                    "marker": "+",
                    "mfc": "none",
                    "mec": phasecolor["bcc"],
                    "ms": 6})
    e2_fcc, = myplot(axpv, exp2_fcc[0], exp2_fcc[1],
                     {"linestyle": "none",
                      "marker": "s",
                      "mfc": "none",
                      "mec": phasecolor["fcc"],
                      "ms": 6,
                      "label": "Sharma et al. Phys.Rev.Lett.(2019)"})
    e2_bcc, = myplot(axpv, exp2_bcc[:, 0], exp2_bcc[:, 1],
                     {"linestyle": "none",
                      "marker": "s",
                      "mfc": "none",
                      "mec": phasecolor["bcc"],
                      "ms": 6})
    e3, = myplot(axpv, exp3[:, 0], exp3[:, 1],
                 {"linestyle": "none",
                  "marker": "p",
                  "mfc": "none",
                  "mec": phasecolor["fcc"],
                  "ms": 6,
                  "label": "Yokoo et al. Appl.Phys.Lett.(2008)"})
    t1, = myplot(axpv, theo1[-1::-1, 0], theo1[-1::-1, 1],
                 {"linestyle": ":",
                  "linewidth": 1.5,
                  # "marker": "none",
                  "mfc": "none",
                  "mec": phasecolor["fcc"],
                  "ms": 6,
                  "label": "Sirmnov J.Phys.:Condens.Matter(2017)"})

    # axpv.text(22, 80,
    #           r"$T=300K$", color="black",
    #           fontsize=15, fontname="Times New Roman")
    myfig_setup_notitle(axpv,
                        r"Density (g/cm$^3$)",
                        r"Pressure (GPa)", Fontsize)
    # axpv.set_xlim(19, 25.5)
    # axpv.set_ylim(-0.05, 140)
    # plt.show()
    # ----------- for lengend format ----------------------------
    # -----------------------------------------------------------
    # xmajor = MultipleLocator(20)
    # xminor = MultipleLocator(10)
    # ymajor = MultipleLocator(2)
    # yminor = MultipleLocator(1)
    # axpv.xaxis.set_major_locator(xmajor)
    # axpv.yaxis.set_major_locator(ymajor)
    # axpv.xaxis.set_minor_locator(xminor)
    # axpv.yaxis.set_minor_locator(yminor)
    axpv.tick_params(axis="both", which="major", labelsize=12)
    axpv.set_xlim(24, 34)
    axpv.legend(fontsize=10)
    # plt.show()
    figpv.savefig("./hugoniot.png", bbox_inches="tight",
                  format="png", dpi=300)


if __name__ == '__main__':
    main()
