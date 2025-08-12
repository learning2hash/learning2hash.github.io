---
layout: publication
title: Compressed 3D Gaussian Splatting For Accelerated Novel View Synthesis
authors: "Simon Niedermayr, Josef Stumpfegger, R\xFCdiger Westermann"
conference: 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2024
bibkey: niedermayr2023compressed
citations: 38
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2401.02436'}]
tags: ["CVPR", "Efficiency"]
short_authors: "Simon Niedermayr, Josef Stumpfegger, R\xFCdiger Westermann"
---
Recently, high-fidelity scene reconstruction with an optimized 3D Gaussian
splat representation has been introduced for novel view synthesis from sparse
image sets. Making such representations suitable for applications like network
streaming and rendering on low-power devices requires significantly reduced
memory consumption as well as improved rendering efficiency. We propose a
compressed 3D Gaussian splat representation that utilizes sensitivity-aware
vector clustering with quantization-aware training to compress directional
colors and Gaussian parameters. The learned codebooks have low bitrates and
achieve a compression rate of up to \\(31\times\\) on real-world scenes with only
minimal degradation of visual quality. We demonstrate that the compressed splat
representation can be efficiently rendered with hardware rasterization on
lightweight GPUs at up to \\(4\times\\) higher framerates than reported via an
optimized GPU compute pipeline. Extensive experiments across multiple datasets
demonstrate the robustness and rendering speed of the proposed approach.