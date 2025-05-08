# WaterTAP Project Template
A logical, reasonably standardized but flexible project structure for doing and sharing WaterTAP projects.

## Starting a new project

To start a new project, run:

```bash
watertap project
```

### The resulting directory structure

The directory structure of your new project will look something like this (depending on the settings that you choose):

```

├── components         <- For storing flowsheets of single units
│
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   ├── archive        <- Old data that isn't being used, but might be useful to keep
│   └── raw            <- The original, immutable data dump.
│
├── figures            <- Generated graphics and figures to be used in reporting
│
├── models             <- Non-WaterTAP models that can be integrated (Reaktoro, Pytorch, etc.)
│
├── notebooks          <- Jupyter notebooks. 
│
├── references         <- Data dictionaries, relevent literature, and all other explanatory materials.
│
├── results            <- Generated analysis as HTML, PDF, LaTeX, etc.
└── README.md          <- The top-level README for developers using this project.
```
