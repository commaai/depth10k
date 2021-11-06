#!/usr/bin/env python3
import os
from PIL import Image
from tqdm import tqdm
from multiprocessing import Pool

BD = "/raid/triples/"
BDSEG = "/raid/triplesseg/"

def transform(im):
  im = im.crop((0, 308, 5784, 308+592))
  # (5784/1248) = 4.63461538462
  im = im.resize((1248, 128))
  return im


def get_seg_frames(fn):
  im = Image.open(BDSEG+fn)
  im = transform(im)
  print(fn)
  im.save("segs/"+fn)

def get_frames(fn):
  im = Image.open(BD+fn)
  im = transform(im)
  print(fn)
  im.save("imgs/"+fn)

tici_f_focal_length = 2648.0

if __name__ == "__main__":
  segs = sorted(os.listdir(BD))
  p = Pool(64)

  """
  arr = ["comma3 %s" % fn.split(".")[0] for fn in segs]
  with open("train.txt", "w") as f:
    f.write('\n'.join(arr))

  fl = tici_f_focal_length / 4.63461538462
  dx = (1928/2) / 4.63461538462
  dy = ((1208/2)-400) / 4.63461538462
  istr = "%f,0.0,%f,0.0,%f,%f,0.0,0.0,1.0" % (fl, dx, fl, dy)
  print(istr)

  for s in segs:
    with open("/raid/depth/comma3/"+s.replace(".png", "_cam.txt"), "w") as f:
      f.write(istr)
  """

  for x in tqdm(p.imap_unordered(get_seg_frames, segs)):
    pass

  #for x in tqdm(p.imap_unordered(get_frames, segs)):
  #  pass
