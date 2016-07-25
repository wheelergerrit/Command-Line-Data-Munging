import pandas as pd



url = #URL of dataset trying to munge



def load_data():

	df = pd.read_csv(url)

	col_names = [] #List of column names if csv does not include

	df.columns = col_names



if __name__ == "__main__":

	#This section of code calls the function load_data()

	load_data()

