import json
from dominate.tags import *
resource=json.load(open("resource.json"))

activestyle="background-color:CornflowerBlue;border-radius:10px"
skilltable=table(style="background-color:LightGray;border-radius:10px")
for i in range(4):
    table_row=tr()
    for j in range(6):
        table_data=td()
        skill = img(src=resource["CV"]["skills"][i][j]["src"], title=resource["CV"]["skills"][i][j]["name"])
        skill["style"]=activestyle
        table_data.add(skill)
        table_row.add(table_data)
    skilltable.add(table_row)
print(skilltable)