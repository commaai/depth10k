# depth10k

It's ~10,000 PNGs of real driving from comma 3. 3 frames in time order, with 50ms between them. MIT license

![Alt](imgs/00748_f_2061c2bef508176e_2021-09-21--15-19-15_15_392.png)
![Alt](imgs/00921_f_7aae592fc08e895f_2021-06-20--23-16-32_5_18.png)
![Alt](imgs/00254_f_978c02f5e9a7d1f7_2021-07-24--18-47-12_26_352.png)

It's [comma10k](https://github.com/commaai/comma10k), but for depthnets instead of segnets

A great dataset for training unsupervised depthnets on. We've tried:
* [depth_and_motion_learning](https://github.com/google-research/google-research/tree/master/depth_and_motion_learning)
* [monodepth2](https://github.com/nianticlabs/monodepth2)

and gotten decent results with both. Though they struggle with cars moving a similar speed to you.

We also ran our segnet on them, outputs in segs/. Might be useful for masking motion.

