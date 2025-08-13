## 𐙚 Campaign Conversion Checker 𐙚 
Say goodbye to spreadsheet headaches, strained eyeballs and endless “just checking in” emails. I built a web-based bestie that instantly cross-checks campaign leads with your master opportunity list so you can see exactly which campaign leads have converted! >ᴗ<

---

### ᯓᡣ𐭩 Features 
You can try it out yourself with the (synthetic) sample data provided! 

1. **Upload Master File** – Contains registration details of ALL business opportunities.
![Upload Master File](/images/step_1.png)

2. **Upload Campaign File** – Leads generated from a specific campaign.
![Upload Master File](/images/step_2.png)

3. **Campaign Parameters** – Start date, query period, distributor, and target country.
![Upload Master File](/images/step_3.png)
(If you are using the synthetic data, choose any date in 2024)
<br>
4. **Automated Matching** – Finds leads that became business opportunities.
![Upload Master File](/images/matches.png)

5. **Results Dashboard** – One-stop solution to determine campaign effectiveness (i.e cost per lead, lead-to-opportunity conversion, average time-to-conersion, etc) [in progress]


---

### ᯓᡣ𐭩 Tech Stack 

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Flask)  
- **Data Handling:** Pandas, OpenPyXL  
- **Server:** Local development server (`localhost:8080`)

---

### ᯓᡣ𐭩 Project Structure
```
├── README.md # Project documentation
├── images # For ReadMe Demo
├── app.py # Flask backend server
├── index.html # Frontend UI
└── sample_data # Synthetic data for user testing
    ├── master_file.xlsx # Upload in Step 1
    └── campaign_leads.xlsx # Upload in Step 2
```


---

### ᯓᡣ𐭩 Instructions 

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

#### Notes:
- Runs locally, no external storage. <br>
- For deployment, update API_BASE in index.html to your backend URL.<br>


#### License: 
This project is licensed under the MIT License.


Happy Converting! ⸜(｡˃ ᵕ ˂ )⸝♡
