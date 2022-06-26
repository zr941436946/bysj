import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
data = pd.read_csv('test_scores.csv')

for_corr = data.drop(['school','student_id','gender','classroom'], axis=1)

for_replace = {'school_setting':{'Urban':0, 'Suburban':1, 'Rural':2},
               'school_type':{'Public':0, 'Non-public':1},
               'teaching_method':{'Standard':0, 'Experimental':1},
               'lunch':{'Does not qualify':0, 'Qualifies for reduced/free lunch':1}}

corr = for_corr.replace(for_replace)


from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
X = corr.drop('posttest', axis=1)
y = corr['posttest'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
cat_model = CatBoostRegressor(loss_function='RMSE', verbose=50)

cat_model.fit(X_train, y_train,early_stopping_rounds=100,eval_set=[(X_test, y_test)])
import joblib
joblib.dump(cat_model,"model/test1.model")

pred = cat_model.predict(X_test)
print(mean_squared_error(pred, y_test))




