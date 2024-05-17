## AI_Course_Project_3_Team_1
AI Assisted data processing, EDA and graphing

## Introduction

Welcome to our project repository! This project aims to create a user-friendly, web-based application that facilitates automatic generation of custom graphs for any given tabular dataset through simple voice commands or text prompts. This technology will enable users to engage with data analysis in a more intuitive and efficient manner, significantly reducing the manual effort involved in data processing. Our focus has been on [mention the broad technology or approach used, like machine learning, NLP, etc.] to achieve [specific objectives or outcomes].

## Table of Contents

- [Project Setup](#project-setup)
- [Data Collection and Cleaning](#data-collection-and-cleaning)
- [Model Implementation and Optimization](#model-implementation-and-optimization)
- [Results](#results)
- [Future Work](#future-work)
- [Authors](#Authors)
- [Acknowledgments](#Acknowledgments)

## Built With
- Visual Studio Code - The source code editor used for development.
- GitHub Copilot - AI assistant that helps in writing better code.
- ChatGPT - AI model for generating documentation and guidance.
- Perplexity - AI assistant that helps generate and write cleaner code.
- Streamlit - Web framework is specifically tailored for data science applications, allowing Python developers to easily build and deploy web applications. Streamlit will serve as the foundation for our web-based interface, ensuring a seamless user experience.

## Location of the Code and Write Up

The file is in the root directory of the Git repository. The file name is "Main_Page_for_Plotly.py. 

## Getting Started

The steps below should get you started to get this project up and running on your local machine.
$ streamlit run "Main_Page_for_Plotly.py"

### Prerequisites

The following are prerequisites for this project. Instructions for pip installation are provided for each of the packages.

* Python - This project was created using Python version 3.11.5. Package compatability has not been tested with other versions of Python. See https://www.digitalocean.com/community/tutorials/install-python-windows-10 as a reference for Python installation.

* Stremlit
  ```sh
  pip install streamlit
  ```

* Steamlit mic recorder
  ```sh
  pip install streamlit-mic-recorder
  ```
  
* pandas 
  ```sh
  pip install pandas
  ```
* tensorflow 
  ```sh
  pip install tensorflow[and-cuda] - if using a compatable GPU

  or 

  pip install tensorflow-cpu - if using only your cpu
  ```
* sklearn 
  ```sh
  pip install -U scikit-learn
  Note: scikit-lean installation encourages the use of a virtual environment. See https://scikit-learn.org/stable/install.html
  ```
* numpy 
  ```sh
  pip install numpy
  ```
* keras 
  ```sh
  keras will be automatically installed when you install tensorflow. While it can be installed separately, it is recommended to just use the pip installation of tensor flow to install keras.
  ```

### Installation and Running

_In addition to setting up Python and the required packages, perform the following steps._

1. Clone the repository on your local machine
   ```sh
   git clone https://github.com/DougInVentura/AI_Course_Project_3_Team_1)
   ```
2. Open the folder corresponding to app where you installed in using the repo clone above.

3. Open the file "Main_Page_for_Plotly.py"

4. Make the modifications you desired. Run cell by cell or run the entire Jupyter notebook.
## Data Collection and Cleaning

Describe the sources of your data and the methodology used to clean and preprocess it. This section could include:
- Data sources
- Key steps in data cleaning and preprocessing
- Exporting the cleaned data for modeling

## Model Implementation and Optimization

This section explains the model(s) used, including any additional libraries or technologies that were incorporated beyond the class syllabus. It should cover:
- Description of the initial model setup and rationale
- Iterative improvements and optimizations made
- Final model configuration and performance metrics

## Results

Summarize the model's performance and the conclusions drawn from applying the model to your data. Include key metrics that highlight the model's effectiveness.

## Future Work

Discuss potential improvements or next steps for the project if more time and resources were available. This could include:
- Exploring additional data sources
- Trying different model architectures or algorithms
- Deploying the model as a web or mobile application

## Authors
- Chris Alvarez
- Doug Francis
- Geoff McDaniel

## License
This project is not licensed and is available for educational and non-commercial use only

## Acknowledgments
Big shoutout to our instructor Firas, and of course, Sean, for their awesome support with our project. Our profs laid down the basics, making sure we got the hang of what we needed for Project 3. All together, they've been the dream team behind our data analysis skills, and we couldn't be more grateful.
