import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 기본 경로
base_dir = ''

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

# 훈련에 사용되는 type0/type1 이미지 경로
train_type0_dir = os.path.join(train_dir, 'type0')
train_type1_dir = os.path.join(train_dir, 'type1')
print(train_type0_dir)
print(train_type1_dir)

# 테스트에 사용되는 type0/type1 이미지 경로
validation_type0_dir = os.path.join(validation_dir, 'type0')
validation_type1_dir = os.path.join(validation_dir, 'type1')
print(validation_type0_dir)
print(validation_type1_dir)

train_type0_fnames = os.listdir(train_type0_dir)
train_type1_fnames = os.listdir(train_type1_dir)

print(train_type0_fnames[:5])
print(train_type1_fnames[:5])

print('Total training type0 images :', len(os.listdir(train_type0_dir)))
print('Total training type1 images :', len(os.listdir(train_type1_dir)))

print('Total validation type0 images :', len(os.listdir(validation_type0_dir)))
print('Total validation type1 images :', len(os.listdir(validation_type1_dir)))

nrows, ncols = 4, 4
pic_index = 0

fig = plt.gcf()
fig.set_size_inches(ncols*3, nrows*3)

pic_index += 8

next_type0_pix = [os.path.join(train_type0_dir, fname)
for fname in train_type0_fnames[pic_index-8:pic_index]]

next_type1_pix = [os.path.join(train_type1_dir, fname)
for fname in train_type1_fnames[pic_index-8:pic_index]]

for i, img_path in enumerate(next_type0_pix+next_type1_pix):
    sp = plt.subplot(nrows, ncols, i + 1)
sp.axis('Off')

img = mpimg.imread(img_path)
plt.imshow(img)

plt.show()

model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(640, 480, 3)),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
  tf.keras.layers.MaxPooling2D(2, 2),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

model.summary()

model.compile(optimizer=RMSprop(lr=0.001),
            loss='binary_crossentropy',
            metrics = ['accuracy'])

train_datagen = ImageDataGenerator(rescale=1.0/255.)
test_datagen = ImageDataGenerator(rescale=1.0/255.)

train_generator = train_datagen.flow_from_directory(train_dir,
                                                    batch_size=20,
                                                    class_mode='binary',
                                                    target_size=(640, 480))
validation_generator = test_datagen.flow_from_directory(validation_dir,
                                                        batch_size=20,
                                                        class_mode='binary',
                                                        target_size=(640, 480))

history = model.fit(train_generator,
                    validation_data=validation_generator,
                    steps_per_epoch=100,
                    epochs=100,
                    validation_steps=50,
                    verbose=2)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'go', label='Training Loss')
plt.plot(epochs, val_loss, 'g', label='Validation Loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()