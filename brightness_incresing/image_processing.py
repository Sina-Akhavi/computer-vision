import cv2
import numpy as np

path = "./paradise.jpeg"
path2 = "./channels_separation/geeks_for_geeks.jpg"
paradise_img = cv2.imread(path)
# print(f'shape of {path}: ', paradise_img.shape)
# print(paradise_img)

def make_black(image_path, fraction, direction='UP'):
    
    img = cv2.imread(image_path)
    rows = paradise_img.shape[0]

    start = 0
    end = rows

    if direction == 'DOWN':
        start = int ((1 - fraction) *  rows)
    elif direction == 'UP':
        end = int (fraction *  rows)    
    else:
        raise ValueError("Invalid Direction {}".format(direction))

    specific_part = img[start:end, :, :]
    specific_part[:] = 0

    return img

def show_image(img_obj):
    cv2.imshow("Title", img_obj)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def increase_brightness_hsv(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite("./brighter_img.jpeg", img)

def increase_brightness_rgb(img, value=30):
    b, g, r = cv2.split(img)

    limit = 255 - value
    b[b <= limit] += value
    b[b > limit] = 255

    g[g <= limit] += value
    g[g > limit] = 255

    r[r <= limit] += value
    r[r > limit] = 255

    rgb_img = cv2.merge([b, g, r])
    cv2.imwrite("./brighter_bgr_img.jpeg", rgb_img)

def separate_channels(path):
    img = cv2.imread(path)

    b, g, r = cv2.split(img)
    
    b_status = cv2.imwrite("./channels_separation/b_channel.jpeg" ,b)
    g_status = cv2.imwrite("./channels_separation/g_channel.jpeg" ,g)
    r_status = cv2.imwrite("./channels_separation/r_channel.jpeg" ,r)

    print("b status={}, g status={}, r status={}".format(g_status, b_status, r_status))
    

# ------------------- make one fourth black -------------------
# fraction = 1 / 4
# blackened_img = make_black(path, fraction, direction='LEFT')
# show_image(blackened_img)


# ------------------- increase brightness testcase 1 -------------------
# increase_brightness_value = 30
# img_obj = cv2.imread(path)
# increase_brightness_hsv(img_obj, increase_brightness_value)

# ------------------- increase brightness testcase 2 -------------------
# increase_brightness_value = 30
# img_obj = cv2.imread(path)
# increase_brightness_rgb(img_obj, increase_brightness_value)

# ------------------- separate channels testcase 1 -------------------
separate_channels(path2)



# --------------------------- test ---------------------------
# array = np.array([[1, 4, 6],
#                   [5, 8, 6],
#                   [3, 5, 7]])

# part_array = array[2:, :]
# part_array[:] = -1
# print("part_array =\n", part_array)
# print("array =\n", array + 10)

# --------------------------- test ---------------------------

# array = np.empty((2, 3, 3))
# array[:] = 0

# print(array)
