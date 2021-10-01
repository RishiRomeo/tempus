import joblib
import numpy as np
import pandas as pd

#Unpickle with joblib
with open('/model.joblib', 'rb') as pickle_file:
    model = joblib.load(pickle_file)

#Load clinical_text csv and change df['features'] type
df = pd.read_csv('/clinical_text.csv')
df['features']=df['features'].apply(eval).apply(np.array)


def main():
    '''
    Iterates thru the dataframe and runs the model's predict() fxn.
    Returns dataframe of sample_name and it's corresponding classification
    (i.e Neurology, Psychiatry, Radiology, etc.)

    params: none

    '''
    sample_name, classification = [] , []
    for index, row in df.iterrows():
        sample_name.append(row['sample_name'])
        classification.append(str(model.predict(row['features'].reshape(1,587)))[3:-2])
    out = pd.DataFrame(list(zip(sample_name, classification)),
               columns =['sample_name', 'model_classification'])
    print(out)


if __name__ == "__main__":
    main()
