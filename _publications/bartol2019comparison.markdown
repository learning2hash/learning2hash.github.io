---
layout: publication
title: On The Comparison Of Classic And Deep Keypoint Detector And Descriptor Methods
authors: "Kristijan Bartol, David Bojani\u0107, Tomislav Pribani\u0107, Tomislav Petkovi\u0107\
  , Yago Diez Donoso, Joaquim Salvi Mas"
conference: 2019 11th International Symposium on Image and Signal Processing and Analysis
  (ISPA)
year: 2019
bibkey: bartol2019comparison
citations: 31
additional_links: [{name: Code, url: 'https://github.com/kristijanbartol/keypoint-algorithms-benchmark'},
  {name: Paper, url: 'https://arxiv.org/abs/2007.10000'}]
tags: []
short_authors: Bartol et al.
---
The purpose of this study is to give a performance comparison between several
classic hand-crafted and deep key-point detector and descriptor methods. In
particular, we consider the following classical algorithms: SIFT, SURF, ORB,
FAST, BRISK, MSER, HARRIS, KAZE, AKAZE, AGAST, GFTT, FREAK, BRIEF and RootSIFT,
where a subset of all combinations is paired into detector-descriptor
pipelines. Additionally, we analyze the performance of two recent and
perspective deep detector-descriptor models, LF-Net and SuperPoint. Our
benchmark relies on the HPSequences dataset that provides real and diverse
images under various geometric and illumination changes. We analyze the
performance on three evaluation tasks: keypoint verification, image matching
and keypoint retrieval. The results show that certain classic and deep
approaches are still comparable, with some classic detector-descriptor
combinations overperforming pretrained deep models. In terms of the execution
times of tested implementations, SuperPoint model is the fastest, followed by
ORB. The source code is published on
https://github.com/kristijanbartol/keypoint-algorithms-benchmark.