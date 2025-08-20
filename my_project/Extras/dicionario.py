carnes = {"picanha": 9, "maminha": 5, "linguiça": 5,}

print(carnes["picanha"])
carnes["suino"] = 30
print(carnes["suino"])
print(carnes)

if "frango" in carnes:
    print("tem frango")
else:
    print("nao tem frango")

if "maminha" in carnes:
    print("tem maminha")
else:
    print("nao tem maminha")

del carnes["maminha"]

if "maminha" in carnes:
    print("tem maminha")
else:
    print("nao tem maminha")