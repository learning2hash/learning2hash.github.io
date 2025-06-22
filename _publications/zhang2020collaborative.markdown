---
layout: publication
title: Collaborative Generative Hashing For Marketing And Fast Cold-start Recommendation
authors: Yan Zhang, Ivor W. Tsang, Lixin Duan
conference: Arxiv
year: 2020
citations: 6
bibkey: zhang2020collaborative
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2011.00953'}]
tags: [Tools and Libraries, Hashing Methods, RecSys]
---
Cold-start has being a critical issue in recommender systems with the
explosion of data in e-commerce. Most existing studies proposed to alleviate
the cold-start problem are also known as hybrid recommender systems that learn
representations of users and items by combining user-item interactive and
user/item content information. However, previous hybrid methods regularly
suffered poor efficiency bottlenecking in online recommendations with
large-scale items, because they were designed to project users and items into
continuous latent space where the online recommendation is expensive. To this
end, we propose a collaborative generated hashing (CGH) framework to improve
the efficiency by denoting users and items as binary codes, then fast hashing
search techniques can be used to speed up the online recommendation. In
addition, the proposed CGH can generate potential users or items for marketing
application where the generative network is designed with the principle of
Minimum Description Length (MDL), which is used to learn compact and
informative binary codes. Extensive experiments on two public datasets show the
advantages for recommendations in various settings over competing baselines and
analyze its feasibility in marketing application.