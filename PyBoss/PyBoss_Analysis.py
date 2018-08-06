
# coding: utf-8

# In[32]:


import pandas as pd
import datetime
import csv
import os


# In[2]:


employee_data = csvpath = os.path.join("RawData", "employee_data1.csv")


# In[3]:


employee_data_pd = pd.read_csv(employee_data, low_memory = False)
employee_data_pd.head()


# In[4]:


# Checkout the data types
employee_data_pd.info()


# In[5]:


# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}


# In[6]:


# Placeholders for lists of each column of data
emp_ids = employee_data_pd['Emp ID'].tolist()
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []


# In[7]:


#The Name column should be split into separate First Name and Last Name columns
split_name = employee_data_pd['Name'].str.split(' ', expand=True)
emp_first_names = split_name[0].tolist()
emp_last_names = split_name[1].tolist()
emp_last_names[0]


# In[8]:


#The DOB data should be re-written into DD/MM/YYYY format
employee_data_pd['DOB'] = pd.to_datetime(employee_data_pd.DOB)
emp_dobs = employee_data_pd['DOB'].dt.strftime('%d/%m/%Y').tolist()
emp_dobs[0]


# In[20]:


#The SSN data should be re-written such that the first five numbers are hidden from view.
split_ssn = employee_data_pd['SSN'].tolist()
for item in split_ssn:
    item = item.replace(item[0:6],'***-**')
    emp_ssns.append(item)

emp_ssns[0]


# In[25]:


#The State data should be re-written as simple two-letter abbreviations
states = employee_data_pd['State'].tolist()
for s in states:
    abbrev = us_state_abbrev[s]
    emp_states.append(abbrev)
    
emp_states[0]


# In[29]:


# Zip the lists together
empdb = zip(emp_ids, emp_first_names, emp_last_names,
            emp_dobs, emp_ssns, emp_states)


# In[33]:


#Export the data to a textfile
with open("PyBoss_Analysis/employee_data_reformatted2.csv", "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(empdb)

