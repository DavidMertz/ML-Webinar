#!/usr/bin/env python
np.random.seed(1)
theta = np.random.random(1000) * tau
r = np.random.random(1000)
feat1 = np.sin(theta) * r
feat2 = np.cos(theta) * r
z = feat1 * feat2       
silly_df = pd.DataFrame({"feature_1": feat1, 
                         "feature_2": feat2, 
                         "TARGET": z })
silly_df.to_csv('../data/linear_failure.csv')