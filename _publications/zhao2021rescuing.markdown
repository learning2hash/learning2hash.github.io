---
layout: publication
title: Rescuing Deep Hashing from Dead Bits Problem
authors: Zhao Shu, Wu Dayan, Zhou Yucan, Li Bo, Wang Weiping
conference: "Arxiv"
year: 2021
bibkey: zhao2021rescuing
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2102.00648"}
tags: ['ARXIV', 'General', 'Image Retrieval', 'Quantisation']
---
Deep hashing methods have shown great retrieval accuracy and efficiency in large-scale image retrieval. How to optimize discrete hash bits is always the focus in deep hashing methods. A common strategy in these methods is to adopt an activation function e.g. (cdot) or (cdot) and minimize a quantization loss to approximate discrete values. However this paradigm may make more and more hash bits stuck into the wrong saturated area of the activation functions and never escaped. We call this problem Dead Bits Problem~(DBP). Besides the existing quantization loss will aggravate DBP as well. In this paper we propose a simple but effective gradient amplifier which acts before activation functions to alleviate DBP. Moreover we devise an error-aware quantization loss to further alleviate DBP. It avoids the negative effect of quantization loss based on the similarity between two images. The proposed gradient amplifier and error-aware quantization loss are compatible with a variety of deep hashing methods. Experimental results on three datasets demonstrate the efficiency of the proposed gradient amplifier and the error-aware quantization loss.
