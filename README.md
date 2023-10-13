[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/health-data-science-OR/simpy-streamlit-tutorial/HEAD)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Read the Docs](https://readthedocs.org/projects/pip/badge/?version=latest)](https://health-data-science-or.github.io/simpy-streamlit-tutorial)
[![License: MIT](https://img.shields.io/badge/ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037)
[![License: MIT](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)


# Improving the usability of open health service delivery simulation models using python and web apps

## Overview

The materials and methods in this repository support health service researchers learning to use `simpy` and `streamlit` to build open discrete-event simulation models.  The models are sharable with other researchers and the NHS.

## Author ORCIDs

[![ORCID: Harper](https://img.shields.io/badge/ORCID-0000--0001--5274--5037-brightgreen)](https://orcid.org/0000-0001-5274-5037)
[![ORCID: Monks](https://img.shields.io/badge/ORCID-0000--0003--2631--4481-brightgreen)](https://orcid.org/0000-0003-2631-4481)

## Dependencies

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)

All dependencies can be found in [`binder/environment.yml`]() and are pulled from conda-forge.  To run the code locally, we recommend install [mini-conda](https://docs.conda.io/en/latest/miniconda.html); navigating your terminal (or cmd prompt) to the directory containing the repo and issuing the following command:

> `conda env create -f binder/environment.yml`

**Online Alternatives**:

[![Read the Docs](https://readthedocs.org/projects/pip/badge/?version=latest)](https://health-data-science-or.github.io/simpy-streamlit-tutorial)

* Visit our [jupyter book](https://health-data-science-or.github.io/simpy-streamlit-tutorial) for interactive code and explanatory text
* Run out Jupyter notebooks in binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/health-data-science-OR/simpy-streamlit-tutorial/HEAD)

## Citation

**If you use the work contained in the repository for your research or job then a citation would be very welcome when you write up.**

### Citing the journal article

We have a [journal article](https://openresearch.nihr.ac.uk/articles/3-48) that accompanies this repo published in NIHR open research: https://openresearch.nihr.ac.uk/articles/3-48

>  Monks T and Harper A. Improving the usability of open health service delivery simulation models using Python and web apps [version 1; peer review: 1 approved, 1 approved with reservations]. NIHR Open Res 2023, 3:48 (https://doi.org/10.3310/nihropenres.13467.1) 

```bibtex
@article{monksharper2023improving,
  title={Improving the usability of open health service delivery simulation models using Python and web apps},
  author={Monks, Tom and Harper, Andrew},
  journal={NIHR Open Research},
  volume={3},
  pages={48},
  year={2023},
  doi={10.3310/nihropenres.13467.1},
  url={https://doi.org/10.3310/nihropenres.13467.1},
  note={Version 1; Peer Review: 1 Approved, 1 Approved with Reservations}
}

```
### Citing the code

Please cite the code and work in this repository as follows:

> Monks, Thomas, & Harper, Alison. (2023). SimPy and StreamLit Tutorial Materials for Healthcare Discrete-Event Simulation (v1.1.2). Zenodo. https://doi.org/10.5281/zenodo.8193001


```bibtex
@software{monks_thomas_2023_8193001,
  author       = {Monks, Thomas and
                  Harper, Alison},
  title        = {{SimPy and StreamLit Tutorial Materials for 
                   Healthcare Discrete-Event Simulation}},
  month        = jul,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v1.1.2},
  doi          = {10.5281/zenodo.8193001},
  url          = {https://doi.org/10.5281/zenodo.8193001}
}
```

## Repo Overview

```
.
├── binder
│   └── environment.yml
├── CITATION.cff
├── _config.yml
├── content
│   ├── 01_setup
│   ├── 02_simpy
│   ├── 03_streamlit
│   ├── 04_exercises
│   ├── 05_solutions
│   └── front_page.md
├── imgs
├── LICENSE
├── main.py
├── README.md
└── _toc.yml

```


* `binder` - contains the environment.yml file (sim) and all dependencies managed via conda
* `_config.yml` - configuration of our Jupyter Book
* `content` - the notebooks and markdown arranged by setup, simpy, streamlit, exercises, and solutions.
* `data` - directory containing data files used by analysis notebooks. 
* `imgs` - all image files used in the tutorial material
* `LICENSE` - details of the MIT permissive license of this work.
* `main.py` - an example simpy model to use to test the virtual environment 
* `README` - what you are reading now!
* `_toc.yml` - the table of contents for our Jupyter Book.