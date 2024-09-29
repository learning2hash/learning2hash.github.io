---
layout: publication
title: Asymmetric Deep Semantic Quantization For Image Retrieval
authors: Yang Zhan, Raymond Osolo Ian, Sun Wuqing, Long Jun
conference: "Arxiv"
year: 2019
bibkey: yang2019asymmetric
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/1903.12493"}
tags: ['ARXIV', 'Deep Learning', 'Image Retrieval', 'Quantisation', 'Supervised']
---
Due to its fast retrieval and storage efficiency capabilities hashing has been widely used in nearest neighbor retrieval tasks. By using deep learning based techniques hashing can outperform non45;learning based hashing technique in many applications. However we argue that the current deep learning based hashing methods ignore some critical problems (e.g. the learned hash codes are not discriminative due to the hashing methods being unable to discover rich semantic information and the training strategy having difficulty optimizing the discrete binary codes). In this paper we propose a novel image hashing method termed as textbf123;underline123;A125;125;symmetric textbf123;underline123;D125;125;eep textbf123;underline123;S125;125;emantic textbf123;underline123;Q125;125;uantization (textbf123;ADSQ125;). textbf123;ADSQ125; is implemented using three stream frameworks which consist of one emph123;LabelNet125; and two emph123;ImgNets125;. The emph123;LabelNet125; leverages the power of three fully45;connected layers which are used to capture rich semantic information between image pairs. For the two emph123;ImgNets125; they each adopt the same convolutional neural network structure but with different weights (i.e. asymmetric convolutional neural networks). The two emph123;ImgNets125; are used to generate discriminative compact hash codes. Specifically the function of the emph123;LabelNet125; is to capture rich semantic information that is used to guide the two emph123;ImgNets125; in minimizing the gap between the real45;continuous features and the discrete binary codes. Furthermore textbf123;ADSQ125; can utilize the most critical semantic information to guide the feature learning process and consider the consistency of the common semantic space and Hamming space. Experimental results on three benchmarks (i.e. CIFAR45;10 NUS45;WIDE and ImageNet) demonstrate that the proposed textbf123;ADSQ125; can outperforms current state45;of45;the45;art methods.
