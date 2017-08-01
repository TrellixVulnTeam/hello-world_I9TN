from flask import Flask, render_template
app = Flask(__name__)

id_game = {
    1: 'Dragon & Warrior'
}

events = {
    -1: '重新开始',
    0: '开始游戏',
    1: '去麦基家',
    2: '去老爷爷家的商店', 
    3: '去野外',
    4: '打怪',
    5: '你死了'
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
