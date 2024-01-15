# Simple Sushi Website Using Flask

This repository contains a Flask application for managing promotions and user data for a sushi website. The application includes features such as updating promotions, user authentication, and real-time chart updates.

## Features

### 1. Promotions Management
- **Update Promotions:** The `/update_promotions` route allows adding new promotions or removing existing ones via POST requests. Promotions are stored in a CSV file (`promotions.csv`).

- **Get Promotions:** The `/get_promotions` route retrieves the list of promotions from the CSV file.

### 2. User Management
- **Login:** Users can log in through the `/login` route, providing their username, password, and role. Authentication is performed against user data stored in `users.csv`.

- **Add User:** The `/add_user` route allows adding new users with a username, password, and role. User data is stored in `users.csv`.

### 3. Chart Data Visualization
- The application provides a homepage (`/`) with a chart displaying sample data.

- **Real-time Chart Updates:** The `/update_chart` route allows updating chart data dynamically. The chart data is stored and retrieved from the server.

### 4. Additional Pages
- The application includes pages for monitoring (`/monitoring`) and updating (`/updating`).

## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/your-username/FlaskProject.git
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the application:

   ```
   python app.py
   ```

   The application will run in debug mode, accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. **Promotions Management:**
   - Add new promotions or remove existing ones through the `/update_promotions` route using POST requests.

2. **User Management:**
   - Log in via the `/login` route with a valid username, password, and role.
   - Add new users through the `/add_user` route.

3. **Chart Data Visualization:**
   - Explore the sample chart on the homepage (`/`).
   - View real-time updates on the monitoring page (`/monitoring`).

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Flask framework and its contributors.
- [Chart.js](https://www.chartjs.org/) for the chart visualization.
- Other open-source libraries used in this project.

Thank you for using and contributing to the FlaskProject!
