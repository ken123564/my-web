from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# 用戶的初始數據
user_data = {
    'points': 0,
    'energy_level': 1,
    'achievements': []
}

# 等級名稱和描述
levels = {
    1: {"description": "巨嬰 - 最極端的肥宅狀態。", "image": "level1.jpeg"},
    2: {"description": "沙發戰士 - 花大部分時間在沙發上打電玩或追劇。", "image": "level2.jpg"},
    3: {"description": "宅魂至尊- 很少參與戶外或社交活動。", "image": "level3.jpg"},
    4: {"description": "螺旋進步者 - 開始有意識地提升自我，但進步緩慢。", "image": "level4.png"},
    5: {"description": "內向鍊成者 - 在現實與虛擬之間覺醒，邁向運動與社交的試煉之路，內心的堡壘逐漸重塑。", "image": "level5.png"},
    6: {"description": "鍛魂者 - 從混沌中鍛造出規律，身心步向無限進化", "image": "level6.jpeg"},
    7: {"description": "潮覺醒者 - 初步解鎖穿搭之道，踏上自信之巔的征途。", "image": "level7.jpg"},
    8: {"description": "型態修羅 - 外形與品味近乎完美，細節掌控者，型男之境近在咫尺。", "image": "level8.jpeg"},
    9: {"description": "時尚霸主 - 掌握潮流命脈，舉手投足皆為時尚法則的顯現。", "image": "level9.png"},
    10: {"description": "全村的希望 - 帥到逆天，顯示出自信、風度和健美身材的完美平衡。", "image": "level10.jpeg"}
}

# 主頁，包含所有遊戲入口和重置分數按鈕
@app.route('/')
def index():
    user_data['energy_level'] = 1 + user_data['points'] // 25  # 根據分數計算等級
    max_level = max(levels.keys())
    if user_data['energy_level'] > max_level:
        user_data['energy_level'] = max_level  # 等級限制在最高等級

    level_data = levels.get(user_data['energy_level'], {"description": "未知等級", "image": "default.jpg"})
    return render_template('index.html', user=user_data, level_description=level_data["description"], level_image=level_data["image"])

# 重置用戶數據
@app.route('/reset')
def reset():
    user_data['points'] = 0
    user_data['energy_level'] = 1
    user_data['achievements'] = []
    return redirect(url_for('index'))

# 新增骰子功能
@app.route('/roll-dice', methods=['POST'])
def roll_dice():
    # 隨機選擇遊戲 (1 到 5)
    game_number = random.randint(1, 5)
    return redirect(url_for(f'game{game_number}'))

# API: 更新用戶數據
@app.route('/update', methods=['POST'])
def update():
    game_points = int(request.form.get('points', 0))
    user_data['points'] += game_points
    user_data['achievements'].append(request.form.get('achievement'))
    return redirect(url_for('index'))

# 其他遊戲路由保持不變
@app.route('/game1')
def game1():
    return render_template('game1.html', user=user_data)

@app.route('/game2')
def game2():
    return render_template('game2.html', user=user_data)

@app.route('/game3')
def game3():
    return render_template('game3.html', user=user_data)

@app.route('/game4')
def game4():
    return render_template('game4.html', user=user_data)

@app.route('/game5')
def game5():
    return render_template('game5.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)
