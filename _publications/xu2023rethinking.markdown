---
layout: publication
title: Rethinking The Localization In Weakly Supervised Object Localization
authors: Rui Xu, Yong Luo, Han Hu, Bo Du, Jialie Shen, Yonggang Wen
conference: Proceedings of the 31st ACM International Conference on Multimedia
year: 2023
bibkey: xu2023rethinking
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2308.06161'}]
tags: []
short_authors: Xu et al.
---
Weakly supervised object localization (WSOL) is one of the most popular and
challenging tasks in computer vision. This task is to localize the objects in
the images given only the image-level supervision. Recently, dividing WSOL into
two parts (class-agnostic object localization and object classification) has
become the state-of-the-art pipeline for this task. However, existing solutions
under this pipeline usually suffer from the following drawbacks: 1) they are
not flexible since they can only localize one object for each image due to the
adopted single-class regression (SCR) for localization; 2) the generated pseudo
bounding boxes may be noisy, but the negative impact of such noise is not well
addressed. To remedy these drawbacks, we first propose to replace SCR with a
binary-class detector (BCD) for localizing multiple objects, where the detector
is trained by discriminating the foreground and background. Then we design a
weighted entropy (WE) loss using the unlabeled data to reduce the negative
impact of noisy bounding boxes. Extensive experiments on the popular
CUB-200-2011 and ImageNet-1K datasets demonstrate the effectiveness of our
method.