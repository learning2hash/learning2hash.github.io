---
layout: publication
title: 'CARAFE++: Unified Content-aware Reassembly Of Features'
authors: Jiaqi Wang, Kai Chen, Rui Xu, Ziwei Liu, Chen Change Loy, Dahua Lin
conference: IEEE Transactions on Pattern Analysis and Machine Intelligence
year: 2021
bibkey: wang2020carafe
citations: 46
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2012.04733'}]
tags: []
short_authors: Wang et al.
---
Feature reassembly, i.e. feature downsampling and upsampling, is a key
operation in a number of modern convolutional network architectures, e.g.,
residual networks and feature pyramids. Its design is critical for dense
prediction tasks such as object detection and semantic/instance segmentation.
In this work, we propose unified Content-Aware ReAssembly of FEatures
(CARAFE++), a universal, lightweight and highly effective operator to fulfill
this goal. CARAFE++ has several appealing properties: (1) Unlike conventional
methods such as pooling and interpolation that only exploit sub-pixel
neighborhood, CARAFE++ aggregates contextual information within a large
receptive field. (2) Instead of using a fixed kernel for all samples (e.g.
convolution and deconvolution), CARAFE++ generates adaptive kernels on-the-fly
to enable instance-specific content-aware handling. (3) CARAFE++ introduces
little computational overhead and can be readily integrated into modern network
architectures. We conduct comprehensive evaluations on standard benchmarks in
object detection, instance/semantic segmentation and image inpainting. CARAFE++
shows consistent and substantial gains across all the tasks (2.5% APbox, 2.1%
APmask, 1.94% mIoU, 1.35 dB respectively) with negligible computational
overhead. It shows great potential to serve as a strong building block for
modern deep networks.