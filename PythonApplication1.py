
from flask import Flask
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URL']='postgresql://.......@localhost/mydatabase'
#db=SQLAchemy(app)
#@app.route("/service")

@app.route('/service')


def service():
    conn = psycopg2.connect(database="dwh", user = "dwhuser", password = "Passw0rd", host = "dwhcluster.cgfjw1ky3oot.us-west-2.redshift.amazonaws.com", port = "5439")
    return "Service is running!"

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)