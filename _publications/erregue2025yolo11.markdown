---
layout: publication
title: 'YOLO11-JDE: Fast And Accurate Multi-object Tracking With Self-supervised Re-id'
authors: "I\xF1aki Erregue, Kamal Nasrollahi, Sergio Escalera"
conference: Arxiv
year: 2025
bibkey: erregue2025yolo11
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.13710'}]
tags: ["Efficiency", "Self-Supervised"]
short_authors: "I\xF1aki Erregue, Kamal Nasrollahi, Sergio Escalera"
---
We introduce YOLO11-JDE, a fast and accurate multi-object tracking (MOT) solution that combines real-time object detection with self-supervised Re-Identification (Re-ID). By incorporating a dedicated Re-ID branch into YOLO11s, our model performs Joint Detection and Embedding (JDE), generating appearance features for each detection. The Re-ID branch is trained in a fully self-supervised setting while simultaneously training for detection, eliminating the need for costly identity-labeled datasets. The triplet loss, with hard positive and semi-hard negative mining strategies, is used for learning discriminative embeddings. Data association is enhanced with a custom tracking implementation that successfully integrates motion, appearance, and location cues. YOLO11-JDE achieves competitive results on MOT17 and MOT20 benchmarks, surpassing existing JDE methods in terms of FPS and using up to ten times fewer parameters. Thus, making our method a highly attractive solution for real-world applications.