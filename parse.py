import json
from dominate.tags import *

def parse_upgrades(ship_type, build):
    upgrade_table=table()
    table_row=tr()
    upgrade_table.add(table_row)
    for index,upgrade_id in enumerate(build["upgrades"]):
        table_data=td()
        upgrade = img(src=resource[ship_type]["upgrades"][index][upgrade_id-1]["src"], title=resource[ship_type]["upgrades"][index][upgrade_id-1]["name"])
        table_data.add(upgrade)
        table_row.add(table_data)
    return str(upgrade_table)

def parse_skills(ship_type, build):
    skill_table=table(style="background-color:LightGray;border-radius:10px")
    for i in range(4):
        table_row=tr()
        for j in range(6):
            table_data=td()
            skill = img(src=resource[ship_type]["skills"][i][j]["src"], title=resource[ship_type]["skills"][i][j]["name"])
            if [i+1,j+1] in build["skills"]:
                skill["style"]=active_style
            table_data.add(skill)
            table_row.add(table_data)
        skill_table.add(table_row)
    return str(skill_table)

def parse_order(ship_type, build):
    order_table=table()
    table_row=tr()
    order_table.add(table_row)
    for skill in build["skills"]:
        table_data=td()
        skill_img = img(src=resource[ship_type]["skills"][skill[0]-1][skill[1]-1]["src"], title=resource[ship_type]["skills"][skill[0]-1][skill[1]-1]["name"])
        table_data.add(skill_img)
        table_row.add(table_data)
    return str(order_table)

if __name__=="__main__":
    resource=json.load(open("resource.json",encoding="utf-8"))
    build_list=json.load(open("builds.json",encoding="utf-8"))
    active_style="background-color:CornflowerBlue;border-radius:10px"
    output=""

    for country in build_list:
        output+="# {}\n".format(country)
        for ship_type in build_list[country]:
            output+="## {}\n".format(ship_type)
            for ship in build_list[country][ship_type]:
                output+="### {}\n".format(ship["ship"])
                for build in ship["builds"]:
                    output+="#### {} 来源:{}\n".format(build["name"],build["writer"])
                    output+="##### 配件\n"
                    output+=parse_upgrades(ship_type, build)
                    output+="##### 加点\n"
                    output+=parse_skills(ship_type, build)
                    if build["ordered"] == True:
                        output+="##### 加点顺序\n"
                        output+=parse_order(ship_type, build)
    print(output)
