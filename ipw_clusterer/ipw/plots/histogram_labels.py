import matplotlib.pyplot as plt
def histogram_labels(labels):
    label_dict = {}
        
    for label in labels:
        if label in label_dict:
            label_dict[label] += 1
        else:
            label_dict[label] = 1

    plt.hist(label_dict.values())

    # add labels and title to the chart  
    plt.xlabel("Cluster size")  
    plt.ylabel("Frequency")  
    plt.title("Cluster size Frequency Histogram")  
    plt.show()