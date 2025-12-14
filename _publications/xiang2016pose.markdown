---
layout: publication
title: Pose-selective Max Pooling For Measuring Similarity
authors: Xiang Xiang, Trac D. Tran
conference: Arxiv
year: 2016
bibkey: xiang2016pose
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1609.07042'}]
tags: [Evaluation, Datasets]
short_authors: Xiang Xiang, Trac D. Tran
---
In this paper, we deal with two challenges for measuring the similarity of
the subject identities in practical video-based face recognition - the
variation of the head pose in uncontrolled environments and the computational
expense of processing videos. Since the frame-wise feature mean is unable to
characterize the pose diversity among frames, we define and preserve the
overall pose diversity and closeness in a video. Then, identity will be the
only source of variation across videos since the pose varies even within a
single video. Instead of simply using all the frames, we select those faces
whose pose point is closest to the centroid of the K-means cluster containing
that pose point. Then, we represent a video as a bag of frame-wise deep face
features while the number of features has been reduced from hundreds to K.
Since the video representation can well represent the identity, now we measure
the subject similarity between two videos as the max correlation among all
possible pairs in the two bags of features. On the official 5,000 video-pairs
of the YouTube Face dataset for face verification, our algorithm achieves a
comparable performance with VGG-face that averages over deep features of all
frames. Other vision tasks can also benefit from the generic idea of employing
geometric cues to improve the descriptiveness of deep features.