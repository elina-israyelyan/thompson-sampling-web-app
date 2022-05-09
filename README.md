# thompson-sampling-web-app

A tool for marketeers to input data, define KPI-s and receive analysis on the best reward-giving
advertisement based on Thompson Sampling approach.

### What is this repository for? ###

* To run the thompson sampling algorithm on a given data to understand which advertisement will provide the maximum
  reward.
* Create a web application that will make the tool easily accessible and will provide different features along with the
  algorithm.

*** Note *** \
All the features mentioned above are working with dummy variables as the thompson algorithm will only consider beta
distribution.

### Who do I talk to if any questions ? ###

You can email to one of the contributors of this git repository: \
[Elina Israyelyan](elina_israyelyan@edu.aua.am) \
[Armine Papikyan](armine_papikyan@edu.aua.am ) \
[Davit Nazlukhanyan](david_nazlukhanyan@edu.aua.am) \
[Awadis Shikoyan](awadis_shikoyan@edu.aua.am)

# Getting Started

### Environment setup

Before getting to the application we need to set up the environment.
Run the following command to create a virtual environment.

```bash
conda create -n 'thompson_sampling_web' python=3.8
conda activate thompson_sampling_web
```

To install the dependencies run the following command.

```bash
pip install -r requirements.txt
```

As all the imports in the code are done from source `thompson_web_app` directory, you should include this in PYTHONPATH.
You can do it with the following command if it is linux environment.

```bash
export PYTHONPATH='thompson_web_app'
```

For windows

```bash
set PYTHONPATH='thompson_web_app'
```

Finally, you should define environmental variables for the app to run.

```bash
export PORT={the port you want the app to run on}
```

For windows

```bash
set PORT={the port you want the app to run on}
```

### Running the app

After setting up the environment you can run the application by running the `thompson_web_app/app/app.py` python file
with the following command.

```bash
python thompson_web_app/app/app.py
```

You can see the application running on  http://127.0.0.1:8050/homepage \
Also, you can check the working app on https://find-your-reward.herokuapp.com/homepage