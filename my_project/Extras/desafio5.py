temp = [36.8, 37.5, 38.2, 37.0, 36.5, 39.1, 38.6]
febre = []
for grau in temp:
    if grau > 37.5:
        febre.append(grau)
    
print(febre)