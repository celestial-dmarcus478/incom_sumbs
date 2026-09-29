celestialpeople = {"Jake":[90,120,130,80,110,120,60],
            "Ben":[140,90,70,90,120,130,100],
            "Sally":[140,90,100,60,140,80,90]
}

print("summary of blood sugar of patients")
for person,level in celestialpeople.items():
    print(32*"=")
    print(person, level)
    for value in level:
        if value>120:
            print(value,": High")
        else:
            print(value, ": Normal")
    celestialavggl = sum(level) / len(level)
    celestialtopgl = max(level)
    celestialwsgl = min(level)
    celestialdiff=celestialtopgl-celestialwsgl
    print(f"Highest blood sugar of {person}: ", celestialtopgl)
    print(f"Lowest blood sugar of {person}: ", celestialwsgl)
    print("celestialdifference in level: ",celestialdiff)
    print(f"Average blood sugar of {person}: ", celestialavggl)
