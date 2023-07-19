import matplotlib.pyplot as plt
import numpy as np
from typing import Dict
from wordcloud import WordCloud

def wordcloud(dict: Dict[str, int], w:int = 12, h:int = 8)-> WordCloud:
    if not dict:  
        dict = {"NO WORDS": 1} 
    
    wordcloud = WordCloud(width = w * 100, 
                          height= h * 100,
                          background_color="white", 
                          prefer_horizontal=0.8,  
                          min_font_size=10, 
                          max_font_size=400).generate_from_frequencies(dict) 

    # Display the generated image  
    plt.figure(figsize=(w, h))  
    plt.imshow(wordcloud, interpolation="bilinear")  
    plt.axis("off")  
    return plt
