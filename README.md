# 🇳🇵 Nepal Land Use Dashboard

An interactive data visualization dashboard built using **Plotly Dash** and **Bootstrap** to explore land use trends in Nepal from 1967 to 2010. The app includes line charts, pie charts, and responsive UI elements for dynamic insights into land distribution over time.
 
--- 

## 📦 Features

* 📈 Interactive line chart for land use trends over time
* 🥧 Pie chart showing land distribution for a selected year
* 📋 Dropdown to filter land use types
* 🕹️ Slider to pick a specific year
* 🎨 Responsive, modern UI with Bootstrap components

---

## 📊 Dataset

* **Source**: [Open Data Nepal - Land Use Statistics (1967–2010)](https://opendatanepal.com/dataset/land-use-statistics-of-nepal/resource/267f2676-71f6-4b8b-ac05-59cfd90ec3c1)
* **Format**: CSV
* **Attributes**:

  * `Land Use Type`
  * Land distribution (%) across years: `1967`, `1978`, `1991`, `2000`, `2010`

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/heisenbergsandip/basic_app-on-plotlydash.git
cd nepal-land-dashboard
```

### 2. Install Dependencies

Use pip to install the required libraries:

```bash
pip install dash dash-bootstrap-components pandas plotly
```

---

## 🚀 Run the App

```bash
python app.py
```

Navigate to: [http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## 🧠 Tech Stack

* [Dash](https://dash.plotly.com/) - Python framework for analytical web apps
* [Plotly](https://plotly.com/python/) - Interactive graphing library
* [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) - Bootstrap components for Dash
* [Pandas](https://pandas.pydata.org/) - Data manipulation

---

## 📁 File Structure

```
├── app.py              # Main Dash app
├── README.md           # Project documentation
```

---

## 📸 Screenshots

[Screenshot](images/Screenshot 2025-05-29 194856.png)
[Screenshot](images/Screenshot 2025-05-29 194927.png)
[Screenshot](images/Screenshot 2025-05-29 195001.png)
 

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Contribution

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

---

Let me know if you'd like this in a downloadable format or want to include deployment instructions (like Heroku, Render, or Docker).
