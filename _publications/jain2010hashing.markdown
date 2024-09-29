---
layout: publication
title: Hashing Hyperplane Queries To Near Points With Applications To Large45;scale Active Learning
authors: Prateek Jain, Sudheendra Vijayanarasimhan, Kristen Grauman
conference: "Neural Information Processing Systems"
year: 2010
bibkey: jain2010hashing
additional_links:
  - {name: "Paper", url: "https://papers.nips.cc/paper/2010/hash/470e7a4f017a5476afb7eeb3f8b96f9b-Abstract.html"}
tags: ['NEURIPS']
---
We consider the problem of retrieving the database points nearest to a given 123;em hyperplane125; query without exhaustively scanning the database. We propose two hashing45;based solutions. Our first approach maps the data to two45;bit binary keys that are locality45;sensitive for the angle between the hyperplane normal and a database point. Our second approach embeds the data into a vector space where the Euclidean norm reflects the desired distance between the original points and hyperplane query. Both use hashing to retrieve near points in sub45;linear time. Our first methods preprocessing stage is more efficient while the second has stronger accuracy guarantees. We apply both to pool45;based active learning taking the current hyperplane classifier as a query our algorithm identifies those points (approximately) satisfying the well45;known minimal distance45;to45;hyperplane selection criterion. We empirically demonstrate our methods tradeoffs and show that they make it practical to perform active selection with millions of unlabeled points.
