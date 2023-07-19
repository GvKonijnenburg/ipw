import matplotlib.pyplot as plt
import numpy as np
from typing import Dict

def histogram_wordfreq(dict):
#calculate the optimal distribution of bins according to Freedman-Draconis
    data = list(dict.values())

    # create bins for the histogram  
    #bins = np.exp(bins_sturge(np.log(data)))
    log_data = np.log(data)
    
    iqr = np.percentile(log_data, 75) - np.percentile(log_data, 25)
    bin_width = (2 * iqr) / (len(log_data) ** (1 / 3))
    log_bins = np.arange(min(log_data), max(log_data), bin_width)
    bins = np.exp(log_bins)

    # create the histogram  
    alpha = 1
    plt.hist(data, bins=bins, align='left', color = 'blue', alpha = alpha)

    # add labels and title to the chart  
    plt.xlabel("Frequency (log scale)")  
    plt.ylabel("Occurrences (log scale)")  
    plt.title("Word Frequency Histogram")  

    # set the axis to a logarithmic scale  
    plt.xscale('log')  
    plt.yscale('log')  

    return plt