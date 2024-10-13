---
layout: publication
title: Vision Transformer Based Video Hashing Retrieval For Tracing The Source Of Fake Videos
authors: Pei Pengfei, Zhao Xianfeng, Cao Yun, Li Jinchuan, Lai Xuyuan
conference: "Arxiv"
year: 2021
bibkey: pei2021vision
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2112.08117"}
  - {name: "Code", url: "https://github.com/lajlksdf/vtl}"}
tags: ['ARXIV', 'Has Code']
---
In recent years, the spread of fake videos has brought great influence on individuals and even countries. It is important to provide robust and reliable results for fake videos. The results of conventional detection methods are not reliable and not robust for unseen videos. Another alternative and more effective way is to find the original video of the fake video. For example, fake videos from the Russia-Ukraine war and the Hong Kong law revision storm are refuted by finding the original video. We use an improved retrieval method to find the original video, named ViTHash. Specifically, tracing the source of fake videos requires finding the unique one, which is difficult when there are only small differences in the original videos. To solve the above problems, we designed a novel loss Hash Triplet Loss. In addition, we designed a tool called Localizator to compare the difference between the original traced video and the fake video. We have done extensive experiments on FaceForensics++, Celeb-DF and DeepFakeDetection, and we also have done additional experiments on our built three datasets: DAVIS2016-TL (video inpainting), VSTL (video splicing) and DFTL (similar videos). Experiments have shown that our performance is better than state-of-the-art methods, especially in cross-dataset mode. Experiments also demonstrated that ViTHash is effective in various forgery detection: video inpainting, video splicing and deepfakes. Our code and datasets have been released on GitHub: \\url\{https://github.com/lajlksdf/vtl\}.
