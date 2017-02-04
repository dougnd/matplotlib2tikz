# -*- coding: utf-8 -*-
""" Hatches test

This test tests patches support. Matplotlib hatches are translated
into patterns in PGFPlots

"""
desc = 'Hatches Chart'
phash = 'bded52636358a930'

def plot():
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    import numpy as np

    # plot data
    fig = plt.figure()

    x = np.arange(3)
    y1 = [1, 2, 3]
    y2 = [3, 2, 4]
    y3 = [5, 3, 1]
    w = 0.25

    mpl.rcParams['hatch.color'] = 'purple'

    ax = fig.add_subplot(221)
    ax.bar(x-w, y1, w, ec='k', color='b', align='center', hatch='\\')
    ax.bar(x,   y2, w, ec='k', color='g', align='center', hatch='/')
    ax.bar(x+w, y3, w, ec='k', color='r', align='center', hatch='x')
    ax = fig.add_subplot(222)
    ax.bar(x-w, y1, w, ec='b', color='w', align='center', hatch='|')
    ax.bar(x,   y2, w, ec='g', color='w', align='center', hatch='-')
    ax.bar(x+w, y3, w, ec='r', color='w', align='center', hatch='+')
    ax = fig.add_subplot(223)
    ax.bar(x-w, y1, w, ec='k', color='b', align='center', hatch='.')
    ax.bar(x,   y2, w, ec='k', color='g', align='center', hatch='.x')
    ax.bar(x+w, y3, w, ec='k',color='r', align='center', hatch='*')
    ax = fig.add_subplot(224)
    ax.bar(x-w, y1, w, ec='k',color='b', align='center', hatch='/\\')
    ax.bar(x,   y2, w, ec='k',color='g', align='center', hatch='|-')
    ax.bar(x+w, y3, w, ec='k',color='r', align='center', hatch='-|')

    return fig

