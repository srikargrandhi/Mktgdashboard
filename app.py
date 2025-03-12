# app.py - Flask application to serve the Market Analysis Dashboard

# 1. Import and configure Flask
from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Define the path to the data directory (relative to app.py)
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# 2. Serve the main dashboard page at the root route ("/")
@app.route('/')
def index():
    """
    Route for the root URL ("/").
    Renders the index.html template from the templates folder, which is the main dashboard page.
    """
    return render_template('index.html')

# 3. API endpoint to serve marketShare.json data
@app.route('/api/marketShare')
def get_market_share():
    """
    API endpoint for /api/marketShare.
    Reads data from data/marketShare.json and returns it as JSON.
    """
    try:
        with open(os.path.join(DATA_DIR, 'marketShare.json'), 'r') as f:
            market_share_data = json.load(f)
        return jsonify(market_share_data)
    except FileNotFoundError:
        return jsonify({"error": "marketShare.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding marketShare.json"}), 500

# 3. API endpoint to serve revenueTrends.json data
@app.route('/api/revenueTrends')
def get_revenue_trends():
    """
    API endpoint for /api/revenueTrends.
    Reads data from data/revenueTrends.json and returns it as JSON.
    """
    try:
        with open(os.path.join(DATA_DIR, 'revenueTrends.json'), 'r') as f:
            revenue_trends_data = json.load(f)
        return jsonify(revenue_trends_data)
    except FileNotFoundError:
        return jsonify({"error": "revenueTrends.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding revenueTrends.json"}), 500

# 3. API endpoint to serve marketSegmentation.json data
@app.route('/api/marketSegmentation')
def get_market_segmentation():
    """
    API endpoint for /api/marketSegmentation.
    Reads data from data/marketSegmentation.json and returns it as JSON.
    """
    try:
        with open(os.path.join(DATA_DIR, 'marketSegmentation.json'), 'r') as f:
            market_segmentation_data = json.load(f)
        return jsonify(market_segmentation_data)
    except FileNotFoundError:
        return jsonify({"error": "marketSegmentation.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding marketSegmentation.json"}), 500

# 4. Serve static files (if needed)
# In this example, static files are not explicitly needed as D3.js is loaded from CDN
# However, if you have CSS or JS files in the 'static' folder, Flask will serve them automatically.
# For example, if you have a file at /static/css/style.css, you can access it in HTML like:
# <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
# No specific code is needed here in app.py to enable static file serving as it's a default Flask feature.

# 5. Run the Flask app
if __name__ == '__main__':
    app.run(debug=True) # Set debug=True for development to enable automatic reloading

"""
Recommended Repository Structure:

market-analysis-dashboard/  (Root directory of your project - e.g., GitHub repository)
├── app.py                  (Flask application file - the code in this file)
├── templates/              (Folder for HTML templates)
│   └── index.html          (Dashboard HTML template - generated in previous step)
├── data/                   (Folder for JSON data files)
│   ├── marketShare.json    (Market share data - generated in the first step)
│   ├── revenueTrends.json    (Revenue trends data - generated in the first step)
│   └── marketSegmentation.json (Market segmentation data - generated in the first step)
├── static/                 (Optional folder for static assets like CSS, JS, images)
│   ├── css/                (Optional CSS files)
│   ├── js/                 (Optional JavaScript files)
│   └── images/             (Optional images)
├── README.md               (Project description, setup instructions, etc. - important for GitHub repos)
└── requirements.txt        (List of Python dependencies - useful for setting up the environment)

Explanation:
- Root directory: Keeps all project files organized under a single folder. This is the main project folder that you would upload to GitHub.
- app.py: Contains the core Flask application code.
- templates/: Stores HTML templates. Flask looks for templates in this folder by default.
- data/:  Stores the JSON data files that the Flask app serves. Keeping data separate makes the project cleaner.
- static/:  For static files like CSS stylesheets, JavaScript files (if you had any custom JS beyond D3.js CDN), and images. Although not strictly required in this example, it's good practice to include it for future expansion.
- README.md: A markdown file describing the project, how to set it up, and run it. Crucial for making your project understandable on GitHub.
- requirements.txt: Lists Python package dependencies (e.g., Flask). This is used to easily recreate the project's environment using 'pip install -r requirements.txt'. For this simple example, it would mainly contain 'Flask'.

This structure is a common and well-organized way to set up a Flask web application project, especially one intended for sharing on platforms like GitHub. It promotes clarity, maintainability, and makes collaboration easier.
"""
