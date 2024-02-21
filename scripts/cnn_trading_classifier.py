from keras.models import Sequential
from keras.layers import Conv1D, BatchNormalization, MaxPooling1D, LSTM, Bidirectional, Dropout, Dense
from keras.optimizers import Adam
from keras.regularizers import l1_l2

def rede_cnnTrading(params):
    model = Sequential()
    model.add(Conv1D(filters=int(params['filters']), kernel_size=int(params['kernel_size']), activation=params['activation'], 
                     padding='same', kernel_initializer=params['kernel_initializer'], input_shape=(15, 1)))
    model.add(BatchNormalization())
    model.add(MaxPooling1D(pool_size=int(params['pool_size'])))
    model.add(Conv1D(filters=int(params['filters'] * 2), kernel_size=int(params['kernel_size']), activation=params['activation'], padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling1D(pool_size=int(params['pool_size'])))
    model.add(Conv1D(filters=int(params['filters']), kernel_size=int(params['kernel_size']), activation=params['activation'], padding='same'))
    model.add(BatchNormalization())
    model.add(MaxPooling1D(pool_size=int(params['pool_size'])))
    model.add(Bidirectional(LSTM(units=int(params['lstm_units']), return_sequences=True)))
    model.add(Dropout(params['dropout_rate']))
    model.add(Bidirectional(LSTM(units=int(params['lstm_units']))))
    model.add(Dropout(params['dropout_rate']))
    model.add(Dense(units=1, activation='tanh', kernel_initializer=params['kernel_initializer'], 
                    kernel_regularizer=l1_l2(l1=params['l1'], l2=params['l2'])))

    model.compile(optimizer=Adam(learning_rate=1e-4), loss=params['loss'], metrics=['accuracy'])
    return model