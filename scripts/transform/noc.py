# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: active,-all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # NOC Codes
#
# This portion of code is meant to define and describe design decisions relating to the NOC code dimension table, as well as its subdimensions.
#
# To begin with, we'll need to define the root of the project, as scattered `ipynb` files create something of an incoherent workspace. As this project is an application, jupyter functionally operates both as a way for me to define the project, document it, and play with the data live.

# %%
import pandas as pd
import numpy as np
from pathlib import Path

def find_root(markers=(".git", "requirements.txt")):
    here = Path.cwd().resolve()
    for p in [here, *here.parents]:
        if any((p / m).exists() for m in markers):
            return p
    raise FileNotFoundError("Project root not found.")

ROOT = find_root()


# %% [markdown]
# As such, each call to data needs to be built from this file global.
#
# ## Object Definition
#
# I essentially want to create the following model for noc information.
#
# ```mermaid
# erDiagram
#     NocGroups {
#         int nocgroup_id PK
#         string name
#     }
# ```

# %%
class Noc:
    """
    Represents NOC in a snowflake schema. Transforms the csv into the
    dimension and its outrigger tables before loading.
    """
    def __init__(self, file: str):
        self.level_ot: set[int] = set()
        self._raw_data = pd.read_csv(file)

    def __parse_file(self, file):
        """Parses the file """
        df = pd.read_csv(file)
    
        return df

# %% [markdown]
# We want to see headers and then we can dive into data in different columns.

# %% active="ipynb"
# noc = Noc(ROOT / "data" / "noc_2021_version_1.0_-_classification_structure.csv")

# %% active="ipynb"
# noc._raw_data.columns

# %% [markdown]
# So to 
