studentsL={"Ana":[90,85,82],
          "Kirk":[72,73,78],}
studentsT={"Ana":(90,85,82),
          "Kirk":(72,73,78),}
for ppl,nummy in studentsL.items():
    print(ppl,*nummy)
for a, b in studentsT.items():
    print(a, *b)
