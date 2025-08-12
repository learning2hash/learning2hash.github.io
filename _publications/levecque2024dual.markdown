---
layout: publication
title: 'Dual JPEG Compatibility: A Reliable And Explainable Tool For Image Forensics'
authors: Etienne Levecque, Jan Butora, Patrick Bas
conference: Arxiv
year: 2024
bibkey: levecque2024dual
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.17106'}]
tags: []
short_authors: Etienne Levecque, Jan Butora, Patrick Bas
---
Given a JPEG pipeline (compression or decompression), this paper demonstrates
how to find the antecedent of an 8x8 block. If it exists, the block is
considered compatible with the pipeline. For unaltered images, all blocks
remain compatible with the original pipeline; however, for manipulated images,
this is not necessarily true. This article provides a first demonstration of
the potential of compatibility-based approaches for JPEG image forensics. It
introduces a method to address the key challenge of finding a block antecedent
in a high-dimensional space, relying on a local search algorithm with
restrictions on the search space. We show that inpainting, copy-move, and
splicing, when applied after JPEG compression, result in three distinct
mismatch problems that can be detected. In particular, if the image is
re-compressed after modification, the manipulation can be detected when the
quality factor of the second compression is higher than that of the first.
Through extensive experiments, we highlight the potential of this compatibility
attack under varying degrees of assumptions. While our approach shows promising
results-outperforming three state-of-the-art deep learning models in an
idealized setting-it remains a proof of concept rather than an off-the-shelf
forensic tool. Notably, with a perfect knowledge of the JPEG pipeline, our
method guarantees zero false alarms in block-by-block localization, given
sufficient computational power.