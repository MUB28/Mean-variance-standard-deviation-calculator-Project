import numpy as np

def calculate(list):


    
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        data = np.array(list)

        mean_row = data.reshape(3,3).mean(axis = 0).tolist()
        mean_column = data.reshape(3,3).mean(axis = 1).tolist()
        mean_of_all_elements = data.reshape(3,3).mean().tolist()

        variance_row = data.reshape(3,3).var(axis = 0).tolist()
        variance_column = data.reshape(3,3).var(axis = 1).tolist()
        variance_of_all_elements = data.reshape(3,3).var().tolist()

        std_row = data.reshape(3,3).std(axis = 0).tolist()
        std_column = data.reshape(3,3).std(axis = 1).tolist()
        std_of_all_elements = data.reshape(3,3).std().tolist()

        max_row = data.reshape(3,3).max(axis = 0).tolist()
        max_column = data.reshape(3,3).max(axis = 1).tolist()
        max_of_all_elements = data.reshape(3,3).max().tolist()

        min_row = data.reshape(3,3).min(axis = 0).tolist()
        min_column = data.reshape(3,3).min(axis = 1).tolist()
        min_of_all_elements = data.reshape(3,3).min().tolist()

        sum_row = data.reshape(3,3).sum(axis = 0).tolist()
        sum_column = data.reshape(3,3).sum(axis = 1).tolist()
        sum_of_all_elements = data.reshape(3,3).sum().tolist()
        
        return(

        { 'mean': [mean_row, mean_column, mean_of_all_elements],
          'variance': [variance_row, variance_column, variance_of_all_elements],
          'standard deviation': [std_row, std_column, std_of_all_elements], 
          'max': [max_row, max_column, max_of_all_elements],
          'min': [min_row, min_column, min_of_all_elements],
          'sum':  [sum_row, sum_column, sum_of_all_elements]

        }  
        
        )



    