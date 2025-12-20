---
layout: publication
title: 'C-BEV: Contrastive Bird''s Eye View Training For Cross-view Image Retrieval
  And 3-dof Pose Estimation'
authors: Florian Fervers, Sebastian Bullinger, Christoph Bodensteiner, Michael Arens,
  Rainer Stiefelhagen
conference: Arxiv
year: 2023
bibkey: fervers2023c
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2312.08060'}]
tags: ["Datasets", "Evaluation", "Image Retrieval", "Supervised"]
short_authors: Fervers et al.
---
To find the geolocation of a street-view image, cross-view geolocalization
(CVGL) methods typically perform image retrieval on a database of georeferenced
aerial images and determine the location from the visually most similar match.
Recent approaches focus mainly on settings where street-view and aerial images
are preselected to align w.r.t. translation or orientation, but struggle in
challenging real-world scenarios where varying camera poses have to be matched
to the same aerial image. We propose a novel trainable retrieval architecture
that uses bird's eye view (BEV) maps rather than vectors as embedding
representation, and explicitly addresses the many-to-one ambiguity that arises
in real-world scenarios. The BEV-based retrieval is trained using the same
contrastive setting and loss as classical retrieval.
  Our method C-BEV surpasses the state-of-the-art on the retrieval task on
multiple datasets by a large margin. It is particularly effective in
challenging many-to-one scenarios, e.g. increasing the top-1 recall on VIGOR's
cross-area split with unknown orientation from 31.1% to 65.0%. Although the
model is supervised only through a contrastive objective applied on image
pairings, it additionally learns to infer the 3-DoF camera pose on the matching
aerial image, and even yields a lower mean pose error than recent methods that
are explicitly trained with metric groundtruth.