---
layout: publication
title: 'Zebrapose: Coarse To Fine Surface Encoding For 6dof Object Pose Estimation'
authors: Yongzhi Su, Mahdi Saleh, Torben Fetzer, Jason Rambach, Nassir Navab, Benjamin
  Busam, Didier Stricker, Federico Tombari
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: su2022zebrapose
citations: 106
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.09418'}]
tags: ["CVPR"]
short_authors: Su et al.
---
Establishing correspondences from image to 3D has been a key task of 6DoF
object pose estimation for a long time. To predict pose more accurately, deeply
learned dense maps replaced sparse templates. Dense methods also improved pose
estimation in the presence of occlusion. More recently researchers have shown
improvements by learning object fragments as segmentation. In this work, we
present a discrete descriptor, which can represent the object surface densely.
By incorporating a hierarchical binary grouping, we can encode the object
surface very efficiently. Moreover, we propose a coarse to fine training
strategy, which enables fine-grained correspondence prediction. Finally, by
matching predicted codes with object surface and using a PnP solver, we
estimate the 6DoF pose. Results on the public LM-O and YCB-V datasets show
major improvement over the state of the art w.r.t. ADD(-S) metric, even
surpassing RGB-D based methods in some cases.