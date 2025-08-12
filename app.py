from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import pandas as pd
from datetime import datetime, timedelta
import os
from werkzeug.utils import secure_filename
import json
import re

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Global variables to store uploaded data
master_data = None
campaign_data = None

DISTRIBUTORS = [
    "AGASTYA", "ARIHANT", "ARROW", "AVNET", "CHANGNAM", "DABO", 
    "ESOURCE", "FUTURE", "HANCOM", "IPT", "JINGCHUAN", "MACNICA", 
    "MILLENNIUM", "NEXTY", "RUTRONIK", "UNIQUEST", "WEIKENG", "WPG"
]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def normalize_column_names(df):
    """Normalize column names to handle different capitalizations"""
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def extract_first_word(text):
    """
    Extract the first word from a string, removing spaces, symbols, and punctuation.
    Returns lowercase version for case-insensitive comparison.
    """
    if pd.isna(text) or str(text).strip() == '':
        return ''
    
    # Convert to string and strip whitespace
    text_str = str(text).strip()
    
    # Use regex to find the first word (sequence of letters and numbers)
    # This ignores spaces, punctuation, and symbols
    match = re.search(r'[a-zA-Z0-9]+', text_str)
    
    if match:
        return match.group().lower()
    else:
        return ''

def parse_excel_file(file_path):
    """Parse Excel file and return DataFrame"""
    try:
        df = pd.read_excel(file_path)
        df = normalize_column_names(df)
        return df
    except Exception as e:
        raise Exception(f"Error parsing Excel file: {str(e)}")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/upload/master', methods=['POST'])
def upload_master():
    global master_data
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'master_' + filename)
        file.save(filepath)
        
        try:
            master_data = parse_excel_file(filepath)
            
            # Check for required columns
            required_columns = ['registration_id', 'main_distributor', 'registration_date', 'resale_customer', 'country_resale_customer']
            missing_columns = []
            
            for col in required_columns:
                if col not in master_data.columns:
                    # Try common variations
                    variations = [
                        col.replace('_', ' '),
                        col.replace('_', ''),
                        col.title().replace('_', ' '),
                        col.title().replace('_', ''),
                        'resale mc' if col == 'resale_customer' else col
                    ]
                    found = False
                    for var in variations:
                        if var.lower().replace(' ', '_') in master_data.columns:
                            # Rename the column to the expected name
                            old_col = [c for c in master_data.columns if c == var.lower().replace(' ', '_')][0]
                            master_data.rename(columns={old_col: col}, inplace=True)
                            found = True
                            break
                    if not found:
                        missing_columns.append(col)
            
            if missing_columns:
                return jsonify({
                    'error': f'Missing required columns: {missing_columns}',
                    'available_columns': list(master_data.columns)
                }), 400
            
            # Convert registration_date to datetime
            master_data['registration_date'] = pd.to_datetime(master_data['registration_date'], errors='coerce')
            
            return jsonify({
                'message': 'Master file uploaded successfully',
                'rows': len(master_data),
                'columns': list(master_data.columns)
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    return jsonify({'error': 'Invalid file format'}), 400

@app.route('/api/upload/campaign', methods=['POST'])
def upload_campaign():
    global campaign_data
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'campaign_' + filename)
        file.save(filepath)
        
        try:
            campaign_data = parse_excel_file(filepath)
            
            # Check for required columns
            required_columns = ['first_name', 'last_name', 'email', 'company']
            missing_columns = []
            
            for col in required_columns:
                if col not in campaign_data.columns:
                    # Try common variations
                    variations = [
                        col.replace('_', ' '),
                        col.replace('_', ''),
                        col.title().replace('_', ' '),
                        col.title().replace('_', '')
                    ]
                    found = False
                    for var in variations:
                        if var.lower().replace(' ', '_') in campaign_data.columns:
                            # Rename the column to the expected name
                            old_col = [c for c in campaign_data.columns if c == var.lower().replace(' ', '_')][0]
                            campaign_data.rename(columns={old_col: col}, inplace=True)
                            found = True
                            break
                    if not found:
                        missing_columns.append(col)
            
            if missing_columns:
                return jsonify({
                    'error': f'Missing required columns: {missing_columns}',
                    'available_columns': list(campaign_data.columns)
                }), 400
            
            return jsonify({
                'message': 'Campaign file uploaded successfully',
                'rows': len(campaign_data),
                'columns': list(campaign_data.columns)
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    
    return jsonify({'error': 'Invalid file format'}), 400

@app.route('/api/distributors', methods=['GET'])
def get_distributors():
    return jsonify({'distributors': DISTRIBUTORS})

@app.route('/api/query', methods=['POST'])
def query_data():
    global master_data, campaign_data
    
    if master_data is None:
        return jsonify({'error': 'Master file not uploaded'}), 400
    
    if campaign_data is None:
        return jsonify({'error': 'Campaign file not uploaded'}), 400
    
    try:
        data = request.get_json()
        start_date = datetime.strptime(data['startDate'], '%Y-%m-%d')
        query_period = data.get('queryPeriod', 180)  # Default to 180 days if not provided
        distributor = data['distributor']
        country = data['country']
        
        # Calculate end date based on selected period
        end_date = start_date + timedelta(days=query_period)
        
        # Filter master data
        filtered_master = master_data.copy()
        
        # Date filter
        filtered_master = filtered_master[
            (filtered_master['registration_date'] >= start_date) & 
            (filtered_master['registration_date'] <= end_date)
        ]
        
        # Distributor filter
        filtered_master = filtered_master[
            filtered_master['main_distributor'].str.upper() == distributor.upper()
        ]
        
        # Country filter
        filtered_master = filtered_master[
            filtered_master['country_resale_customer'].str.upper() == country.upper()
        ]
        
        # Prepare master results
        master_results = []
        for _, row in filtered_master.iterrows():
            master_results.append({
                'main_distributor': row['main_distributor'],
                'resale_customer': row['resale_customer'],
                'registration_id': row['registration_id'],
                'registration_date': row['registration_date'].strftime('%Y-%m-%d') if pd.notna(row['registration_date']) else 'N/A'
            })
        
        # Prepare campaign results
        campaign_results = []
        for _, row in campaign_data.iterrows():
            campaign_results.append({
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'company': row['company']
            })
        
        # Find matches between first word of resale_customer and company
        matches = []
        matched_campaign_leads = set()
        for _, master_row in filtered_master.iterrows():
            resale_first_word = extract_first_word(master_row['resale_customer'])
            
            # Skip if no valid first word found
            if not resale_first_word:
                continue
                
            
            for _, campaign_row in campaign_data.iterrows():
                company_first_word = extract_first_word(campaign_row['company'])
                
                # Skip if no valid first word found
                if not company_first_word:
                    continue
                
                # Check if first words match (case-insensitive)
                if resale_first_word == company_first_word:

                    lead_key = f"{campaign_row['first_name']}|{campaign_row['last_name']}|{campaign_row['company']}"
                    matched_campaign_leads.add(lead_key)

                    matches.append({
                        'first_name': campaign_row['first_name'],
                        'last_name': campaign_row['last_name'],
                        'email': campaign_row['email'],
                        'company': campaign_row['company'],
                        'resale_customer': master_row['resale_customer'],
                        'registration_id': master_row['registration_id'],
                        'registration_date': master_row['registration_date'].strftime('%Y-%m-%d') if pd.notna(master_row['registration_date']) else 'N/A',
                        'main_distributor': master_row['main_distributor'],
                        'matched_word': resale_first_word  # For debugging purposes
                    })
        
        return jsonify({
            'query_params': {
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d'),
                'query_period': query_period,
                'distributor': distributor,
                'country': country
            },
            'master_results': master_results,
            'campaign_results': campaign_results,
            'matches': matches,
            'summary': {
                'opportunities_found': len(master_results),
                'matched_campaign_leads': len(matched_campaign_leads),
                'campaign_leads': len(campaign_results),
                'matches_found': len(matches)
            }
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        'master_file_uploaded': master_data is not None,
        'campaign_file_uploaded': campaign_data is not None,
        'master_rows': len(master_data) if master_data is not None else 0,
        'campaign_rows': len(campaign_data) if campaign_data is not None else 0
    })

if __name__ == '__main__':
    print("Starting Campaign Conversion Checker...")
    print("Access the application at: http://localhost:8080")
    app.run(debug=True, host='0.0.0.0', port=8080)