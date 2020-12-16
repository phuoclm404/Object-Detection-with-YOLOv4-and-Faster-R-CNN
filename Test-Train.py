import glob2
import os
files_test = []
files_train = []
for ext in ["*.png", "*.jpeg", "*.jpg"]:
  image_files = glob2.glob(os.path.join("UIT-VD/Test/", ext))
  files_test += image_files
for ext in ["*.png", "*.jpeg", "*.jpg"]:
  image_files = glob2.glob(os.path.join("UIT-VD/Train/", ext))
  files_train += image_files

# Tạo file test.txt
with open("test.txt", "w") as f:
  for idx in files_test:
      f.write(idx+'\n')
 
# Tạo file train.txt
with open("train.txt", "w") as f:
  for idx in files_train:
      f.write(idx+'\n')