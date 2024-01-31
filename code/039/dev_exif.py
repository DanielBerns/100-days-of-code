from PIL import Image
from PIL import ExifTags

import glob
import math

# https://pillow.readthedocs.io/en/stable/_modules/PIL/ExifTags.html

def get_info(fn):
    image = Image.open(fn)    
    info = image.getexif()
    exif = {}
    for tag, value in info.items():
        decoded = ExifTags.TAGS.get(tag, tag)
        exif[decoded] = value
    gps_ifd = info.get_ifd(ExifTags.IFD.GPSInfo)
    gps = {}
    for tag, value in gps_ifd.items():
        decoded = ExifTags.GPSTAGS.get(tag, tag)
        gps[decoded] = value
    return exif, gps


def gps_to_dms(value):
    d_, m_, s_ = value
    return (int(d_), # d
            int(m_), # m
            float(s_) # s
        )


def dms_to_seconds(dms):
    d_, m_, s_ = dms
    return float((d_ * 60 + m_) * 60) + s_


def seconds_to_dec(seconds):
    d_ = int(seconds) // 3600
    r_ = (seconds - d_ * 3600) / 3600
    return d_ + r_

def seconds_to_dms(seconds):
    r_ = seconds - math.floor(seconds)
    q_ = int(seconds - r_)
    s_ = q_ % 60
    q_ = q_ / 60
    m_ = q_ % 60
    q_ = q_ / 60
    d_ = q_ 
    return (d_, m_, float(s_) + r_)


def get_span(a, b):
    a_s = dms_to_seconds(a)
    b_s = dms_to_seconds(b)
    span = (a_s - b_s)
    return seconds_to_dms(span)


def get_center(a_, b_):
    print(a_)
    print(b_)
    a_s = dms_to_seconds(a_)
    b_s = dms_to_seconds(b_)
    center = (a_s + b_s) / 2.0
    dms = seconds_to_dms(center)
    return dms


def get_photos(mask):
    photos = dict()
    for current in glob.iglob(mask):
        exif, gps_ifd = get_info(current)
        photos[current] = (exif, gps_ifd)
    return photos


def get_lat_long(gps):
    lat, lat_ref = gps['GPSLatitude'], gps['GPSLatitudeRef']
    lng, lng_ref = gps['GPSLongitude'], gps['GPSLongitudeRef']
    lat_d, lat_m, lat_s = gps_to_dms(lat)
    lng_d, lng_m, lng_s = gps_to_dms(lng)
    lat_seconds = dms_to_seconds((lat_d, lat_m, lat_s))
    lng_seconds = dms_to_seconds((lng_d, lng_m, lng_s)) 
    lat_dec = seconds_to_dec(lat_seconds)
    lng_dec = seconds_to_dec(lng_seconds)  
    return -lat_dec, -lng_dec

def get_code(i, lat, lng):
    return f"var marker_{i:d} = L.marker([{lat:f}, {lng:f}]).addTo(map);\n"
    
if __name__ == '__main__':
    source_mask = '/home/dberns/Data/fce_cr/crd-1/*.jpg'
    target_txt = '/home/dberns/Data/fce_cr/target.txt'
    photos = get_photos(source_mask)
    with open(target_txt, 'w') as target:
        for i, item in enumerate(photos.items()):
            key, (exif, gps) = item
            print(i, ' ', key)
            print('    exif')
            for k, v in exif.items():
                print(f"      {k:s}:{str(v):s}")
            print('    gps')
            for k, v in gps.items():
                print(f"      {k:s}:{str(v):s}")
            if gps:
                print( '    gps lat, lng')
                lat, lng = get_lat_long(gps)
                print(f'        lat: {lat:f} | lng {lng:f}')
                code = get_code(i, lat, lng)
                target.write(code)
