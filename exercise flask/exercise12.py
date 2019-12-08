from flask import Flask, render_template

app = Flask(__name__)
# =============================================================================
#                           exercises 1
# =============================================================================

@app.route('/')
def index():
    return "This is the Index page"

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/members')
def members():
    return "Members Page!"

# =============================================================================
#                           exercises 2
# =============================================================================
 
    

@app.route('/scores/<int:score>')
def score(score):
    return render_template('pass.html', score = score)


# =============================================================================
#                           exercises 3
# =============================================================================
    
@app.route('/color')
def color():
    return render_template("index.html")




if __name__ == '__main__':
    app.run()