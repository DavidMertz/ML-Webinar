#!/usr/bin/env python
from os.path import join
import pandas as pd

# Read the data
fname = join('..', 'data', "Learning about Humans learning ML.csv")
humans = pd.read_csv(fname)

# Drop unused column
humans.drop('Timestamp', axis=1, inplace=True)

# Add an improved column
humans['Education'] = (humans[
    'Years of post-secondary education (e.g. BA=4; Ph.D.=10)']
                       .str.replace(r'.*=','')
                       .astype(int))

# Then drop the one it is based on
humans.drop('Years of post-secondary education (e.g. BA=4; Ph.D.=10)', 
            axis=1, inplace=True)

# Simplify the column names
humans.columns = ['Fav_lang', 'Fav_movie', 'Experience', 'Sklearn', 
                  'Age', 'Humans_Machines', 'Fav_Game', 'Success', 'Education']

# Get the dummies
human_dummies = pd.get_dummies(humans)

# Replicate the data 50 times
more_dummies = pd.concat([human_dummies]*50)
more_dummies.index = range(len(more_dummies))

# Bias the mild positive predictor movie=something different
samp = more_dummies.sample(frac=0.75)
ndx = samp[samp['Fav_movie_And Now for Something Completely Different']==1].index
more_dummies.loc[ndx, 'Success'] = 11

# Bias the mild negative predictor move=holy grail
samp = more_dummies.sample(frac=0.75)
ndx = samp[samp['Fav_movie_Monty Python and the Holy Grail']==1].index
more_dummies.loc[ndx, 'Success'] = -1

# Bias the mild negative predictor age>38
samp = more_dummies.sample(frac=0.75)
ndx = samp[samp['Age']> 38].index
more_dummies.loc[ndx, 'Success'] = -2

# Bias the mild positive predictor game=chass
samp = more_dummies.sample(frac=0.75)
ndx = samp[samp['Fav_Game_Chess']==1].index
more_dummies.loc[ndx, 'Success'] = 12

# Boolean at cutoff value
more_dummies['Success'] = more_dummies.Success >= 8

# Write the data
out = join('..', 'data', "FakeLearning.csv")
more_dummies.to_csv(out)


