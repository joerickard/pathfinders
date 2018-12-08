from flask import Flask
app = Flask(__name__)

@app.route('/')
def page1():
    return '<!DOCTYPE html><html><body><h1>Executive Summary</h1><p>We met with Rischelle and did some research.</p><a href="/background">Background</a></body></html>'

@app.route('/background')
def page2():
    return '<!DOCTYPE html><html><body><h1>Background Section</h1><p>What is the state of commuting on campus? what are the goals of our stakeholders?</p><a href="/">Executive Summary</a></body></html>'

@app.route('/goals')
def page3():
    return 'goals'

@app.route('/research')
def page4():
    return 'research!'

@app.route('/map')
def page5():
    return 'Map here!'

@app.route('/analysis')
def page6():
    return 'Analysis'
