import cracker as core
import time

chinese_options = [
    "解锁关卡到僵王博士 (5-10)",
    "解锁迷你游戏 益智模式 生存模式",
    "解锁所有迷你游戏的关卡",
    "解锁所有益智模式的关卡",
    "解锁所有生存模式的关卡",
    "破解金币到最高值"
]

options = {
    "Crack_Zombie_Doctorate": 1,
    "Crack_Other_Games": 2,
    "Crack_Mini_Game": 3,
    "Crack_Puzzle_Game": 4,
    "Crack_Survival_Game": 5,
    "Crack_Coins": 6
}

directory = "C:\\ProgramData\\PopCap Games\\PlantsVsZombies\\userdata\\"

info = """欢迎使用 PVZ Cracker 1.0! 
以下是您的可选修改操作: (修改第一次创建的用户 (user1.dat))
工具会默认生成一个 user1.dat.bak 文件，如需要还原操作请直接修改文件名替换 user1.dat 即可
"""
print(info)
print("默认修改目录:", directory, "\n")
for option in chinese_options:
    print('  ', end='')
    print(f"{option}: {list(options.values())[chinese_options.index(option)]}")
print('\n')

select = input("请输入您想修改的序号: ")

try:
    select = int(select)
except:
    print("请输入数字")

if select in options.values():
    exec(f"core.{list(options.keys())[select-1].lower()}(directory)")
    print("修改成功! ")
    time.sleep(0.5)
else:
    print("您的序号不在可修改操作中")