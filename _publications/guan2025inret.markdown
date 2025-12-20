---
layout: publication
title: 'Inret: A General Framework For Accurate Retrieval Of Inrs For Shapes'
authors: Yushi Guan, Daniel Kwan, Ruofan Liang, Selvakumar Panneer, Nilesh Jain, Nilesh
  Ahuja, Nandita Vijaykumar
conference: 2025 International Conference on 3D Vision (3DV)
year: 2025
bibkey: guan2025inret
citations: 0
additional_links: [{name: Paper, url: 'https://arxiv.org/abs/2501.15722'}]
tags: ["Tools & Libraries"]
short_authors: Guan et al.
---
Implicit neural representations (INRs) have become an important method for
encoding various data types, such as 3D objects or scenes, images, and videos.
They have proven to be particularly effective at representing 3D content, e.g.,
3D scene reconstruction from 2D images, novel 3D content creation, as well as
the representation, interpolation, and completion of 3D shapes. With the
widespread generation of 3D data in an INR format, there is a need to support
effective organization and retrieval of INRs saved in a data store. A key
aspect of retrieval and clustering of INRs in a data store is the formulation
of similarity between INRs that would, for example, enable retrieval of similar
INRs using a query INR. In this work, we propose INRet, a method for
determining similarity between INRs that represent shapes, thus enabling
accurate retrieval of similar shape INRs from an INR data store. INRet flexibly
supports different INR architectures such as INRs with octree grids, triplanes,
and hash grids, as well as different implicit functions including
signed/unsigned distance function and occupancy field. We demonstrate that our
method is more general and accurate than the existing INR retrieval method,
which only supports simple MLP INRs and requires the same architecture between
the query and stored INRs. Furthermore, compared to converting INRs to other
representations (e.g., point clouds or multi-view images) for 3D shape
retrieval, INRet achieves higher accuracy while avoiding the conversion
overhead.