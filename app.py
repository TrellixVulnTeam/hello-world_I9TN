from flask import Flask, render_template
app = Flask(__name__)

id_game = {
    1: 'Dragon & Warrior'
}

events = {
    -1: '任务板',
    0: '新手村',
    1: '隔壁村子',
    2: '商店呀', 
    3: '野外',
    4: '龙谷呀',
    5: '不存在的'
}

@app.route('/')
def render_homepage():
   return render_template('index.html')

# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name

@app.route('/game')
def render_games():
    return render_template('games.html')

@app.route('/game/<id>')
def render_game(id):
    return render_template('game.html', id=id, title=id_game[int(id)],  next=[events[0], "", "", ""])

@app.route('/game/<id>/<event>')
def render_game_event(id, event):
    
    if event == events[-1]:
        next = [events[1], "", "", ""]
    elif event == events[0]:
        next = [events[1], "", "", ""]
    elif event == events[1]:
        next = [events[2], events[3], "", ""]
    elif event == events[2]:
        next = [events[1], events[3], "", ""]
    elif event == events[3]:
        next = [events[1], events[2], events[4], ""]
    elif event == events[4]:
        next = [events[5], "", "", ""]
    elif event == events[5]:
        next = [events[-1], "", "", ""]
    return render_template('game.html', id=id, title=id_game[int(id)], next=next)

if __name__ == '__main__':
   app.run(debug = True)
