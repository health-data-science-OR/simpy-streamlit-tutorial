# Change log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Dates formatted as YYYY-MM-DD as per [ISO standard](https://www.iso.org/iso-8601-date-and-time-format.html).

Consistent identifier (represents all versions, resolves to latest): [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10636002.svg)](https://doi.org/10.5281/zenodo.10636002)

## [3.0.0] Unreleased

### Changes

* Ugraded package versions in `environment.yml` to latest as of March 2026
* Upgrade Python 3.10 => 3.12
* Upgrade `treat-sim` 1.0.0 => 3.0.0

### Fixes

* Added missing `ciw` dependency from environment file to remove error on rebuild of JupyterBook site.

## [2.0.0](https://github.com/health-data-science-OR/simpy-streamlit-tutorial/releases/edit/v2.0.0)

## Changes

* Upgrade to Python 3.9 -> 3.10
* Addition of `sim-tools` examples for sampling from pre-coded distributions suitable for DES models.

## [1.2.1](https://)github.com/health-data-science-OR/simpy-streamlit-tutorial/releases/edit/v1.2.1

### Fixed:

* Fixed github action to create image on dockerhub

## v1.2.0

Minor revisions to support response to NIHR open research review (more to come. final version will be 2.0.0)

## Changes

* Deployable app on streamlit
* github action for CI dockerhub - to be tested.  Runs on release.
* test of black for `linting` as recommending by reviewer 1

## v1.1.2

### Fixes

* Updated exercise and solution for `simpy` full model example. Removed seed setting from `get_experiments()`
* Updated citation file. Removed message as it was not needed.

## v1.1.1

### Fixes

* Renamed `interactive_app.py`
* Typos in Ciw notebook
* added `resources/overview.m`d in exercise directory
* Added repo overview to `README.md`

## v1.1.0

### Changes
* Added CITATION.cff

### Fixes
* Fixed naming typo in conda env

## v1.0.0

### Changes

* swapping simpy for ciw 
* Running a batch of experiments via streamlit
* Contribution instructions

### Fixes

* Minor updates and typo fixes

## v0.2.0

HSMA 2023 release

### Added

* First draft of materials for pilot in HSMA

## v0.1.0

Iniital release

### Added:

* basic `simpy` tutorial added 
* introductory `streamlit` materials added.