---
layout: publication
title: What Can Human Sketches Do For Object Detection?
authors: Pinaki Nath Chowdhury, Ayan Kumar Bhunia, Aneeshan Sain, Subhadeep Koley,
  Tao Xiang, Yi-Zhe Song
conference: 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2023
bibkey: chowdhury2023what
citations: 38
additional_links: [{name: Code, url: 'https://pinakinathc.github.io/sketch-detect'},
  {name: Paper, url: 'https://arxiv.org/abs/2303.15149'}]
tags: [Evaluation, Supervised, Image Retrieval, Few-shot & Zero-shot, Datasets, CVPR,
  Tools & Libraries]
short_authors: Chowdhury et al.
---
Sketches are highly expressive, inherently capturing subjective and
fine-grained visual cues. The exploration of such innate properties of human
sketches has, however, been limited to that of image retrieval. In this paper,
for the first time, we cultivate the expressiveness of sketches but for the
fundamental vision task of object detection. The end result is a sketch-enabled
object detection framework that detects based on what \textit\{you\} sketch --
\textit\{that\} ``zebra'' (e.g., one that is eating the grass) in a herd of
zebras (instance-aware detection), and only the \textit\{part\} (e.g., ``head" of
a ``zebra") that you desire (part-aware detection). We further dictate that our
model works without (i) knowing which category to expect at testing (zero-shot)
and (ii) not requiring additional bounding boxes (as per fully supervised) and
class labels (as per weakly supervised). Instead of devising a model from the
ground up, we show an intuitive synergy between foundation models (e.g., CLIP)
and existing sketch models build for sketch-based image retrieval (SBIR), which
can already elegantly solve the task -- CLIP to provide model generalisation,
and SBIR to bridge the (sketch\(\rightarrow\)photo) gap. In particular, we first
perform independent prompting on both sketch and photo branches of an SBIR
model to build highly generalisable sketch and photo encoders on the back of
the generalisation ability of CLIP. We then devise a training paradigm to adapt
the learned encoders for object detection, such that the region embeddings of
detected boxes are aligned with the sketch and photo embeddings from SBIR.
Evaluating our framework on standard object detection datasets like PASCAL-VOC
and MS-COCO outperforms both supervised (SOD) and weakly-supervised object
detectors (WSOD) on zero-shot setups. Project Page:
https://pinakinathc.github.io/sketch-detect