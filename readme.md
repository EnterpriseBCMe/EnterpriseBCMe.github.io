- [x] 根据配置更新页面内容
- [x] 命令行构建配置
- [ ] 使用爬虫在线获取对应船只的可选配件列表
- [ ] 水下舰种的resource
## parse.py
将builds.json中的配置直接格式化写入source/_posts/舰长技能与配件.md中
```bash
python parse.py
```
## builds_example.json
配置文件示例
## cli_reader.py
运行后开启一个交互式程序以生成配置。保存至builds.json中
```bash
python cli_reader.py                                                  
选择国家：
E:英联邦 W:欧洲 F:法国 D:德国 I:意大利 R:日本 H:荷兰 V:泛美 C:泛亚 S:苏联 P:西班牙 M:美国 Y:英国 
:m
选择舰种：
CV:航空母舰 BB:战列舰 CA:巡洋舰 DD:驱逐舰 SS:水下舰种 
:cv
输入船名：合众国
输入配置名称：build2
输入作者：syh

1号插件槽
1：空军大队修改型1
2：辅助武器修改型1
3：伤害控制小组修改型1
1号插件槽选择1：空军大队修改型1

2号插件槽
1：伤害控制系统修改型1
2：飞机引擎修改型1
2号插件槽选择2：飞机引擎修改型1

3号插件槽
1：副炮组修改型1
2：鱼雷轰炸机修改型1
3：攻击机修改型1
4：空投鱼雷修改型1
3号插件槽选择4：空投鱼雷修改型1

4号插件槽
1：空袭修改型1
2：攻击机修改型2
3：伤害控制系统修改型2
4：轰炸机修改型2
5：鱼雷轰炸机修改型2
4号插件槽选择4：轰炸机修改型2

5号插件槽
1：隐蔽系统修改型1
2：飞行控制修改型1
3：中队消耗品修改型1
5号插件槽选择2：飞行控制修改型1

6号插件槽
1：空军大队修改型2
2：辅助武器修改型2
3：飞行控制修改型2
6号插件槽选择3：飞行控制修改型2
进行技能选择
当前技能加点是否有先后顺序？（0=无序，1=有序）
1-1：最后一博    1-2：改进型引擎增压 1-3：引擎技师    1-4：制空权     1-5：战斗机指挥中心 1-6：寻而击之    
2-1：鱼雷轰炸机   2-2：空投鱼雷加速  2-3：改进型引擎   2-4：维修专员    2-5：副武器专家   2-6：巡逻队长    
3-1：稳定瞄准    3-2：增强型穿甲弹药 3-3：起火专家    3-4：飞机装甲    3-5：生存专家    3-6：截击机     
4-1：轰炸机飞行控制 4-2：近发引信    4-3：近战专家    4-4：增强型飞机装甲 4-5：隐蔽威胁    4-6：迅速反应    
1-4
2-3
3-5
4-6
4-2
3-4
3-1
1-2
输入一段简介：1112
完成录入！
{'writer': 'syh', 'upgrades': [1, 2, 4, 4, 2, 3], 'ordered': True, 'skills': [[1, 4], [2, 3], [3, 5], [4, 6], [4, 2], [3, 4], [3, 1], [1, 2]], 'description': '1112'}
是否确认保存该配置（0=不保存，1=保存）1
当前配置已保存
```
