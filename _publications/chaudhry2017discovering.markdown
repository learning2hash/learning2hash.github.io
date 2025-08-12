---
layout: publication
title: Discovering Class-specific Pixels For Weakly-supervised Semantic Segmentation
authors: Arslan Chaudhry, Puneet K. Dokania, Philip H. S. Torr
conference: Procedings of the British Machine Vision Conference 2017
year: 2017
bibkey: chaudhry2017discovering
citations: 144
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1707.05821'}]
tags: []
short_authors: Arslan Chaudhry, Puneet K. Dokania, Philip H. S. Torr
---
We propose an approach to discover class-specific pixels for the
weakly-supervised semantic segmentation task. We show that properly combining
saliency and attention maps allows us to obtain reliable cues capable of
significantly boosting the performance. First, we propose a simple yet powerful
hierarchical approach to discover the class-agnostic salient regions, obtained
using a salient object detector, which otherwise would be ignored. Second, we
use fully convolutional attention maps to reliably localize the class-specific
regions in a given image. We combine these two cues to discover class-specific
pixels which are then used as an approximate ground truth for training a CNN.
While solving the weakly supervised semantic segmentation task, we ensure that
the image-level classification task is also solved in order to enforce the CNN
to assign at least one pixel to each object present in the image.
Experimentally, on the PASCAL VOC12 val and test sets, we obtain the mIoU of
60.8% and 61.9%, achieving the performance gains of 5.1% and 5.2% compared to
the published state-of-the-art results. The code is made publicly available.