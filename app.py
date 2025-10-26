from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    """Renders the mobile transit pass page."""
    return render_template('transit_pass.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)