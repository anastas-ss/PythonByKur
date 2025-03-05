import struct
import sys

def read_bmp_hdr(data):
    sig = data[:2]
    if sig != b'BM':
        raise ValueError("Not a Windows BMP")

    size, = struct.unpack_from("<I", data, 2)

    return size

def read_dib_hdr(data):
    dib_size, = struct.unpack_from("<I", data, 14)
    
    if dib_size not in {12, 40, 52, 56, 108, 124}:
        raise ValueError("Incorrect header size")
    
    if dib_size != 12:
        w, h = struct.unpack_from("<ii", data, 18)
        _, bpp = struct.unpack_from("<HH", data, 26)
    else:
        w, h, _, bpp = struct.unpack_from("<HHHH", data, 18)

    comp, = struct.unpack_from("<I", data, 30)
   
    img_size, = struct.unpack_from("<I", data, 34)
    
    return dib_size, w, h, bpp, comp, img_size

def calc_img_size(w, h, bpp):
    r_size = (w * bpp + 31) // 32 * 4
    return r_size * abs(h)

try:
    data = sys.stdin.buffer.read()
    f_size = read_bmp_hdr(data)
    dib_size, w, h, bpp, comp, img_size = read_dib_hdr(data)

    c_img_size = calc_img_size(w, h, bpp)

    if not img_size:
        img_size = c_img_size

    elif img_size not in (c_img_size, c_img_size + 2):
        raise ValueError("Incorrect image size")

    if f_size != len(data):  
        raise ValueError("Incorrect size")

    print(w, abs(h), bpp, comp, 2 if img_size == c_img_size + 2 else 0)

except ValueError as e:
    print(e)