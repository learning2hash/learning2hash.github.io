---
layout: publication
title: Hashing Hyperplane Queries to Near Points with Applications to Large-Scale Active Learning
authors: ['Prateek Jain', 'Sudheendra Vijayanarasimhan', 'Kristen Grauman']
conference: "Neural Information Processing Systems"
year: 2010
bibkey: prateekjain2010hashing
tags: ['NEURIPS']
---
We consider the problem of retrieving the database points nearest to a given em hyperplane query without exhaustively scanning the database. We propose two hashing-based solutions. Our first approach maps the data to two-bit binary keys that are locality-sensitive for the angle between the hyperplane normal and a database point. Our second approach embeds the data into a vector space where the Euclidean norm reflects the desired distance between the original points and hyperplane query. Both use hashing to retrieve near points in sub-linear time. Our first methods preprocessing stage is more efficient while the second has stronger accuracy guarantees. We apply both to pool-based active learning taking the current hyperplane classifier as a query our algorithm identifies those points (approximately) satisfying the well-known minimal distance-to-hyperplane selection criterion. We empirically demonstrate our methods tradeoffs and show that they make it practical to perform active selection with millions of unlabeled points.
