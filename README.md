# depth10k

It's 10,000 PNGs of real driving from comma 3. 3 frames in order. MIT license

![Alt](imgs/00010_f_7aae592fc08e895f_2021-07-19--08-27-56_18_884.png)
![Alt](imgs/00119_f_965a780ebeeed150_2021-09-07--16-22-06_19_607.png)
![Alt](imgs/00622_f_597b2770d03838db_2021-07-29--11-32-08_31_386.png)

It's [comma10k](https://github.com/commaai/comma10k), but for depthnets instead of segnets

A great dataset for training unsupervised depthnets on. We've tried:
* [depth_and_motion_learnin](https://github.com/google-research/google-research/tree/master/depth_and_motion_learning)
* [monodepth2](https://github.com/nianticlabs/monodepth2)
and gotten decent results with both. Though they struggle with cars moving a similar speed to you.

We also ran our segnet on them, outputs in segs/. Might be useful for masking motion.

