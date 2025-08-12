---
layout: publication
title: Image Scene Graph Generation (SGG) Benchmark
authors: Xiaotian Han, Jianwei Yang, Houdong Hu, Lei Zhang, Jianfeng Gao, Pengchuan
  Zhang
conference: Arxiv
year: 2021
bibkey: han2021image
citations: 17
additional_links: [{name: Code, url: 'https://github.com/microsoft/scene_graph_benchmark'},
  {name: Paper, url: 'https://arxiv.org/abs/2107.12604'}]
tags: ["Datasets", "Evaluation"]
short_authors: Han et al.
---
There is a surge of interest in image scene graph generation (object,
attribute and relationship detection) due to the need of building fine-grained
image understanding models that go beyond object detection. Due to the lack of
a good benchmark, the reported results of different scene graph generation
models are not directly comparable, impeding the research progress. We have
developed a much-needed scene graph generation benchmark based on the
maskrcnn-benchmark and several popular models. This paper presents main
features of our benchmark and a comprehensive ablation study of scene graph
generation models using the Visual Genome and OpenImages Visual relationship
detection datasets. Our codebase is made publicly available at
https://github.com/microsoft/scene_graph_benchmark.