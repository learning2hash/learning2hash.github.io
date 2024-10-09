---
layout: publication
title: Mplug-owl Modularization Empowers Large Language Models With Multimodality
authors: Qinghao Ye, Haiyang Xu, Guohai Xu, Jiabo Ye, Ming Yan, Yiyang Zhou, Junyang Wang, Anwen Hu, Pengcheng Shi, Yaya Shi, Chenliang Li, Yuanhong Xu, Hehong Chen, Junfeng Tian, Qi Qian, Ji Zhang, Fei Huang, Jingren Zhou
conference: "Arxiv"
year: 2023
bibkey: ye2023mplug
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2304.14178v3"}
  - {name: "Code", url: "https://github.com/X-PLUG/mPLUG-Owl"}
  - {name: "Code", url: "https://www.modelscope.cn/studios/damo/mPLUG-Owl"}
tags: ['ARXIV', 'Cross Modal', 'Has Code', 'Supervised']
---
Large language models (LLMs) have demonstrated impressive zero-shot abilities on a variety of open-ended tasks while recent research has also explored the use of LLMs for multi-modal generation. In this study we introduce mPLUG-Owl a novel training paradigm that equips LLMs with multi-modal abilities through modularized learning of foundation LLM a visual knowledge module and a visual abstractor module. This approach can support multiple modalities and facilitate diverse unimodal and multimodal abilities through modality collaboration. The training paradigm of mPLUG-Owl involves a two-stage method for aligning image and text which learns visual knowledge with the assistance of LLM while maintaining and even improving the generation abilities of LLM. In the first stage the visual knowledge module and abstractor module are trained with a frozen LLM module to align the image and text. In the second stage language-only and multi-modal supervised datasets are used to jointly fine-tune a low-rank adaption (LoRA) module on LLM and the abstractor module by freezing the visual knowledge module. We carefully build a visually-related instruction evaluation set OwlEval. Experimental results show that our model outperforms existing multi-modal models demonstrating mPLUG-Owls impressive instruction and visual understanding ability multi-turn conversation ability and knowledge reasoning ability. Besides we observe some unexpected and exciting abilities such as multi-image correlation and scene text understanding which makes it possible to leverage it for harder real scenarios such as vision-only document comprehension. Our code pre-trained model instruction-tuned models and evaluation set are available at https://github.com/X-PLUG/mPLUG-Owl. The online demo is available at https://www.modelscope.cn/studios/damo/mPLUG-Owl.
