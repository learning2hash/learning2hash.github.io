---
layout: publication
title: Image Retrieval With Intra-sweep Representation Learning For Neck Ultrasound
  Scanning Guidance
authors: Wanwen Chen, Adam Schmidt, Eitan Prisman, Septimiu E. Salcudean
conference: Arxiv
year: 2024
bibkey: chen2024image
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2412.07741'}]
tags: ["Efficiency", "Evaluation", "Image Retrieval", "Self-Supervised", "Supervised"]
short_authors: Chen et al.
---
Purpose: Intraoperative ultrasound (US) can enhance real-time visualization
in transoral robotic surgery. The surgeon creates a mental map with a
pre-operative scan. Then, a surgical assistant performs freehand US scanning
during the surgery while the surgeon operates at the remote surgical console.
Communicating the target scanning plane in the surgeon's mental map is
difficult. Automatic image retrieval can help match intraoperative images to
preoperative scans, guiding the assistant to adjust the US probe toward the
target plane. Methods: We propose a self-supervised contrastive learning
approach to match intraoperative US views to a preoperative image database. We
introduce a novel contrastive learning strategy that leverages intra-sweep
similarity and US probe location to improve feature encoding. Additionally, our
model incorporates a flexible threshold to reject unsatisfactory matches.
Results: Our method achieves 92.30% retrieval accuracy on simulated data and
outperforms state-of-the-art temporal-based contrastive learning approaches.
Our ablation study demonstrates that using probe location in the optimization
goal improves image representation, suggesting that semantic information can be
extracted from probe location. We also present our approach on real patient
data to show the feasibility of the proposed US probe localization system
despite tissue deformation from tongue retraction. Conclusion: Our contrastive
learning method, which utilizes intra-sweep similarity and US probe location,
enhances US image representation learning. We also demonstrate the feasibility
of using our image retrieval method to provide neck US localization on real
patient US after tongue retraction.