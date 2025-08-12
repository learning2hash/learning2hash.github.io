---
layout: publication
title: 'YOLIC: An Efficient Method For Object Localization And Classification On Edge
  Devices'
authors: Kai Su, Yoichi Tomioka, Qiangfu Zhao, Yong Liu
conference: Image and Vision Computing
year: 2024
bibkey: su2023yolic
citations: 3
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2307.06689'}]
tags: ["Efficiency"]
short_authors: Su et al.
---
In the realm of Tiny AI, we introduce ``You Only Look at Interested Cells"
(YOLIC), an efficient method for object localization and classification on edge
devices. Through seamlessly blending the strengths of semantic segmentation and
object detection, YOLIC offers superior computational efficiency and precision.
By adopting Cells of Interest for classification instead of individual pixels,
YOLIC encapsulates relevant information, reduces computational load, and
enables rough object shape inference. Importantly, the need for bounding box
regression is obviated, as YOLIC capitalizes on the predetermined cell
configuration that provides information about potential object location, size,
and shape. To tackle the issue of single-label classification limitations, a
multi-label classification approach is applied to each cell for effectively
recognizing overlapping or closely situated objects. This paper presents
extensive experiments on multiple datasets to demonstrate that YOLIC achieves
detection performance comparable to the state-of-the-art YOLO algorithms while
surpassing in speed, exceeding 30fps on a Raspberry Pi 4B CPU. All resources
related to this study, including datasets, cell designer, image annotation
tool, and source code, have been made publicly available on our project website
at https://kai3316.github.io/yolic.github.io