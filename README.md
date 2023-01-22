# sports_gambling_line_predictor
This project calls an api to retirve past and current betting odds from multiple different odds makers. It will use this data to train a model to predict gambling lines of its own. It will compare the lines it predicted with current lines from different odds makers to calculate expected values for bets. A positive expected value would mean the bet has favorable odds.

## Notes: 
This project is written in Python and utilizes the fast ai packages to train the model. 
###### API Notes
- [The odds api](https://the-odds-api.com/liveapi/guides/v4/#overview) 
- [Historical Api data](https://the-odds-api.com/historical-odds-data/#how-to-access-historical-odds-data)

###### Notes on Model Prediction
- Predict moneyline and/or spread?
- Possible features:
1. Record over previous 3 years
2. Home or away (0 or 1)
3. historical odds
4. power ranking?

###### Possible Model for Sports Line Prediction:
- Linear Regression 
- Random Forrest
