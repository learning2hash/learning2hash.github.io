---
layout: publication
title: 'SIOD: Single Instance Annotated Per Category Per Image For Object Detection'
authors: Hanjun Li, Xingjia Pan, Ke Yan, Fan Tang, Wei-Shi Zheng
conference: 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
year: 2022
bibkey: li2022siod
citations: 17
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2203.15353'}]
tags: ["CVPR"]
short_authors: Li et al.
---
Object detection under imperfect data receives great attention recently.
Weakly supervised object detection (WSOD) suffers from severe localization
issues due to the lack of instance-level annotation, while semi-supervised
object detection (SSOD) remains challenging led by the inter-image discrepancy
between labeled and unlabeled data. In this study, we propose the Single
Instance annotated Object Detection (SIOD), requiring only one instance
annotation for each existing category in an image. Degraded from inter-task
(WSOD) or inter-image (SSOD) discrepancies to the intra-image discrepancy, SIOD
provides more reliable and rich prior knowledge for mining the rest of
unlabeled instances and trades off the annotation cost and performance. Under
the SIOD setting, we propose a simple yet effective framework, termed
Dual-Mining (DMiner), which consists of a Similarity-based Pseudo Label
Generating module (SPLG) and a Pixel-level Group Contrastive Learning module
(PGCL). SPLG firstly mines latent instances from feature representation space
to alleviate the annotation missing problem. To avoid being misled by
inaccurate pseudo labels, we propose PGCL to boost the tolerance to false
pseudo labels. Extensive experiments on MS COCO verify the feasibility of the
SIOD setting and the superiority of the proposed method, which obtains
consistent and significant improvements compared to baseline methods and
achieves comparable results with fully supervised object detection (FSOD)
methods with only 40% instances annotated.