---
layout: publication
title: Resolving Symmetry Ambiguity In Correspondence-based Methods For Instance-level
  Object Pose Estimation
authors: Yongliang Lin, Yongzhi Su, Sandeep Inuganti, Yan di, Naeem Ajilforoushan,
  Hanqing Yang, Yu Zhang, Jason Rambach
conference: IEEE Transactions on Image Processing
year: 2025
bibkey: lin2024resolving
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2405.10557'}]
tags: ["Evaluation", "Image Retrieval", "Robustness"]
short_authors: Lin et al.
---
Estimating the 6D pose of an object from a single RGB image is a critical
task that becomes additionally challenging when dealing with symmetric objects.
Recent approaches typically establish one-to-one correspondences between image
pixels and 3D object surface vertices. However, the utilization of one-to-one
correspondences introduces ambiguity for symmetric objects. To address this, we
propose SymCode, a symmetry-aware surface encoding that encodes the object
surface vertices based on one-to-many correspondences, eliminating the problem
of one-to-one correspondence ambiguity. We also introduce SymNet, a fast
end-to-end network that directly regresses the 6D pose parameters without
solving a PnP problem. We demonstrate faster runtime and comparable accuracy
achieved by our method on the T-LESS and IC-BIN benchmarks of mostly symmetric
objects. Our source code will be released upon acceptance.