---
title: "E-Calib: A fast, robust, and accurate calibration toolbox for event cameras"
authors:
- Mohammed Salah
- Abdulla Ayyad
- Muhammad Humais
- Daniel Gehrig
- Abdelqader Abusafieh
- Lakmal Seneviratne
- Davide Scaramuzza
- Yahya Zweiri
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2024-03-20T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["article"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Transactions on Image Processing (TRIP)*"
publication_short: ""

abstract: "Event cameras triggered a paradigm shift in the computer vision community delineated by their asynchronous nature, low latency, and high dynamic range. Calibration of event cameras is always essential to account for the sensor intrinsic parameters and for 3D perception. However, conventional image-based calibration techniques are not applicable due to the asynchronous, binary output of the sensor. The current standard for calibrating event cameras relies on either blinking patterns or event-based image reconstruction algorithms. These approaches are difficult to deploy in factory settings and are affected by noise and artifacts degrading the calibration performance. To bridge these limitations, we present E-Calib, a novel, fast, robust, and accurate calibration toolbox for event cameras utilizing the asymmetric circle grid, for its robustness to out-of-focus scenes. E-Calib introduces an efficient reweighted least squares (eRWLS) method for feature extraction of the calibration pattern circles with sub-pixel accuracy and robustness to noise. In addition, a modified hierarchical clustering algorithm is devised to detect the calibration grid apart from the background clutter. The proposed method is tested in a variety of rigorous experiments for different event camera models, on circle grids with different geometric properties, on varying calibration trajectories and speeds, and under challenging illumination conditions. The results show that our approach outperforms the state-of-the-art in detection success rate, reprojection error, and pose estimation accuracy."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://arxiv.org/abs/2306.09078
url_code: 'https://github.com/mohammedsalah98/E_Calib'
url_dataset: 'https://github.com/mohammedsalah98/E_Calib'
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/4giQn6rt-48'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  #caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
