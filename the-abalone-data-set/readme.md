[![Functional?](https://img.shields.io/badge/Functional%3F-no-red.svg)](https://shields.io/)

# [Machine Learning] The Abalone Dataset

Predicting the age of abalone from physical measurements. The age of abalone is determined by cutting the shell through
the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other
measurements, which are easier to obtain, are used to predict the age. Further information, such as weather patterns and
location (hence food availability) may be required to solve the problem.

From the original data examples with missing values were removed (the majority having the predicted value missing), and
the ranges of the continuous values have been scaled for use with an ANN (by dividing by 200).

## Attribute Information
Given is the attribute name, attribute type, the measurement unit and a brief description. The number of rings is the
value to predict: either as a continuous value or as a classification problem.

### Source
Data comes from an original (non-machine-learning) study:
Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994)
"The Population Biology of Abalone (_Haliotis_ species) in Tasmania. I. Blacklip Abalone (_H. rubra_) from the North Coast and Islands of Bass Strait",
Sea Fisheries Division, Technical Report No. 48 (ISSN 1034-3288)

### Original Owners of Database:

Marine Resources Division
Marine Research Laboratories - Taroona
Department of Primary Industry and Fisheries, Tasmania
GPO Box 619F, Hobart, Tasmania 7001, Australia
(contact: Warwick Nash +61 02 277277, wnash '@' dpi.tas.gov.au)

### Donor of Database:

Sam Waugh (Sam.Waugh '@' cs.utas.edu.au)
Department of Computer Science, University of Tasmania
GPO Box 252C, Hobart, Tasmania 7001, Australia

Source: https://archive.ics.uci.edu/ml/datasets/abalone