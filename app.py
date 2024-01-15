from flask import Flask, render_template, request, redirect, url_for, jsonify
import csv
import os
from datetime import datetime

app = Flask(__name__)
PROMOTIONS_FILE = 'promotions.csv'
chartData1 = [10, 20, 30, 40, 50, 60, 70]
chartData2 = [15, 25, 35, 45, 55, 65, 75]
chartData3 = [14, 30, 40, 50, 60, 70, 80]
# Function to load promotions from the file


def load_promotions():
    if os.path.exists(PROMOTIONS_FILE):
        with open(PROMOTIONS_FILE, 'r') as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)
    return []


def save_promotions(promotions):
    with open(PROMOTIONS_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(promotions)

# Function to update promotions


@app.route('/update_promotions', methods=['POST'])
def update_promotions():
    new_promotion = request.json.get('promotions')
    delete_promotion = request.json.get('remove_promotion')
    promotions = load_promotions()
    if new_promotion:
        promotions.append([len(promotions) + 1, new_promotion[0]])
        save_promotions(promotions)
        return jsonify({'message': 'Promotion added successfully'})
    elif delete_promotion:
        promotions = load_promotions()
        promotion_id = int(delete_promotion)
        promotions = [promotion for promotion in promotions if int(
            promotion[0]) != promotion_id]
        promotions = [[index + 1, promotion[1]]
                      for index, promotion in enumerate(promotions)]
        save_promotions(promotions)
        return jsonify({'message': 'Promotion deleted successfully'})
    else:
        return jsonify({'message': 'Invalid request'}), 400

# Function to get promotions


@app.route('/get_promotions', methods=['GET'])
def get_promotions():
    promotions = load_promotions()
    return jsonify({'promotions': promotions})
# Sample class for storing user data


class UserData:
    def __init__(self, username, password, new_role):
        self.username = username
        self.password = password
        self.new_role = new_role


# Store chart data on the server
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def loginPage():
    return render_template('loginPage.html')


def load_users():
    users = []
    with open('/Users/mac/Desktop/flaskproject/data/users.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)
    return users


def save_user(user):
    with open('/Users/mac/Desktop/flaskproject/data/users.csv', 'a', newline='') as csvfile:
        fieldnames = ['username', 'password', 'role']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty, and write the header if needed
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write the new user data
        writer.writerow({'username': user.username,
                        'password': user.password, 'role': user.new_role})
# Function to validate user data


def validate_user(username, password, login_type):
    users = load_users()
    user = next((user for user in users if user['username']
                == username and user['password'] == password), None)

    if user and user['password'] == password and user['role'] == login_type:
        return True
    else:
        return False


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        login_type = request.form['login-type']

        # Check if the user exists
        if validate_user(username, password, login_type):
            # Redirect to the monitoring page upon successful login
            return redirect(url_for('updating'))
        else:
            return "Invalid username, password, or login type."


@app.route('/updating')
def updating():
    return render_template('updating.html')


@app.route('/monitoring')
def monitoring():
    return render_template('graph.html', chartData1=chartData1, chartData2=chartData2, chartData3=chartData3)


@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        new_username = request.form['new-username']
        new_password = request.form['new-password']
        new_role = request.form['new-role']

        # Create a new UserData object
        new_user = UserData(new_username, new_password, new_role)

        # Save the new user to the CSV file
        save_user(new_user)

        # Redirect to the login page after adding a new user
        return redirect(url_for('loginPage'))
# Load data from CSV on startup
# Save data to CSV

# Update data on server startup


@app.route('/get_initial_chart_data', methods=['GET'])
def get_initial_chart_data():
    return jsonify({
        'success': True,
        'chartData1': chartData1,
        'chartData2': chartData2,
        'chartData3': chartData3,
    })


@app.route('/update_chart', methods=['POST'])
def update_chart():
    data = request.get_json()
    chart_index = int(data['chartIndex'])
    value = int(data['value'])
    current_day_index = datetime.today().weekday()

    if chart_index == 1:
        chartData1[current_day_index] = value
        updated_data = chartData1
    elif chart_index == 2:
        chartData2[current_day_index] = value
        updated_data = chartData2
    elif chart_index == 3:
        chartData3[current_day_index] = value
        updated_data = chartData3
    print(f"Updated chart {chart_index} data: {updated_data}")

    return jsonify(success=True, updatedData=updated_data)
# AJAX route to update the chart data


if __name__ == '__main__':
    app.run(debug=True)
