## <span style="color: #2E86C1;"> Campaign Conversion Checker 📈</span>

Track campaign leads and match them with real business opportunities.  
Designed for marketing teams to easily identify which campaign contacts converted into actual opportunities.

---

### <span style="color: #2E86C1;"> Features ✨</span>

- **📂 Upload Master File** – Contains registration details of ALL business opportunities.
![Upload Master File](/images/step_1.png)

- **📂 Upload Campaign File** – Leads generated from a specific campaign.
![Upload Master File](/images/step_2.png)

- **⚙ Campaign Parameters** – Start date, query period, distributor, and target country.
![Upload Master File](/images/step_3.png)

- **🔍 Automated Matching** – Finds leads that became business opportunities.
![Upload Master File](/images/matches.png)

- **📊 Results Dashboard** – One-stop solution to determine campaign effectiveness (i.e cost per lead, lead-to-opportunity conversion, acergae time-to-conersion,etc) [IN PROGRESS]


---

### <span style="color: #2E86C1;"> Tech Stack 🛠</span>

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask)  
- **Data Handling:** Pandas, OpenPyXL  
- **Server:** Local development server (`localhost:8080`)

---

### <span style="color: #2E86C1;">📂 Project Structure</span>
├── app.py # Flask backend server
├── index.html # Frontend UI
└── README.md # Project documentation


---

### <span style="color: #2E86C1;">Instructions! LETS GO 🚀 </span>

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/campaign-conversion-checker.git
cd campaign-conversion-checker
```

2. **Install dependencies (requires Python 3.8+):**
```bash
pip install -r requirements.txt
```

3. **Run the backend server**
```bash
python app.py
```
...and access it at 
```arduino
http://localhost:8080
```

<span style="color: #2E86C1;">Notes</span>
Runs locally – no external storage.
For deployment, update API_BASE in index.html to your backend URL.

<span style="color: #2E86C1;">License</span>
This project is licensed under the MIT License.