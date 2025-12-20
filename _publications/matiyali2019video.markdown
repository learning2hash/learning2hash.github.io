---
layout: publication
title: Video Person Re-identification Using Learned Clip Similarity Aggregation
authors: Neeraj Matiyali, Gaurav Sharma
conference: 2020 IEEE Winter Conference on Applications of Computer Vision (WACV)
year: 2019
bibkey: matiyali2019video
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1910.08055'}]
tags: ["Evaluation"]
short_authors: Neeraj Matiyali, Gaurav Sharma
---
We address the challenging task of video-based person re-identification.
Recent works have shown that splitting the video sequences into clips and then
aggregating clip based similarity is appropriate for the task. We show that
using a learned clip similarity aggregation function allows filtering out hard
clip pairs, e.g. where the person is not clearly visible, is in a challenging
pose, or where the poses in the two clips are too different to be informative.
This allows the method to focus on clip-pairs which are more informative for
the task. We also introduce the use of 3D CNNs for video-based
re-identification and show their effectiveness by performing equivalent to
previous works, which use optical flow in addition to RGB, while using RGB
inputs only. We give quantitative results on three challenging public
benchmarks and show better or competitive performance. We also validate our
method qualitatively.