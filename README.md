#sports_gambling_line_predictor
This project calls an api to past and current betting odds from multiple different odds makers. It will use this data to train a model to make gambling lines of its own. It will compare its line with current lines from different odds makers to find calculated expected values for bets. A positive expected value would mean the bet has favorable odds.

Notes: 
This project is written in Python and utilizes the fast ai packages to train the model. A possible api to retrieve data is The odds api:
    https://the-odds-api.com/liveapi/guides/v4/#overview 
    https://the-odds-api.com/historical-odds-data/#how-to-access-historical-odds-data

    - Notes on Model Prediction
        - Predict moneyline and/or spread?
        - Possible features:
            - Record over previous 3 years
            - Home or away
            - historical odds
            - power ranking?

        - Possible Model for Sports Line Prediction:
            - Linear Regression 
            - Random Forrest
