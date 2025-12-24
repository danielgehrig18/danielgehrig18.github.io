---
title: "Time Lens++: Event-based Frame Interpolation with Parametric Non-linear Flow and Multi-scale Fusion"
authors:
- Stepan Tulyakov 
- Alfredo Bochicchio
- Daniel Gehrig 
- Stamatios Georgoulis
- Yuanyou Li 
- Davide Scaramuzza
author_notes:
- "Equal contribution"
- "Equal contribution"
#date: "2015-09-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: "2022-06-19T00:00:00Z"

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ["paper-conference"]

# Publication name and optional abbreviated publication name.
publication: "*IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*"

publication_short: ""

abstract: "Recently, video frame interpolation using a combination of frame- and event-based cameras has surpassed traditional image-based methods both in terms of performance and memory efficiency. However, current methods still suffer from (i) brittle image-level fusion of complementary interpolation results, that fails in the presence of artifacts in the fused image, (ii) potentially temporally inconsistent and inefficient motion estimation procedures, that run for every inserted frame and (iii) low contrast regions that do not trigger events, and thus cause events-only motion estimation to generate artifacts. Moreover, previous methods were only tested on datasets consisting of planar and faraway scenes, which do not capture the full complexity of the real world. In this work, we address the above problems by introducing multi-scale feature-level fusion and computing one-shot non-linear inter-frame motion—which can be efficiently sampled for image warping—from events and images. We also collect the first large-scale events and frames dataset consisting of more than 100 challenging scenes with depth variations, captured with a new experimental setup based on a beamsplitter. We show that our method improves the reconstruction quality by up to 0.2 dB in terms of PSNR and up to 15% in LPIPS score."

# Summary. An optional shortened abstract.
summary: ''

tags:
- Computer Vision
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: https://rpg.ifi.uzh.ch/docs/CVPR22_Tulyakov.pdf
url_code: ''
url_dataset: 'https://github.com/uzh-rpg/timelens-pp/'
url_poster: ''
url_project: 'https://rpg.ifi.uzh.ch/TimeLens.html'
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/bWJz_p8Y5Hc'

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

{{% callout note %}}
This work appeared in [IEEE Spectrum](https://spectrum.ieee.org/video-friday-remote-control-burger-crafting), and lead to a patent with Huawei RC Zurich!

Stepan Tulyakov, Alfredo Bocicchio, Stamatios Georgoulis, Yuanyou Li, Daniel Gehrig,
Mathias Gehrig, and Davide Scaramuzza, IMAGE PROCESSING APPARATUS AND
METHOD FOR GENERATING INTERPOLATED FRAME, WO/2023/083467, Pub-
lished 19.05.2023
{{% /callout %}}
