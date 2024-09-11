---
layout: publication
title: "Deep Hashing via Discrepancy Minimization"
authors: Zhixiang Chen, Xin Yuan, Jiwen Lu*, Qi Tian, and Jie Zhou,
conference: CVPR
year: 2018
bibkey: chen2018deep
additional_links:
   - {name: "PDF", url: "https://openaccess.thecvf.com/content_cvpr_2018/CameraReady/0540.pdf"}
tags: ["CVPR", "Deep Learning"]
---
This paper presents a discrepancy minimizing model to
address the discrete optimization problem in hashing learning. The discrete optimization introduced by binary constraint is an NP-hard mixed integer programming problem.
It is usually addressed by relaxing the binary variables into
continuous variables to adapt to the gradient based learning of hashing functions, especially the training of deep
neural networks. To deal with the objective discrepancy
caused by relaxation, we transform the original binary optimization into differentiable optimization problem over hash
functions through series expansion. This transformation decouples the binary constraint and the similarity preserving
hashing function optimization. The transformed objective
is optimized in a tractable alternating optimization framework with gradual discrepancy minimization. Extensive experimental results on three benchmark datasets validate the
efficacy of the proposed discrepancy minimizing hashing.
