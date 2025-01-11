from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

train_dir = 'data/train'
val_dir = 'data/test'

train_datagen = ImageDataGenerator(
    rescale=1./255,
    width_shift_range= 0.1,
    height_shift_range= 0.1,
    zoom_range=0.1,
    )

val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size = (48,48),
    batch_size = 64,
    color_mode = "grayscale",
    class_mode = 'categorical'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size = (48,48),
    batch_size = 64,
    color_mode = "grayscale",
    class_mode = 'categorical'
)

# Learning Rate Scheduler: Dynamically reduces the learning rate
reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',  
    factor=0.5,          # Learning rate reduction factor
    patience=5,          # Number of epochs to wait before decreasing the learning rate
    min_lr=1e-6          # Minimum learning rate
)

emotion_model = Sequential()

emotion_model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape = (48,48,1)))
emotion_model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2,2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Conv2D(128, kernel_size=(3,3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2,2)))
emotion_model.add(Conv2D(128, kernel_size=(3,3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2,2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))

emotion_model.compile(loss='categorical_crossentropy',optimizer=Adam(learning_rate=0.0001, decay=1e-6),metrics=['accuracy'])

emotion_model_info = emotion_model.fit(
    train_generator,
    steps_per_epoch = 28709 // 64,
    epochs=100,
    validation_data = val_generator,
    validation_steps = 7178 // 64,
    callbacks=[reduce_lr]  
)

# Printing accuracy information during training
print("Training Accuracy:", emotion_model_info.history['accuracy'])
print("Validation Accuracy:", emotion_model_info.history['val_accuracy'])

# Average accuracy rates
mean_training_accuracy = sum(emotion_model_info.history['accuracy']) / len(emotion_model_info.history['accuracy'])
mean_validation_accuracy = sum(emotion_model_info.history['val_accuracy']) / len(emotion_model_info.history['val_accuracy'])

print(f"Ortalama Eğitim Doğruluğu: {mean_training_accuracy:.2f}")
print(f"Ortalama Doğrulama Doğruluğu: {mean_validation_accuracy:.2f}")

# Best epoch
best_epoch = emotion_model_info.history['val_accuracy'].index(max(emotion_model_info.history['val_accuracy'])) + 1
print(f"En iyi epoch: {best_epoch}. Epoch")

# Visualize training and validation accuracy
plt.plot(emotion_model_info.history['accuracy'], label='Training Accuracy')
plt.plot(emotion_model_info.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

emotion_model.save_weights('model.h5')