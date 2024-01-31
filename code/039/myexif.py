from PIL import Image
from PIL import ExifTags

import glob
import math

# https://pillow.readthedocs.io/en/stable/_modules/PIL/ExifTags.html

def get_exif(fn):
    exif_table = {}
    image = Image.open(fn)
    # info = image.getexif()
    # for tag, value in info.items():
    #     decoded = ExifTags.TAGS.get(tag, tag)
    #     exif_table[decoded] = value
    # pdb.set_trace()
    # gps_ifd = info.get_ifd(ExifTags.IFD.GPSInfo)
    gps_ifd = image.getexif().get_ifd(0x8825)
    return gps_ifd


def gps_to_dms(value):
    d_, m_, s_ = value
    return (d_[0], # d
            m_[0], # m
            (float(s_[0]) / float(s_[1])) # s
        )

def dms_to_seconds(dms):
    d_, m_, s_ = dms
    return float((d_ * 60 + m_) * 60) + s_

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

import pdb

def get_photos_from_dir(path):
    max_lat = 0.0
    max_lat_dms = None
    min_lat = 180.0 * 3600.0
    min_lat_dms = None
    max_lng = 0.0
    max_lng_dms = None
    min_lng = 90.0 * 3600.0
    min_lng_dms = None
    photos = dict()
    for current in glob.iglob(path):
        exif = get_exif(current)
        try:
            value = exif['GPSInfo']
            exif_lat = value[2]
            exif_lng = value[4]
            dms_lat = gps_to_dms(exif_lat)
            dms_lng = gps_to_dms(exif_lng)
            photos[current] = (dms_lat, dms_lng)
            lat = dms_to_seconds(dms_lat)
            lng = dms_to_seconds(dms_lng)
            if max_lat < lat:
                max_lat = lat
                max_lat_dms = dms_lat
            elif lat < min_lat:
                min_lat = lat
                min_lat_dms = dms_lat
            if max_lng < lng:
                max_lng = lng
                max_lng_dms = dms_lng
            elif lng < min_lng:
                min_lng = lng
                min_lng_dms = dms_lng
        except KeyError:
           pass
    pdb.set_trace()
    if min_lat_dms == None:
        min_lat_dms = min_lat_dms
    if min_lng_dms == None:
        min_lng_dms = max_lng_dms
    print(min_lat_dms, ' ', max_lat_dms)
    lat_span = get_span(max_lat_dms, min_lat_dms)
    print(lat_span)
    print(min_lng_dms, ' ', max_lng_dms)
    lng_span = get_span(max_lng_dms, min_lng_dms)
    print(lng_span)
    lat_center = get_center(max_lat_dms, min_lat_dms)
    lng_center = get_center(max_lng_dms, min_lng_dms)
    print(min_lat_dms, ' ', max_lat_dms)
    print(min_lng_dms, ' ', max_lng_dms)
    print(lat_center, ' -  ', lng_center)
    return photos, max_lat_dms, min_lat_dms, max_lng_dms, min_lng_dms, lat_span, lng_span, lat_center, lng_center

if __name__ == '__main__':
    photos, max_lat_dms, min_lat_dms, max_lng_dms, min_lng_dms, lat_span, lng_span, lat_center, lng_center = get_photos_from_dir('/home/dberns/Data/fce_cr/crd/*.jpg')
    for i, item in enumerate(photos.iteritems()):
        k, v = item
        print(i, ' ', k, v)
