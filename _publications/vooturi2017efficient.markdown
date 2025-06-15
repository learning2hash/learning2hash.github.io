---
layout: publication
title: Efficient Inferencing Of Compressed Deep Neural Networks
authors: Vooturi Dharma Teja, Goyal Saurabh, Choudhury Anamitra R., Sabharwal Yogish, Verma Ashish
conference: "Arxiv"
year: 2017
citations: 0
bibkey: vooturi2017efficient
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1711.00244"}
tags: ['ARXIV', 'Quantisation', 'Supervised']
---
Large number of weights in deep neural networks makes the models difficult to
be deployed in low memory environments such as, mobile phones, IOT edge devices
as well as "inferencing as a service" environments on cloud. Prior work has
considered reduction in the size of the models, through compression techniques
like pruning, quantization, Huffman encoding etc. However, efficient
inferencing using the compressed models has received little attention,
specially with the Huffman encoding in place. In this paper, we propose
efficient parallel algorithms for inferencing of single image and batches,
under various memory constraints. Our experimental results show that our
approach of using variable batch size for inferencing achieves 15-25\%
performance improvement in the inference throughput for AlexNet, while
maintaining memory and latency constraints.
