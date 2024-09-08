---
    layout: publication
    title: "Robust Camera Pose Refinement for Multi-Resolution Hash Encoding"
    authors: Heo Hwan, Kim Taekyung, Lee Jiyoung, Lee Jaewon, Kim Soohyun, Kim Hyunwoo J., Kim Jin-Hwa
    conference: Arxiv
    year: 2023
    bibkey: heo2023robust
    additional_links:
       - {name: "License", url: "http://creativecommons.org/licenses/by-nc-sa/4.0/"}
   - {name: "Paper", url: "https://arxiv.org/abs/2302.01571"}
    tags: ['Arxiv']
    ---
    {% raw %}
    Multi-resolution hash encoding has recently been proposed to reduce the computational cost of neural renderings, such as NeRF. This method requires accurate camera poses for the neural renderings of given scenes. However, contrary to previous methods jointly optimizing camera poses and 3D scenes, the naive gradient-based camera pose refinement method using multi-resolution hash encoding severely deteriorates performance. We propose a joint optimization algorithm to calibrate the camera pose and learn a geometric representation using efficient multi-resolution hash encoding. Showing that the oscillating gradient flows of hash encoding interfere with the registration of camera poses, our method addresses the issue by utilizing smooth interpolation weighting to stabilize the gradient oscillation for the ray samplings across hash grids. Moreover, the curriculum training procedure helps to learn the level-wise hash encoding, further increasing the pose refinement. Experiments on the novel-view synthesis datasets validate that our learning frameworks achieve state-of-the-art performance and rapid convergence of neural rendering, even when initial camera poses are unknown.
    {% endraw %}