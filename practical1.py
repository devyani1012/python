student={
    101:{"name":"raj","scores":[10,50,40]},
    102:{"name":"shruti","scores":[20,55,90]},
    103:{"name":"sayli","scores":[15,70,30]},
    104:{"name":"divya","scores":[70,58,70]},
}
for sid ,details in student.items():
    avg = sum(details["scores"])/len(details["scores"])
    details["average"]=avg
    details["passed"]=avg>=50

print("name of passed student:")


for sid,details in student.items():
    if details["passed"]:
        print(details["name"])   