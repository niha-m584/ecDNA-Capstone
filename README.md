# TODO: PUT PROJECT TITLE HERE 
This contains the code for a chromosome segmentation tool.

## Directory

| File      | Description |
| ----------- | ----------- |
| config.ini      | Configuration file to set parameters       |
| environment.yml   | File to create the environment        |



| Folder      | Description |
| ----------- | ----------- |
| sample      | Folder containing sample images to use with our project       |
| src   | Contains our Python scripts        |

## Installation
To get started, run the following code to create the environment.

```
git clone 
cd ecDNA-Capstone
conda env create -f environment.yml
conda activate cap
```

## Image Specifications
Input folder will only read .tif files

## Instructions
1. Change the config.ini file to your own file path
2. Run chromosome.py
3. Annotated images will show up under annotated/filename/a_filename.tif
4. output.csv contains info in the format of filename, number of chromosomes
