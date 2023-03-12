import numpy as np
from keras.models import Model
from keras.layers import Dense
from keras.layers import Input
from keras.layers import Dropout
from keras.layers import Activation
from keras.metrics import MeanSquaredError
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow.saved_model import save
from q_table import q_table_generator
from utils import table_to_numbers

D_table, Q_control = q_table_generator(500)

X = []
y = []
for key in D_table.keys():
    if Q_control[key]:
        X.append(key)
        y.append(D_table[key])
        
        
for k in range(len(X)):
    
    X[k] = table_to_numbers(X[k])

y = np.asarray(y)
X = np.asarray(X)

def Q_agent():
    
    inputs = Input(shape=(9,))

    # Dodawanie warstw gęstych z funkcją aktywacji ReLU oraz dropout
    x = Dense(16)(inputs)
    x = Activation('relu')(x)
    x = Dropout(0.2)(x)
    
    x = Dense(8)(x)
    x = Activation('relu')(x)
    x = Dropout(0.2)(x)
    
    x = Dense(4)(x)
    x = Activation('relu')(x)
    x = Dropout(0.2)(x)
    
    x = Dense(1)(x)
    outputs = Activation('tanh')(x)

    model = Model(inputs=inputs, outputs=outputs)
    
    return model

policy = Q_agent()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25,
                                                    random_state=42)

policy.compile(loss='mean_squared_error', optimizer='adam',
               metrics=[MeanSquaredError()])

history = policy.fit(X_train, y_train, epochs=1000, batch_size=32, verbose=1,
                     validation_data=(X_test, y_test))

plt.plot(history.history['loss'], label='Train')
plt.plot(history.history['val_loss'], label='Validation')
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()
plt.show()

policy.save('q_policy.h5')
