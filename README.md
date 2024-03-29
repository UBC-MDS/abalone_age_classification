# Abalone Age Classifier

Data analysis project for DSCI 522 (Data Science workflows); a course in the Master of Data Science program at the University of British Columbia.

## Authors
- Nick Lisheng Mao
- Beilin Wu (Lynn)
- Kiran Phaterpekar
- Rakesh Pandey


## Introduction
Abalones are endangered marine snails that are found in the cold coastal water around the world. The price of an abalone is positively associated with its age. However, determining how old an abalone is a very complex process. 

In this project we are classifying abalone snails into "young" and "old" according to their number of rings based on input features such as abalone's gender, height with meat in shell, weight of the shell etc.



## About Data Set and Analysis

The Abalone data set that was used in this project was sourced from the UC Irvine Machine Learning Repository published in 1995. It can be found <a href="https://archive.ics.uci.edu/ml/datasets/abalone" >here</a>. Each row in the data set represents the attributes and physical measurements of abalones including number of rings, sex, length, diameter, height, weight, etc. The number of rings were counted manually using a microscope by the researchers. The age of an abalone is represented by its number of rings plus 1.5 as number of years lived. The data set has already removed its missing values and the range of the continuous values have been scaled for use with an ANN (by dividing by 200).

The `Sex` column in this dataset includes three categories: `Female`, `Male` and `Infant`. Abalone of different sex has different body composition with distinct economic values. Harvesting an infant abalone may cause endangered crisis to the population. 

In the research paper "A Quantitative Comparison of Dystal and Backpropagation" that David Clark, Zoltan Schreter and Anthony Adams submitted to the Australian Conference on Neural Networks (ACNN'96), the original abalone data set was treated as a 3-category classification problem (grouping ring classes 1-8, 9 and 10, and 11 on). In our project, we will treat the data set as a 2-categorical classification problem (grouping ring classes less or equal to 11, and more than 11).

Here, we aim to answer one research question with a Logistic Regression classification model:

**Given the input features including sex, size and weight, is an abalone young (i.e. number of rings smaller than or equal to 11), or old (i.e. number of rings is larger than 11)?**

To perform this analysis, first, after the data download we split the data into train set and test set and perform data wrangling that includes creating the “Is Old” target variable that identifies an abalone’s age. We then perform EDA on the training data to investigate the relationships across the independent variables, as well as differences between young and old abalones. Next, since we are dealing with a binary classification problem, we decide to fit a Logistic Regression model on the data set. In this project, we choose Logistic Regression model since it is easier to implement, interpret, and very efficient to train when compared to other models. Due to limited time span of this project, we will not be testing the data with other models. Before we fit the model, we preprocess the data including scaling the numerical features and one-hot-encoding the categorical feature. When fitting a Logistic Regression model to classify the abalone ages, we use random search cross validation to find the best performing hyperparameter and evaluate the best performing model on the test set on various scores. We also examine the feature importance by looking at their coefficients in the logistic model. The final step of this project is creating a Jupyter Book report that shares the analysis results.

As a result, with hyperparameter tuning on the Logistic Regression model, we found that the best model fit is when C = 100. The final model achieved a F1 score of 90% and a recall of 95% on the test set. Through investigating the feature importances from their coefficients, we discovered that the shucked_weight and if the abalone is infant is most positively correlated with abalone being young and if the whole weight is most negatively correlated.


## Report

The final report can be found [here](https://ubc-mds.github.io/abalone_age_classification/Project_report_milestone2.html).

## Usage

### Option 1: Using `docker`

To run this analysis using Docker, clone/download this repository, use the command line to navigate to the root of this project on your computer, and then type the following (filling in PATH_ON_YOUR_COMPUTER with the absolute path to the root of this project on your computer).

```bash
# Clean output directories and results
docker run --rm -v /$(pwd):/home/abalone veerupandey/abalone_age_classification make -C /home/abalone clean

# Run the Analysis
# Flag `--it` is here for a purpose
docker run --rm -it -p 8000:8000 -v /$(pwd):/home/abalone veerupandey/abalone_age_classification make -C /home/abalone all
```

As a simple python webserver will be started at port 8000 to serve analysis html web page, flag `-it` will help to debug and close the session. Docker can also run in detach mode with flag `-d`.

```bash
docker run --rm -d -p 8000:8000 -v /$(pwd):/home/abalone veerupandey/abalone_age_classification make -C /home/abalone all
```

Report can be accessed in local machine by accessing [http://localhost:8000](http://localhost:8000) in any of the modern web browser.

### Option 2: Using `make`

#### Create project environment

Project `python` environment needs to be created before running the analysis. Run the command mentioned below from project root directory.

```bash
make create_env
conda activate abalone
```

**Note:** If you are on Windows, you might have to run following commands to make the `altair` and `altair_saver` work as expected.

```bash
npm install -g vega vega-cli vega-lite canvas
```

#### Run analysis end to end

To run the analysis end to end, run the following commands in a Terminal/Command Prompt from the project root directory.

```bash
make clean # to clean the analysis output files

make all # to reproduce the analysis end to end
```

`make all` publishes the report on localhost. Report can be accessed in local machine by accessing [http://localhost:8000](http://localhost:8000) in any of the modern web browser.

In case report has to be published to git pages, following command should be used in defiance of `make all`.

```bash
make clean # to clean the analysis output files

make all_git_publish # to reproduce the analysis end to end and publish to git pages
```

Individual steps can also be executed using `make` command. For example - following command runs `data_download.py` script and save the output file to disk. To see all the targets/steps, please refer the `Makefile`.

```bash
make data/raw/abalone.data
```

Please clean the target directories before invoking `make` command. `make clean` can be used to clean all the intermediate files and results.

### Option 3: Using `runner.sh` 

Python environment must be created and activated before running `runner.sh`. To create the environment, use the following command.

```bash
conda env create -f environment.yml
conda activate abalone
```

To run the analysis end to end, run the script `runner.sh` in a Terminal/Command Prompt from the project root directory as follows. Script `runner.sh` runs each individual script one at a time.

```bash
nohup bash runner.sh > runner.log &
```

Log file `runner.log` logs all the steps and can be used for debugging the script.

## Flow Chart 

![Flowchart](images/flowchart.png)

## Project Structure

![Project Structure](images/project_org.png)

## Dependencies

A environment file `environment.yml` of dependencies can be found <a href="https://github.com/UBC-MDS/abalone_age_classification/blob/main/environment.yml">here</a>. As project develops, this `yaml` file is subjected to change.

## Explanatory Data Analysis

A detailed EDA report can be found <a href="https://github.com/UBC-MDS/abalone_age_classification/blob/main/src/eda/eda.ipynb" >here</a>.

## License

This dataset is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) license. This allows for the sharing and adaptation of the datasets for any purpose, provided that the appropriate credit is given.


## References

- Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

- Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994) "The Population Biology of Abalone (Haliotis species) in Tasmania. I. Blacklip Abalone (H. rubra) from the North Coast and Islands of Bass Strait", Sea Fisheries Division, Technical Report No. 48 (ISSN 1034-3288)

- David Clark, Zoltan Schreter, Anthony Adams "A Quantitative Comparison of Dystal and Backpropagation", Australian Conference on Neural Networks (ACNN'96)

- Under Southern Seas: The Ecology of Australia's Rocky Reefs. (1999). United States: UNSW Press.

- Python Software Foundation. Python Language Reference, version 2.7. Available at http://www.python.org

- RStudio Team (2020). RStudio: Integrated Development for R. RStudio, PBC, Boston, MA URL http://www.rstudio.com/.
