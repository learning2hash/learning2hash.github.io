---
layout: publication
title: 'OVIR-3D: Open-vocabulary 3D Instance Retrieval Without Training On 3D Data'
authors: Shiyang Lu, Haonan Chang, Eric Pu Jing, Abdeslam Boularias, Kostas Bekris
conference: Arxiv
year: 2023
bibkey: lu2023ovir
citations: 2
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2311.02873'}]
tags: ["Datasets", "Efficiency"]
short_authors: Lu et al.
---
This work presents OVIR-3D, a straightforward yet effective method for
open-vocabulary 3D object instance retrieval without using any 3D data for
training. Given a language query, the proposed method is able to return a
ranked set of 3D object instance segments based on the feature similarity of
the instance and the text query. This is achieved by a multi-view fusion of
text-aligned 2D region proposals into 3D space, where the 2D region proposal
network could leverage 2D datasets, which are more accessible and typically
larger than 3D datasets. The proposed fusion process is efficient as it can be
performed in real-time for most indoor 3D scenes and does not require
additional training in 3D space. Experiments on public datasets and a real
robot show the effectiveness of the method and its potential for applications
in robot navigation and manipulation.