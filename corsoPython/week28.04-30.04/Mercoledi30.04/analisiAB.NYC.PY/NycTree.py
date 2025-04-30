import xgboost as xgb
from sklearn.preprocessing import StandardScaler

def train_xgboost_model(df_selected, X_selected, y, categorical_features):
    
    # 1. Prendi tutte le feature (sia numeriche che categoriche)
    X_all = df_selected[X_selected.columns.tolist() + categorical_features]
    
    # 2. Crea il DMatrix
    dtrain = xgb.DMatrix(X_all, label=y, enable_categorical=True)

    # 3. Parametri del modello XGBoost
    params = {
        'objective': 'reg:squarederror',  # Regressione per prezzo
        'tree_method': 'hist',  # Utilizza l'algoritmo 'hist' per l'efficienza
        'eval_metric': 'rmse',  # Root Mean Squared Error
        'enable_categorical': True,  # Abilita il supporto per feature categoriali
    }

    # 4. Addestra il modello
    model = xgb.train(params, dtrain, num_boost_round=100)
    
    return model
  
def predict_price(model,user_input,X_selected,scaler):
  # Standardizza le feature numeriche in base al modello
  user_input_scaled = scaler.transform([user_input[X_selected.columns.tolist()]])

  # Crea DMatrix per XGBoost
  dinput = xgb.DMatrix(user_input_scaled, enable_categorical=True)

  # Predici il prezzo
  predicted_price = model.predict(dinput)

  return predicted_price[0]