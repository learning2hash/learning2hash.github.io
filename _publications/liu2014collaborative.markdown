---
layout: publication
title: "Collaborative Hashing"
authors:  X. Liu, J. He, C. Deng, B. Lang 
conference: CVPR
year: 2014
bibkey: liu2014collaborative
additional_links:
   - {name: "PDF", url: "http://www.nlsde.buaa.edu.cn/~xlliu/cvpr2014.pdf"}
   - {name: "Code", url: "http://www.nlsde.buaa.edu.cn/~xlliu/CH.zip"}
---
Hashing technique has become a promising approach for
fast similarity search. Most of existing hashing research
pursue the binary codes for the same type of entities by
preserving their similarities. In practice, there are many
scenarios involving nearest neighbor search on the data
given in matrix form, where two different types of, yet
naturally associated entities respectively correspond to its
two dimensions or views. To fully explore the duality
between the two views, we propose a collaborative hashing
scheme for the data in matrix form to enable fast search
in various applications such as image search using bag of
words and recommendation using user-item ratings. By
simultaneously preserving both the entity similarities in
each view and the interrelationship between views, our
collaborative hashing effectively learns the compact binary
codes and the explicit hash functions for out-of-sample
extension in an alternating optimization way. Extensive
evaluations are conducted on three well-known datasets
for search inside a single view and search across different
views, demonstrating that our proposed method outperforms
state-of-the-art baselines, with significant accuracy
gains ranging from 7.67% to 45.87% relatively.
