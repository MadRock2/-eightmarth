from flask import Flask, redirect, render_template
# from DataBase import mongo

app = Flask(__name__, template_folder='C:/Users/MadRock/PycharmProjects/adminpanelEVEconomy/templates')
# app.config['MONGO_URI'] = 'mongodb+srv://MadRock:MadRock221mongodb@eveconomy.ap1ge.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
#
# mongo.init_app(app)


@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)