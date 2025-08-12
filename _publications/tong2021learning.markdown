---
layout: publication
title: Learning From Miscellaneous Other-class Words For Few-shot Named Entity Recognition
authors: Meihan Tong, Shuai Wang, Bin Xu, Yixin Cao, Minghui Liu, Lei Hou, Juanzi
  Li
conference: 'Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 1: Long Papers)'
year: 2021
bibkey: tong2021learning
citations: 40
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2106.15167'}]
tags: ["Few Shot & Zero Shot"]
short_authors: Tong et al.
---
Few-shot Named Entity Recognition (NER) exploits only a handful of
annotations to identify and classify named entity mentions. Prototypical
network shows superior performance on few-shot NER. However, existing
prototypical methods fail to differentiate rich semantics in other-class words,
which will aggravate overfitting under few shot scenario. To address the issue,
we propose a novel model, Mining Undefined Classes from Other-class (MUCO),
that can automatically induce different undefined classes from the other class
to improve few-shot NER. With these extra-labeled undefined classes, our method
will improve the discriminative ability of NER classifier and enhance the
understanding of predefined classes with stand-by semantic knowledge.
Experimental results demonstrate that our model outperforms five
state-of-the-art models in both 1-shot and 5-shots settings on four NER
benchmarks. We will release the code upon acceptance. The source code is
released on https: //github.com/shuaiwa16/OtherClassNER.git.