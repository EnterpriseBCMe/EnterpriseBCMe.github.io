#coding:utf-8
import json

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()
 
    def __call__(self): return self.impl()
 
 
class _GetchUnix:
    def __init__(self):
        import tty, sys
 
    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
 
 
class _GetchWindows:
    def __init__(self):
        import msvcrt
 
    def __call__(self):
        import msvcrt
        return msvcrt.getch()
 

country_code={
    "E":"英联邦",
    "W":"欧洲",
    "F":"法国",
    "D":"德国",
    "I":"意大利",
    "R":"日本",
    "H":"荷兰",
    "V":"泛美",
    "C":"泛亚",
    "S":"苏联",
    "P":"西班牙",
    "M":"美国",
    "Y":"英国"
}
ship_type={
    "CV":"航空母舰",
    "BB":"战列舰",
    "CA":"巡洋舰",
    "DD":"驱逐舰",
    "SS":"水下舰种"
}

def calculate_total_points(skills):
    total_point=0
    for skill in skills:
        total_point+=skill[0]
    return total_point
    
if __name__=="__main__":
    resource_file=json.load(open("resource.json",encoding="utf-8"))
    getch = _Getch()
    while True:
        fp=open("builds.json","r",encoding="utf-8")
        out_file=json.load(fp)
        fp.close()
        # 国家选择
        print("选择国家：")
        for code in country_code:
            print("{}:{} ".format(code,country_code[code]),end = "")
        country = input("\n:").upper()
        if not country in country_code:
            print("国家代码格式不正确")
            continue
        if not country_code[country] in out_file:
            out_file[country_code[country]]={}
        country_level=out_file[country_code[country]]
        
        # 舰种选择
        print("选择舰种：")
        for stype in ship_type:
            print("{}:{} ".format(stype,ship_type[stype]),end = "")    
        stype = input("\n:").upper()
        if not stype in ship_type:
            print("舰种代码格式不正确")
            continue
        if not ship_type[stype] in country_level:
            country_level[ship_type[stype]]={}
        stype_level=country_level[ship_type[stype]]
        
        # 创建新船
        ship_name=input("输入船名：")
        if not ship_name in stype_level:
            stype_level[ship_name]={}
        builds_level=stype_level[ship_name]
        
        # 创建配置
        build_name=input("输入配置名称：")
        while build_name in builds_level:
            print("配置名已存在")
            build_name=input("输入配置名称：")
        new_build={
            "writer":"",
            "upgrades":[],
            "ordered":False,
            "skills":[],
            "description":""
        }
        new_build["writer"]=input("输入作者：")
        
        # 读取插件选择
        for i in range(6):
            print()
            print("{}号插件槽".format(i+1))
            for index, upgrade in enumerate(resource_file[ship_type[stype]]["upgrades"][i]):
                print("{}：{}".format(index+1,upgrade["name"]))
            upgrade_choose=int(getch())-1
            new_build["upgrades"].append(upgrade_choose+1)
            print("{}号插件槽选择{}：{}".format(i+1,upgrade_choose+1,resource_file[ship_type[stype]]["upgrades"][i][upgrade_choose]["name"]))
        
        # 读取技能选择
        total_points=21
        print("进行技能选择")
        print("当前技能加点是否有先后顺序？（0=无序，1=有序）")
        ordered=bool(getch())
        new_build["ordered"]=ordered
        for i in range(len(resource_file[ship_type[stype]]["skills"])):
            for j in range(len(resource_file[ship_type[stype]]["skills"][i])):
                print("{}-{}：{:8}".format(i+1, j+1, resource_file[ship_type[stype]]["skills"][i][j]["name"]),end="")
            print("")
        while calculate_total_points(new_build["skills"]) < 21:
            first_id=int(getch())
            second_id=int(getch())
            print("{}-{}".format(first_id,second_id))
            new_build["skills"].append([first_id,second_id])
        new_build["description"]=input("输入一段简介：")
        print("完成录入！")
        print(new_build)
        save=bool(input("是否确认保存该配置（0=不保存，1=保存）"))
        if save==True:
            builds_level[build_name]=new_build
            print("当前配置已保存")
        else:
            print("未保存")
        fp=open("builds.json","w",encoding="utf-8")
        json.dump(out_file, fp,ensure_ascii=False)
        fp.close()