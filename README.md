Here’s your **updated README** with a **Render deploy badge** and **corrected workflow section removed** (since you don’t have GitHub Actions yet). You can copy this directly into your `README.md`:

---

# Flask CI/CD App

A simple **Flask web application** with **CI/CD pipeline** integrated and deployed using [Render](https://render.com).

## Features

* Flask-based Python web app
* CI/CD ready (can be extended with GitHub Actions or any CI pipeline)
* Continuous deployment on Render
* Simple folder structure and clean code

---

## Live Demo

[![Render Status](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
App URL: **[https://your-app-name.onrender.com](https://your-app-name.onrender.com)** (update this after deployment)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sumit0920/flask_ci_cd_app.git
cd flask_ci_cd_app
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows use venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app locally

```bash
python app.py
```

The app will run at **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## Deploying to Render

1. Push your code to **GitHub**.
2. Go to [Render Dashboard](https://dashboard.render.com/).
3. Click **New > Web Service**.
4. Connect your GitHub repo and select branch `main`.
5. Set **Build Command**:

   ```bash
   pip install -r requirements.txt
   ```
6. Set **Start Command**:

   ```bash
   python app.py
   ```
7. Click **Deploy**. Render will build and deploy automatically.

---

## Future Improvements

* Add GitHub Actions workflow for automated CI tests
* Add unit tests and coverage reports
* Add Docker support

---

## License

This project is licensed under the MIT License.


