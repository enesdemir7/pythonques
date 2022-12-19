# Soru 6.
import re

def avg_len(sentence):
    sum=0
    words = re.findall(r'\b\w+\b', sentence)
    for word in words:
        sum+=len(word)   
    avg_len = sum / len(words)
    return avg_len

print(avg_len(".,?!:;=Elma, Portakal, Armut.,?!"))  
