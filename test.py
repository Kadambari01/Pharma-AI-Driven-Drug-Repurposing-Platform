import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from keras.utils.np_utils import to_categorical
from keras.layers import  MaxPooling2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D
from keras.models import Sequential, load_model, Model
import pickle
from keras.callbacks import ModelCheckpoint
import os
'''
drug = pd.read_csv("Dataset/Drug.csv", usecols=['DrugBank_ID', 'Formula'])
repurpose = pd.read_csv("Dataset/Literature.csv", encoding='cp1252', usecols=['DrugID', 'DrugName', 'Target', 'Disease', 'NewDisease'])

repurpose = repurpose.values

X = []
Y = []

for i in range(len(repurpose)):
    drug_id = repurpose[i,1]
    name = repurpose[i,0]
    target = repurpose[i,2]
    disease = repurpose[i,3]
    new_disease = repurpose[i,4]
    data = drug.loc[drug['DrugBank_ID'] == drug_id]    
    if len(data) > 0:
        data = data.values
        r = random.randint(10, 20)
        for k in range(0, r):
            X.append([drug_id, data[0,1], name, target, disease, new_disease])
        print(data)

data = pd.DataFrame(X, columns=['DrugID', 'Formula', 'DrugName', 'Target', 'Disease', 'NewDisease'])
data = shuffle(data, random_state=0)
data.to_csv("test.csv", index=False)
'''

dataset = pd.read_csv("test.csv")

label_encoder = []
columns = dataset.columns
types = dataset.dtypes.values
for j in range(len(types)):
    name = types[j]
    if name == 'object': #finding column with object type
        le = LabelEncoder()
        dataset[columns[j]] = pd.Series(le.fit_transform(dataset[columns[j]].astype(str)))#encode all str columns to numeric
        label_encoder.append([columns[j], le])
dataset.fillna(dataset.mean(), inplace = True)#replace missing values

Y = dataset['NewDisease'].ravel()
dataset.drop(['NewDisease'], axis = 1,inplace=True)
X = dataset.values

scaler = StandardScaler()
X = scaler.fit_transform(X)

indices = np.arange(X.shape[0])
np.random.shuffle(indices)
X = X[indices]
Y = Y[indices]
Y = to_categorical(Y)
X = np.reshape(X, (X.shape[0], X.shape[1], 1, 1))

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

cnn_model = Sequential()
cnn_model.add(Convolution2D(32, (1 , 1), input_shape = (X_train.shape[1], X_train.shape[2], X_train.shape[3]), activation = 'relu'))
cnn_model.add(MaxPooling2D(pool_size = (1, 1)))
cnn_model.add(Convolution2D(32, (1, 1), activation = 'relu'))
cnn_model.add(MaxPooling2D(pool_size = (1, 1)))
cnn_model.add(Flatten())
cnn_model.add(Dense(units = 256, activation = 'relu'))
cnn_model.add(Dense(units = y_train.shape[1], activation = 'softmax'))
cnn_model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
if os.path.exists("model/cnn_weights.hdf5") == False:
    model_check_point = ModelCheckpoint(filepath='model/cnn_weights.hdf5', verbose = 1, save_best_only = True)
    hist = cnn_model.fit(X_train, y_train, batch_size = 16, epochs = 280, validation_data=(X_test, y_test), callbacks=[model_check_point], verbose=1)
    f = open('model/cnn_history.pckl', 'wb')
    pickle.dump(hist.history, f)
    f.close()    
else:
    cnn_model.load_weights("model/cnn_weights.hdf5")

predict = cnn_model.predict(X_test)
predict = np.argmax(predict, axis=1)
y_test1 = np.argmax(y_test, axis=1)
acc = accuracy_score(y_test1, predict)
print(acc)

                   

