
def mean_temperature(data):
    """
    Get the mean temperature
    
    Args:
        data (pandas.Dataframe): A pandas dataframe with air temperature measurements
        
    Returns:
                The mean air temperature (float)
    """
    temperatures = data['Air temperature (degC)']
    return sum(temperatures)/len(temperatures)
