# Impoorting required python packages
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd

# Importing dataset
my_df= pd.read_csv("video_game_data.csv")

# Splitting data into Input and output objects
X = my_df.drop(["completion_time"], axis = 1)
y = my_df["completion_time"]

# Splitting data into Training and testing sets
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=42)

# Initiating the model object
regressor= RandomForestRegressor(random_state=42)

# Model Training 
regressor.fit(X_train, y_train)

# Assessing the accuracy of the Random Forest model
y_pred= regressor.predict(X_test)
comparison_of_predictions= pd.DataFrame({"actual": y_test, "prediction": y_pred})

r2_score(y_test, y_pred)