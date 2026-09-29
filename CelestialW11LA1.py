MachineLearning=[("SUPERVISED","DECISION TRUE"),
                 ("SUPERVISED","RANDOM FOREST"),
                 ("UNSUPERVISED","K-MEANS"),
                 ("UNSUPERVISED","GAUSSIAN MIXTURE MODEL")]
print("Learning Type:",MachineLearning[1][0])
for item in MachineLearning:
    if item[0]=="SUPERVISED":
        {print(item[1])}

print("Learning Type:", MachineLearning[2][0])
for item in MachineLearning:
    if item[0]=="UNSUPERVISED":
        {print(item[1])}
   