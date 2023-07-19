import matplotlib.pyplot as plt
def histogram_labels(labels):
    data = [0] * (labels.max() + 1)
    
    for label in labels:
        data[label] += 1
    
    plt.hist(data)

    # add labels and title to the chart  
    plt.xlabel("Cluster size")  
    plt.ylabel("Frequency")  
    plt.title("Cluster size Frequency Histogram")  
    plt.show()