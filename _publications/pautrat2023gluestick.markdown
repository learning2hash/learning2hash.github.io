---
layout: publication
title: 'Gluestick: Robust Image Matching By Sticking Points And Lines Together'
authors: "R\xE9mi Pautrat, Iago Su\xE1rez, Yifan Yu, Marc Pollefeys, Viktor Larsson"
conference: 2023 IEEE/CVF International Conference on Computer Vision (ICCV)
year: 2023
bibkey: pautrat2023gluestick
citations: 37
additional_links: [{name: Code, url: 'https://github.com/cvg/GlueStick'}, {name: Paper,
    url: 'https://arxiv.org/abs/2304.02008'}]
tags: ["Datasets", "Efficiency", "Evaluation", "ICCV"]
short_authors: Pautrat et al.
---
Line segments are powerful features complementary to points. They offer
structural cues, robust to drastic viewpoint and illumination changes, and can
be present even in texture-less areas. However, describing and matching them is
more challenging compared to points due to partial occlusions, lack of texture,
or repetitiveness. This paper introduces a new matching paradigm, where points,
lines, and their descriptors are unified into a single wireframe structure. We
propose GlueStick, a deep matching Graph Neural Network (GNN) that takes two
wireframes from different images and leverages the connectivity information
between nodes to better glue them together. In addition to the increased
efficiency brought by the joint matching, we also demonstrate a large boost of
performance when leveraging the complementary nature of these two features in a
single architecture. We show that our matching strategy outperforms the
state-of-the-art approaches independently matching line segments and points for
a wide variety of datasets and tasks. The code is available at
https://github.com/cvg/GlueStick.