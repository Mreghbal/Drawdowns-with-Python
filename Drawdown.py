import pandas as pd
def drawdown(return_series, initial_wealth):
    '''
    Inputs

    1- Return series, it can be a CSV file during the years and months

    2- Initial wealth that you can know how much the returns in your stocks, coins, ...

    Outputs

    1- A data frame with four variables that store in the function

    ##### You can write other outputs too using the data frame #####

    ##### Maybe you will need NumPy to import for producing new outputs #####

    2- Plot the data frame and compare the variables

    3- Plot the variables separately or with a selection

    4- Finding the maximum, minimum, and other parameters of the variables
    5 - ... 
    '''
    initial_wealth = 1000    # You can change it with any amount you want
    wealth_index = initial_wealth * (1 + return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = wealth_index - previous_peaks
    drawdowns_percentage = (wealth_index - previous_peaks) / previous_peaks
    result = pd.DataFrame({
    "Wealth": wealth_index,
    "Peaks" : previous_peaks,
    "Drawdowns": drawdowns,
    "Drawdowns %": drawdowns_percentage
    })
    return result