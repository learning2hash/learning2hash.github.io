---
layout: publication
title: Vcoder Versatile Vision Encoders For Multimodal Large Language Models
authors: Jitesh Jain, Jianwei Yang, Humphrey Shi
conference: "Arxiv"
year: 2023
bibkey: jain2023vcoder
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/http://arxiv.org/abs/2312.14233v1"}
  - {name: "Code", url: "https://github.com/SHI-Labs/VCoder"}
tags: ['ARXIV', 'Cross Modal', 'Has Code']
---
Humans possess the remarkable skill of Visual Perception the ability to see and understand the seen helping them make sense of the visual world and in turn reason. Multimodal Large Language Models (MLLM) have recently achieved impressive performance on vision-language tasks ranging from visual question-answering and image captioning to visual reasoning and image generation. However when prompted to identify or count (perceive) the entities in a given image existing MLLM systems fail. Working towards developing an accurate MLLM system for perception and reasoning we propose using Versatile vision enCoders (VCoder) as perception eyes for Multimodal LLMs. We feed the VCoder with perception modalities such as segmentation or depth maps improving the MLLMs perception abilities. Secondly we leverage the images from COCO and outputs from off-the-shelf vision perception models to create our COCO Segmentation Text (COST) dataset for training and evaluating MLLMs on the object perception task. Thirdly we introduce metrics to assess the object perception abilities in MLLMs on our COST dataset. Lastly we provide extensive experimental evidence proving the VCoders improved object-level perception skills over existing Multimodal LLMs including GPT-4V. We open-source our dataset code and models to promote research. We open-source our code at https://github.com/SHI-Labs/VCoder
