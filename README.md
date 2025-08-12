## <span style="color: #2E86C1;"> ✨ Campaign Conversion Checker ✨ </span>
Say goodbye to spreadsheet headaches, strained eyeballs and endless “just checking in” emails. I built a web-based bestie that instantly cross-checks campaign leads with your master opportunity list so you can see exactly which campaign leads have converted! 💅

---

<span style="color: #2E86C1;"> Features</span>

1. **Upload Master File** – Contains registration details of ALL business opportunities.
![Upload Master File](/images/step_1.png)

2. **Upload Campaign File** – Leads generated from a specific campaign.
![Upload Master File](/images/step_2.png)

3. **⚙Campaign Parameters** – Start date, query period, distributor, and target country.
![Upload Master File](/images/step_3.png)

4. **Automated Matching** – Finds leads that became business opportunities.
![Upload Master File](/images/matches.png)

5. **Results Dashboard** – One-stop solution to determine campaign effectiveness (i.e cost per lead, lead-to-opportunity conversion, acergae time-to-conersion,etc) 

    [in progress]


---

### <span style="color: #2E86C1;">Tech Stack </span>

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask)  
- **Data Handling:** Pandas, OpenPyXL  
- **Server:** Local development server (`localhost:8080`)

---

### <span style="color: #2E86C1;">Project Structure</span>
├── app.py # Flask backend server <br>
├── index.html # Frontend UI<br>
└── README.md # Project documentation<br>


---

### <span style="color: #2E86C1;">Instructions! LETS GOOOO 🚀 </span>

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

<span style="color: #2E86C1;">Notes:</span><br>
- Runs locally, no external storage. <br>
- For deployment, update API_BASE in index.html to your backend URL.<br>
- 

<span style="color: #2E86C1;">License:</span><br>
This project is licensed under the MIT License.


Happy Converting! 