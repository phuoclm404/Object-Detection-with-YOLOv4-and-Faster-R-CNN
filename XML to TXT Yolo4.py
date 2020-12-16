import xml.etree.ElementTree as ET
# thứ tự của list là id của class 
# các tên bên dưới là các class mà ta muốn train, phải tồn tại với lable trong XML
classes = ["pedestrian", "car", "van", "bus", "truck","motor", "bicycle","tricycle"]
# cách chuyển đổi từ tọa độ XML sang tọa độ Yolo
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)
def convert_annotation(image_id):
    in_file = open('C:/Users/Azex/Desktop/Demo ML/YoloV4/UIT-VD/Test/%s.xml' % (image_id))    # đường dẫn file xml
    out_file = open('C:/Users/Azex/Desktop/Demo ML/YoloV4/UIT-VD/Test/%s.txt' % (image_id), 'w')    # đường dẫn file txt xuất ra 
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:    # tên class tìm thấy trong file xml nhưng ta muốn bỏ qua nó
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
image_ids_train = open('C:/Users/Azex/Desktop/Demo ML/YoloV4/test.txt').read().strip().split()    # đọc tên của file xml
for i in range(len(image_ids_train)):
    image_ids_train[i]=image_ids_train[i].strip("UIT-VD/Test\.jpg") # strip được sử dụng để loại bỏ các 
    convert_annotation(image_ids_train[i])                          # thành phần dư thừa chỉ dữ lại tên ảnh
    

