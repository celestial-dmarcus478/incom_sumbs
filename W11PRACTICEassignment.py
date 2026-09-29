people = {"Jake":[90,120,130,80,110,120,60],
            "Ben":[140,90,70,90,120,130,100],
            "Sally":[140,90,100,60,140,80,90]
}

print("summary of blood sugar of patients")
for person,level in people.items():
    print(32*"=")
    print(person, level)
    for value in level:
        if value>120:
            print(value,": High")
        else:
            print(value, ": Normal")
    avggl = sum(level) / len(level)
    topgl = max(level)
    lwsgl = min(level)
    diff=topgl-lwsgl
    print(f"Highest blood sugar of {person}: ", topgl)
    print(f"Lowest blood sugar of {person}: ", lwsgl)
    print("Difference in level: ",diff)
    print(f"Average blood sugar of {person}: ", avggl)

