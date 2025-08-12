---
layout: publication
title: 'Fine-grained Is Too Coarse: A Novel Data-centric Approach For Efficient Scene
  Graph Generation'
authors: "Neau Ma\xEBlic, Paulo E. Santos, Anne-Gwenn Bosser, C\xE9dric Buche"
conference: 2023 IEEE/CVF International Conference on Computer Vision Workshops (ICCVW)
year: 2023
bibkey: "ma\xEBlic2023fine"
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2305.18668'}]
tags: ["Efficiency", "ICCV"]
short_authors: "Ma\xEBlic et al."
---
Learning to compose visual relationships from raw images in the form of scene
graphs is a highly challenging task due to contextual dependencies, but it is
essential in computer vision applications that depend on scene understanding.
However, no current approaches in Scene Graph Generation (SGG) aim at providing
useful graphs for downstream tasks. Instead, the main focus has primarily been
on the task of unbiasing the data distribution for predicting more fine-grained
relations. That being said, all fine-grained relations are not equally relevant
and at least a part of them are of no use for real-world applications. In this
work, we introduce the task of Efficient SGG that prioritizes the generation of
relevant relations, facilitating the use of Scene Graphs in downstream tasks
such as Image Generation. To support further approaches, we present a new
dataset, VG150-curated, based on the annotations of the popular Visual Genome
dataset. We show through a set of experiments that this dataset contains more
high-quality and diverse annotations than the one usually use in SGG. Finally,
we show the efficiency of this dataset in the task of Image Generation from
Scene Graphs.