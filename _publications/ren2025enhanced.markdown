---
layout: publication
title: Enhanced Cross-modal 3D Retrieval Via Tri-modal Reconstruction
authors: Ren Junlong, Wang Hao
conference: 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2025
bibkey: ren2025enhanced
citations: 54
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2504.01476'}]
tags: [CVPR]
---
Cross-modal 3D retrieval is a critical yet challenging task, aiming to
achieve bi-directional retrieval between 3D and text modalities. Current
methods predominantly rely on a certain 3D representation (e.g., point cloud),
with few exploiting the 2D-3D consistency and complementary relationships,
which constrains their performance. To bridge this gap, we propose to adopt
multi-view images and point clouds to jointly represent 3D shapes, facilitating
tri-modal alignment (i.e., image, point, text) for enhanced cross-modal 3D
retrieval. Notably, we introduce tri-modal reconstruction to improve the
generalization ability of encoders. Given point features, we reconstruct image
features under the guidance of text features, and vice versa. With well-aligned
point cloud and multi-view image features, we aggregate them as multimodal
embeddings through fine-grained 2D-3D fusion to enhance geometric and semantic
understanding. Recognizing the significant noise in current datasets where many
3D shapes and texts share similar semantics, we employ hard negative
contrastive training to emphasize harder negatives with greater significance,
leading to robust discriminative embeddings. Extensive experiments on the
Text2Shape dataset demonstrate that our method significantly outperforms
previous state-of-the-art methods in both shape-to-text and text-to-shape
retrieval tasks by a substantial margin.