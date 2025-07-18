---
layout: publication
title: Gpu-friendly, Parallel, And (almost-)in-place Construction Of Left-balanced
  K-d Trees
authors: Wald Ingo
conference: 'Concurrency and Computation: Practice and Experience'
year: 2022
bibkey: wald2022gpu
citations: 18
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2211.00120'}]
tags: [Tree Based ANN]
---
We present an algorithm that allows for building left-balanced and complete
k-d trees over k-dimensional points in a trivially parallel and GPU friendly
way. Our algorithm requires exactly one int per data point as temporary
storage, and uses O(log N) iterations, each of which performs one parallel
sort, and one trivially parallel CUDA per-node update kernel.