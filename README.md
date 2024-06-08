# GoFresh Project

GoFresh is a web application developed using Flask, which utilizes an SQLite database for data storage. This application is designed to run in a virtual environment.

# Demo



https://github.com/ashish-sreevatsav/GoFresh/assets/115939043/c4430a41-c0d1-4944-aa2c-a363aa725a48



## Description

### app.py
This is the main entry point of the application. It initializes the Flask app and sets up the routes.

### grocery_models.py
This file contains the database models used by the application.

### grocery_services.py
This file contains the business logic and service functions used in the application.

### grocery_store.db
This is the SQLite database file where the data is stored.

### requirements.txt
This file lists all the Python dependencies required to run the project.

### sample.py
A sample script for demonstrating various functionalities of the project.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gofresh.git
   cd gofresh
   ```
2. **Create a virtual environment:**
  ```bash
  python3 -m venv venv
  ```
3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the application:**
   ```bash
   flask run
   ```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

**Navigate to the home page:**
Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

**Interact with the application:**
Use the UI to interact with the grocery store database, add items, view items, and perform other operations as implemented in the app.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgments

Thanks to all the contributors and open-source libraries that made this project possible.


Feel free to adjust any section to better match your project's specifics and ensure everything is accurate for your implementation.

