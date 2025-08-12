---
layout: publication
title: Envisioning Class Entity Reasoning By Large Language Models For Few-shot Learning
authors: Mushui Liu, Fangtai Wu, Bozheng Li, Ziqian Lu, Yunlong Yu, Xi Li
conference: Proceedings of the AAAI Conference on Artificial Intelligence
year: 2025
bibkey: liu2024envisioning
citations: 1
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2408.12469'}]
tags: ["AAAI", "Few Shot & Zero Shot"]
short_authors: Liu et al.
---
Few-shot learning (FSL) aims to recognize new concepts using a limited number
of visual samples. Existing approaches attempt to incorporate semantic
information into the limited visual data for category understanding. However,
these methods often enrich class-level feature representations with abstract
category names, failing to capture the nuanced features essential for effective
generalization. To address this issue, we propose a novel framework for FSL,
which incorporates both the abstract class semantics and the concrete class
entities extracted from Large Language Models (LLMs), to enhance the
representation of the class prototypes. Specifically, our framework composes a
Semantic-guided Visual Pattern Extraction (SVPE) module and a
Prototype-Calibration (PC) module, where the SVPE meticulously extracts
semantic-aware visual patterns across diverse scales, while the PC module
seamlessly integrates these patterns to refine the visual prototype, enhancing
its representativeness. Extensive experiments on four few-shot classification
benchmarks and the BSCD-FSL cross-domain benchmarks showcase remarkable
advancements over the current state-of-the-art methods. Notably, for the
challenging one-shot setting, our approach, utilizing the ResNet-12 backbone,
achieves an impressive average improvement of 1.95% over the second-best
competitor.