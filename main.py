from flask import Flask, render_template

from database.db_session import init_database_session
from database.dao import get_all_users, get_all_deals
from database.tables.deals_history import DealHistory
from database.tables.users import User
from utils import table_fields

init_database_session()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/users")
def users():
    return render_template('users.html', fields=table_fields(User), users=get_all_users())


@app.route("/deals")
def deals():
    return render_template('deals.html', fields=table_fields(DealHistory), deals=get_all_deals())
