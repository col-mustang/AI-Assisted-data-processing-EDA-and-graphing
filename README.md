# AI_Course_Project_3_Team_1

## AI Assisted Data Processing, EDA, and Graphing

## Introduction

Welcome to our project repository! This project aims to create a user-friendly, web-based application that facilitates automatic generation of custom graphs for any given tabular dataset through simple voice commands or text prompts. This technology will enable users to engage with data analysis in a more intuitive and efficient manner, significantly reducing the manual effort involved in data processing. Our focus has been on machine learning and natural language processing (NLP) to achieve seamless data visualization and interaction.

## Table of Contents

- [Project Setup](#project-setup)
- [Data Collection and Cleaning](#data-collection-and-cleaning)
- [Model Implementation and Optimization](#model-implementation-and-optimization)
- [Results](#results)
- [Future Work](#future-work)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Built With
- **Visual Studio Code** - Source code editor used for development.
- **GitHub Copilot** - AI assistant that helps in writing better code.
- **ChatGPT** - AI model for generating documentation and guidance.
- **Perplexity** - AI assistant that helps generate and write cleaner code.
- **Streamlit** - Web framework tailored for data science applications, allowing Python developers to easily build and deploy web applications. Streamlit serves as the foundation for our web-based interface, ensuring a seamless user experience.

## Location of the Code and Write Up

The main file is located in the root directory of the Git repository. The file name is `Main_Page_for_Plotly.py`.

## Getting Started

Follow the steps below to get this project up and running on your local machine.
```sh
$ streamlit run "Main_Page_for_Plotly.py"
```

### Prerequisites

The following are prerequisites for this project. Instructions for pip installation are provided for each package.

- **Python** - This project was created using Python version 3.11.5. Package compatibility has not been tested with other versions of Python. Refer to this [DigitalOcean tutorial](https://www.digitalocean.com/community/tutorials/install-python-windows-10) for Python installation.

- **Streamlit**
  ```sh
  pip install streamlit
  ```

- **Streamlit Mic Recorder**
  ```sh
  pip install streamlit-mic-recorder
  ```

- **Pandas**
  ```sh
  pip install pandas
  ```

- **TensorFlow**
  ```sh
  pip install tensorflow[and-cuda]  # if using a compatible GPU
  # or
  pip install tensorflow-cpu  # if using only your CPU
  ```

- **Scikit-learn**
  ```sh
  pip install -U scikit-learn
  # Note: Scikit-learn installation encourages the use of a virtual environment. See https://scikit-learn.org/stable/install.html
  ```

- **Numpy**
  ```sh
  pip install numpy
  ```

- **Keras**
  ```sh
  # Keras will be automatically installed when you install TensorFlow.
  ```

### Installation and Running

In addition to setting up Python and the required packages, perform the following steps.

1. Clone the repository on your local machine:
   ```sh
   git clone https://github.com/DougInVentura/AI_Course_Project_3_Team_1
   ```

2. Open the folder corresponding to the app where you installed it using the repo clone above.

3. Open the file `Main_Page_for_Plotly.py`.

4. Make the desired modifications. Run cell by cell or run the entire Jupyter notebook.

## Data Collection and Cleaning

Describe the sources of your data and the methodology used to clean and preprocess it. This section includes:
- Data sources
- Key steps in data cleaning and preprocessing
- Exporting the cleaned data for modeling

## Model Implementation and Optimization

This section explains the model(s) used, including any additional libraries or technologies that were incorporated beyond the class syllabus. It covers:
- Description of the initial model setup and rationale
- Iterative improvements and optimizations made
- Final model configuration and performance metrics

## Visualizations

3D Plotting 

![3D Plot](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/168fb6df-ace1-4ece-9c68-793fab614450)

![Graph](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/c5c5dc4c-9741-4f9f-92d9-c8a9057752ae)

Streamlit Automated Graphing

![Screenshot 2024-05-22 at 7 14 32 PM](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/cc39a366-2042-444d-9eed-cf81c00da7a7)

![Screenshot 2024-05-22 at 7 14 47 PM](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/56976753-fcc9-43ad-85d0-05e84d7a527c)

![Screenshot 2024-05-22 at 7 15 18 PM](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/feb968fb-d651-49cb-a444-d6b90e534bcb)

![Screenshot 2024-05-22 at 7 15 37 PM](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/0d7264c7-1f3b-46a7-bb23-50e39ee2edff)



## Results

Summarize the model's performance and the conclusions drawn from applying the model to your data. Include key metrics that highlight the model's effectiveness.

## Future Work

Discuss potential improvements or next steps for the project if more time and resources were available. This could include:
- Exploring additional data sources
- Trying different model architectures or algorithms
- Deploying the model as a web or mobile application

## Authors

- **Chris Alvarez** - Presentation visualization, data collection, preprocessing, and application deployment
- **Doug Francis** - Feature/data engineering, model evaluation, model deployment, and documentation
- **Geoff McDaniel** - Feature/data engineering, model evaluation, and voice capture widget deployment

## License

This project is not licensed and is available for educational and non-commercial use only.

## Acknowledgments

Big shoutout to our instructor Firas, and of course, Sean, for their awesome support with our project. Our professors laid down the basics, making sure we got the hang of what we needed for Project 3. All together, they've been the dream team behind our data analysis skills, and we couldn't be more grateful.
