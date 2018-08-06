
# coding: utf-8

# # Python Challenge: PyPoll Analysis
# #### In this challenge, the task is to help a small, rural town modernize its vote-counting process. This python script analyzes the votes and calculates each of the following:
# * The total number of votes cast
# * A complete list of candidates who received votes
# * The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.

# In[10]:


import pandas as pd
import numpy as np
import os
import csv


# In[11]:


election_data = os.path.join("RawData","election_data_1.csv")


# In[12]:


election_data_pd = pd.read_csv(election_data, low_memory=False)
election_data_pd.head()


# In[13]:


#Calculate the total number of votes cast
votes_total = len(election_data_pd)
print(votes_total)


# In[14]:


#Extract a complete list of candidates who received votes
candidate_list = set(election_data_pd["Candidate"])
print (candidate_list)


# In[15]:


# Find the percentage of votes each candidate won
vote_percentage = election_data_pd.groupby(["Candidate"]).count()
del vote_percentage["County"]
vote_percentage['Percentage'] = ((100 * vote_percentage['Voter ID'] / vote_percentage['Voter ID'].sum()).astype(int)).astype(str)+ "%"
vote_percentage.rename(columns={'Voter ID': 'Voter Count'}, inplace=True)
print (vote_percentage)


# In[16]:


# Find the total number of votes each candidate won
election_data_pd.groupby(["Candidate"])["Voter ID"].count()


# In[17]:


# Determine the winner of the election based on popular vote
highest_count = (election_data_pd.groupby(["Candidate"])["Voter ID"].count()).max()
winner_info = vote_percentage[vote_percentage["Voter Count"].isin([highest_count])]
winner_name = list(winner_info.index.values)[0]
print(winner_name)


# In[18]:


# Display final analysis
print (f" Election Results \n ------------------------- \n Total Votes: {votes_total} \n ------------------------- \n ")
print (f" {vote_percentage} \n ------------------------- \n Winner: {winner_name} \n -------------------------")


# In[22]:


#Export results to a text file
file_to_output = "PyPoll_Analysis/election_analysis.txt"
with open(file_to_output, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {votes_total}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)
    
    # Print each candidate's voter count and percentage (to terminal)
    voter_output = f"{vote_percentage}\n"
    print(voter_output, end="")
    # Save each candidate's voter count and percentage to text file
    txt_file.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner_name}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

