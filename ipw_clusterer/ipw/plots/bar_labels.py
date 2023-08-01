import matplotlib.pyplot as plt  
  
def bar_labels(labels):  
    label_dict = {}  
          
    for label in labels:  
        if label in label_dict:  
            label_dict[label] += 1  
        else:  
            label_dict[label] = 1  

    sorted_labels = sorted(label_dict.items())  
  
    plt.bar([f'Cluster {key}' for key, value in sorted_labels], [value for key, value in sorted_labels])  
  
    # add labels and title to the chart    
    plt.xlabel("Cluster size")    
    plt.ylabel("Frequency")    
    plt.title("Cluster size per cluster")    
    plt.show()  