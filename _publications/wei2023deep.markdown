---
layout: publication
title: Attribute45;aware Deep Hashing With Self45;consistency For Large45;scale Fine45;grained Image Retrieval
authors: Wei Xiu-shen, Shen Yang, Sun Xuhao, Wang Peng, Peng Yuxin
conference: "Arxiv"
year: 2023
bibkey: wei2023deep
additional_links:
  - {name: "Paper", url: "https://arxiv.org/abs/2311.12894"}
tags: ['ARXIV', 'Image Retrieval', 'Supervised']
---
Our work focuses on tackling large45;scale fine45;grained image retrieval as ranking the images depicting the concept of interests (i.e. the same sub45;category labels) highest based on the fine45;grained details in the query. It is desirable to alleviate the challenges of both fine45;grained nature of small inter45;class variations with large intra45;class variations and explosive growth of fine45;grained data for such a practical task. In this paper we propose attribute45;aware hashing networks with self45;consistency for generating attribute45;aware hash codes to not only make the retrieval process efficient but also establish explicit correspondences between hash codes and visual attributes. Specifically based on the captured visual representations by attention we develop an encoder45;decoder structure network of a reconstruction task to unsupervisedly distill high45;level attribute45;specific vectors from the appearance45;specific visual representations without attribute annotations. Our models are also equipped with a feature decorrelation constraint upon these attribute vectors to strengthen their representative abilities. Then driven by preserving original entities similarity the required hash codes can be generated from these attribute45;specific vectors and thus become attribute45;aware. Furthermore to combat simplicity bias in deep hashing we consider the model design from the perspective of the self45;consistency principle and propose to further enhance models self45;consistency by equipping an additional image reconstruction path. Comprehensive quantitative experiments under diverse empirical settings on six fine45;grained retrieval datasets and two generic retrieval datasets show the superiority of our models over competing methods.
