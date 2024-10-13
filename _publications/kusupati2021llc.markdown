---
layout: publication
title: LLC Accurate Multi-purpose Learnt Low-dimensional Binary Codes
authors: Aditya Kusupati, Matthew Wallingford, Vivek Ramanujan, Raghav Somani, Jae Sung Park, Krishna Pillutla, Prateek Jain, Sham Kakade, Ali Farhadi
conference: "Neural Information Processing Systems"
year: 2021
bibkey: kusupati2021llc
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2021/hash/c88d8d0a6097754525e02c2246d8d27f-Abstract.html"}
  - {name: "Code", url: "https://github.com/RAIVNLab/LLC"}
tags: ['Has Code', 'Image Retrieval', 'NEURIPS', 'Supervised']
---
<p>Learning binary representations of instances and classes is a
classical problem with several high potential applications. In modern
settings, the compression of high-dimensional neural representations to
low-dimensional binary codes is a challenging task and often require
large bit-codes to be accurate. In this work, we propose a novel method
for <span class="math inline">\(\textbf{L}\)</span>earning <span
class="math inline">\(\textbf{L}\)</span>ow-dimensional binary <span
class="math inline">\(\textbf{C}\)</span>odes <span
class="math inline">\((\textbf{LLC})\)</span> for instances as well as
classes. Our method does <span
class="math inline">\({\textit{not}}\)</span> require any
side-information, like annotated attributes or label meta-data, and
learns extremely low-dimensional binary codes (<span
class="math inline">\(\approx 20\)</span> bits for ImageNet-1K). The
learnt codes are super-efficient while still ensuring <span
class="math inline">\(\textit{nearly optimal}\)</span> classification
accuracy for ResNet50 on ImageNet-1K. We demonstrate that the learnt
codes capture intrinsically important features in the data, by
discovering an intuitive taxonomy over classes. We further
quantitatively measure the quality of our codes by applying it to the
efficient image retrieval as well as out-of-distribution (OOD) detection
problems. For ImageNet-100 retrieval problem, our learnt binary codes
outperform <span class="math inline">\(16\)</span> bit HashNet using
only <span class="math inline">\(10\)</span> bits and also are as
accurate as <span class="math inline">\(10\)</span> dimensional real
representations. Finally, our learnt binary codes can perform OOD
detection, out-of-the-box, as accurately as a baseline that needs <span
class="math inline">\(\approx3000\)</span> samples to tune its
threshold, while we require <span
class="math inline">\({\textit{none}}\)</span>. Code is open-sourced at
https://github.com/RAIVNLab/LLC.</p>
