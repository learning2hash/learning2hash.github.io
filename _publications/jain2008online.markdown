---
layout: publication
title: Online Metric Learning and Fast Similarity Search
authors: Prateek Jain, Brian Kulis, Inderjit Dhillon, Kristen Grauman
conference: "Neural Information Processing Systems"
year: 2008
bibkey: jain2008online
tags: ['NEURIPS', 'TIP']
---
Metric learning algorithms can provide useful distance functions for a variety of domains and recent work has shown good accuracy for problems where the learner can access all distance constraints at once. However in many real applications constraints are only available incrementally thus necessitating methods that can perform online updates to the learned metric. Existing online algorithms offer bounds on worst-case performance but typically do not perform well in practice as compared to their offline counterparts. We present a new online metric learning algorithm that updates a learned Mahalanobis metric based on LogDet regularization and gradient descent. We prove theoretical worst-case performance bounds and empirically compare the proposed method against existing online metric learning algorithms. To further boost the practicality of our approach we develop an online locality-sensitive hashing scheme which leads to efficient updates for approximate similarity search data structures. We demonstrate our algorithm on multiple datasets and show that it outperforms relevant baselines.
