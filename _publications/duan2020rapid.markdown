---
layout: publication
title: 'Rapid: Rotation-aware People Detection In Overhead Fisheye Images'
authors: Zhihao Duan, M. Ozan Tezcan, Hayato Nakamura, Prakash Ishwar, Janusz Konrad
conference: 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops
  (CVPRW)
year: 2020
bibkey: duan2020rapid
citations: 61
additional_links: [{name: Code, url: 'http://vip.bu.edu/rapid'}, {name: Paper, url: 'https://arxiv.org/abs/2005.11623'}]
tags: ["CVPR"]
short_authors: Duan et al.
---
Recent methods for people detection in overhead, fisheye images either use
radially-aligned bounding boxes to represent people, assuming people always
appear along image radius or require significant pre-/post-processing which
radically increases computational complexity. In this work, we develop an
end-to-end rotation-aware people detection method, named RAPiD, that detects
people using arbitrarily-oriented bounding boxes. Our fully-convolutional
neural network directly regresses the angle of each bounding box using a
periodic loss function, which accounts for angle periodicities. We have also
created a new dataset with spatio-temporal annotations of rotated bounding
boxes, for people detection as well as other vision tasks in overhead fisheye
videos. We show that our simple, yet effective method outperforms
state-of-the-art results on three fisheye-image datasets. Code and dataset are
available at http://vip.bu.edu/rapid .