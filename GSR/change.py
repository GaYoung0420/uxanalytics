
with open("S1_.txt", "r") as f:
    example = f.read()
    newer = example.replace('#','\n')
    print(newer);


with open("S1_.csv", "w") as N:
        N.write(newer);

# 12개 피험자 파일 txt => csv 변환
# for i in range(1,13):
#     file = "S"+i
#     with open(file+".txt", "r") as f:
#         example = f.read()
#         newer = example.replace('#','\n')
#         print(newer);
#     with open(file+".csv", "w") as N:
#         N.write(newer);