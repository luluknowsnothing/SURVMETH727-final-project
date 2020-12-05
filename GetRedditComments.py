# load libraries
import pandas as pd
import datetime as dt
from psaw import PushshiftAPI
import os
import random

# working directory: using google colab

# set API
api = PushshiftAPI()

# Set beging and end date of period interested in
# from the beginning of the year to right before the election
start_epoch_2020=int(dt.datetime(2020, 1, 1).timestamp())
end_epoch_2020=int(dt.datetime(2020, 11, 2).timestamp())

# set the keywords to search for
keys = ['china', 'chinese', 'ccp', 'wuhan']
for key in keys:
  # create empty lists
  comment_list = []
  # Fill lists with data from API
  # Here: search comments made to subreddit AskTrumpSupporters 
  # which contain the key words listed above
  comment_list = list(api.search_comments(q=key,
                              before=end_epoch_2020,
                              after=start_epoch_2020,               
                              subreddit='AskTrumpSupporters'))

  # Save as data frame
  all_comments_df =pd.DataFrame([s.d_ for s in comment_list])
  # check the running process by printing the number of comments found
  print(len(all_comments_df))
  # save comments as csv
  df = all_comments_df.copy(deep=True)
  # remove the line space of comments body to avoid error
  for index in range(len(all_comments_df)):
      line = str(all_comments_df.iloc[index]['body']).replace('\n', '')
      df.loc[df.index == index, 'body'] = line
      df.to_csv(f'comments_{key}.csv')

#----------------------------------------------------------------------------#
# control comments
# random comments from the subreddit over the required period
def rand_date(start,end):
    # start and end are timestamps
  	# get a random timestamp
  	return int((start + (end - start)*random.random()))

# scrap random comments during 1000 random hours on the subreddit over the epoch
control_list = []
control_list = list(api.search_comments(
                              after= rand_date(end_epoch_2020,start_epoch_2020)
                              before= after + 3600               
                              subreddit='AskTrumpSupporters'))
# save as a data frame
control_comments_df = pd.DataFrame([s.d_ for s in comment_list])

for i in range(999):
  control_list = []  
  control_list = list(api.search_comments(
                              after= rand_date(end_epoch_2020,start_epoch_2020)
                              before= after + 3600               
                              subreddit='AskTrumpSupporters'))
  # save as a data frame
  temp = pd.DataFrame([s.d_ for s in comment_list])
  control_comments_df = control_comments.append(temp, ignore_index=True)

# save as csv
df = control_comments_df.copy(deep=True)
# remove the line space of comments body to avoid error
line = str(control_comments_df.iloc[index]['body']).replace('\n', '')
df.loc[df.index == index, 'body'] = line
df.to_csv(f'control_comments.csv')


  