from flask import Flask,render_template
from flask import request
import random

app = Flask(__name__,template_folder="./")

@app.route('/')
def index():
    return render_template('index')

@app.route('/templates/grid', methods=['POST'])
def generate_grid():
    n = int(request.form['dimension'])
    grid = generate_grid_map(n)
    return render_template('grid', grid=grid)

def generate_grid_map(n):
    # Generate your grid map logic here
    #grid = [[0] * n for _ in range(n)]
    grid = grid = [[random.randint(0,1) for _ in range(n)] for _ in range(n)]
    return grid

if __name__ == "__main__":
    app.run(debug=True)