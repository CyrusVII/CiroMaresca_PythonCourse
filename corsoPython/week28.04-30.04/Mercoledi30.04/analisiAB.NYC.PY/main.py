import CalcoloVifTakeData as cvt
import NycTree as nt
import pandas as pd

df,xF,y,cF,scaler= cvt.prepare_data()
model = nt.train_xgboost_model(df,xF,y,cF)
user_input = {
    'minimum_nights': 2,
    'number_of_reviews': 50,
    'reviews_per_month': 4,
    'calculated_host_listings_count': 1,
    'availability_365': 200
}
userInputDf = pd.DataFrame([user_input], columns= xF.columns.tolist())

predict = nt.predict_price(df,userInputDf,xF,scaler)
#print(f"Il prezzo predetto per il nuovo appartamento è: {predict}")