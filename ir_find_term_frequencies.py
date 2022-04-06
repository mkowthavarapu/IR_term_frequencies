import pandas as pd

def load_data_set(file_name):
    csv_data = pd.read_csv(file_name)
    pd_data_frame = pd.DataFrame({ 'terms':csv_data.Terms, 'd1':csv_data.doc1,'d2':csv_data.doc2,'d3':csv_data.doc3,'d4':csv_data.doc4,'d5':csv_data.doc5})
    # pd_data_frame.index = ['a','b','c','d','e','f','g','h','i']
    print(pd_data_frame,'\n')
    return pd_data_frame

def task_1(data_frame):
    """List terms that have frequencies of 4 or more in doc1
    """
    print(data_frame[data_frame.d5>=3][["terms", "d5"]], '\n')

def task_2(data_frame):
    """Find terms that contain letter 'a' in doc3
    """
    print(data_frame[data_frame.terms.str.contains("a")][data_frame.d3!=0][["terms", "d3"]], '\n')

def task_3(data_frame):
    """Find terms that start with letter 's' in doc5
    """
    print(data_frame[data_frame.terms.str.startswith("a")][data_frame.d5!=0][["terms", "d5"]], '\n')

def task_4(data_frame):
    """List all term frequencies of doc3, but not the ones for team
    """
    print(data_frame[data_frame.terms != "team"][['terms', 'd3']], '\n')

def task_5(data_frame):
    """Find the terms with the highest and lowest term frequencies in docs 2 and 4
    """
    print(data_frame[
        data_frame.d2.isin([data_frame.d2.min(), data_frame.d2.max()])
        |
        data_frame.d4.isin([data_frame.d4.min(), data_frame.d4.max()])
        ][["terms", "d2", "d4"]], '\n'
    )

def task_6(data_frame):
    """Find terms that not included in docs that have the label classification
    """
    print(data_frame[(data_frame['d1']==0) & (data_frame["d1"].iloc[8] == 1) | (data_frame['d2']==0) & (data_frame["d2"].iloc[8] == 1) | (data_frame['d3']==0) & (data_frame["d3"].iloc[8] == 1) | (data_frame['d4']==0) & (data_frame["d4"].iloc[8] == 1) | (data_frame['d5']==0) & (data_frame["d5"].iloc[8] == 1)
    ])


def main():
    data_frame = load_data_set("doc_term_frequency.csv")
    task_1(data_frame)
    task_2(data_frame)
    task_3(data_frame)
    task_4(data_frame)
    task_5(data_frame)
    task_6(data_frame)

if __name__ == "__main__":
    main()