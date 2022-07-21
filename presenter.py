import pandas as pd

df = pd.read_csv('list.csv')

rslt_df = df[df['Presented'] == "no"] 
if len(rslt_df.index) > 0:

    # Using the sample function from pandas to randomly select a student! https://www.w3schools.com/python/pandas/ref_df_sample.asp
    selected = rslt_df['Student'].sample() 
    print("========================================")
    print("========================================")
    print("========================================")
    print("========================================")
    print("========================================")
    print("Congratulations, " + selected.to_string(index=False) + "! You have been selected to present next!!")
    #print(selected.index[0])
    print("========================================")
    question = input("Do you wish to remove " + selected.to_string(index=False) + " from the list of presenters? y/n: ")
    if question == "y":
        print (selected.to_string(index=False) + " is removed from the list of presenters!")
        df.at[selected.index[0],'Presented'] ='yes'
        df.to_csv('list.csv', index=False)
    else:
        print(selected.to_string(index=False) + " was NOT removed from the list of presenters! Seeya...")
        raise SystemExit
else:
    print("Everyone has already presented!!!!")
    
