---
layout: publication
title: Real-time Human Action Recognition Using Locally Aggregated Kinematic-guided
  Skeletonlet And Supervised Hashing-by-analysis Model
authors: Bin Sun, Shaofan Wang, Dehui Kong, Lichun Wang, Baocai Yin
conference: IEEE Transactions on Cybernetics
year: 2021
bibkey: sun2021real
citations: 15
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2105.11312'}]
tags: ["Datasets", "Efficiency", "Hashing Methods", "Neural Hashing", "Supervised", "Tools & Libraries"]
short_authors: Sun et al.
---
3D action recognition is referred to as the classification of action
sequences which consist of 3D skeleton joints. While many research work are
devoted to 3D action recognition, it mainly suffers from three problems: highly
complicated articulation, a great amount of noise, and a low implementation
efficiency. To tackle all these problems, we propose a real-time 3D action
recognition framework by integrating the locally aggregated kinematic-guided
skeletonlet (LAKS) with a supervised hashing-by-analysis (SHA) model. We first
define the skeletonlet as a few combinations of joint offsets grouped in terms
of kinematic principle, and then represent an action sequence using LAKS, which
consists of a denoising phase and a locally aggregating phase. The denoising
phase detects the noisy action data and adjust it by replacing all the features
within it with the features of the corresponding previous frame, while the
locally aggregating phase sums the difference between an offset feature of the
skeletonlet and its cluster center together over all the offset features of the
sequence. Finally, the SHA model which combines sparse representation with a
hashing model, aiming at promoting the recognition accuracy while maintaining a
high efficiency. Experimental results on MSRAction3D, UTKinectAction3D and
Florence3DAction datasets demonstrate that the proposed method outperforms
state-of-the-art methods in both recognition accuracy and implementation
efficiency.