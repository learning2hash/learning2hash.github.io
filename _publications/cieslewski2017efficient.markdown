---
layout: publication
title: Efficient Decentralized Visual Place Recognition From Full-image Descriptors
authors: Titus Cieslewski, Davide Scaramuzza
conference: 2017 International Symposium on Multi-Robot and Multi-Agent Systems (MRS)
year: 2017
bibkey: cieslewski2017efficient
citations: 28
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/1705.10739'}]
tags: ["Evaluation"]
short_authors: Titus Cieslewski, Davide Scaramuzza
---
In this paper, we discuss the adaptation of our decentralized place
recognition method described in [1] to full image descriptors. As we had shown,
the key to making a scalable decentralized visual place recognition lies in
exploting deterministic key assignment in a distributed key-value map. Through
this, it is possible to reduce bandwidth by up to a factor of n, the robot
count, by casting visual place recognition to a key-value lookup problem. In
[1], we exploited this for the bag-of-words method [3], [4]. Our method of
casting bag-of-words, however, results in a complex decentralized system, which
has inherently worse recall than its centralized counterpart. In this paper, we
instead start from the recent full-image description method NetVLAD [5]. As we
show, casting this to a key-value lookup problem can be achieved with k-means
clustering, and results in a much simpler system than [1]. The resulting system
still has some flaws, albeit of a completely different nature: it suffers when
the environment seen during deployment lies in a different distribution in
feature space than the environment seen during training.