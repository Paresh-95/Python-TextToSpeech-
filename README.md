# Text-to-Speech Web App

This is a simple web application built with Flask that converts text to speech. It uses the `Gtts` library to generate audio from the provided text.

## Features

- Enter text in a text area and select a voice from available voices.
- Click the "Speak" button to generate and play the audio.
- Download the generated audio as an MP3 file.

## Prerequisites

- Python 3.11
- Flask
- Gtts

## Installation

1) To Run by .EXE

    ```bash
    git clone https://github.com/Paresh-95/Python-TextToSpeech-.git
    cd your TextToSpeech GTTS
    cd EXE FILE
    run TextToSpeech.exe 


2) To Run By Installing Flask

1. Clone the repository:

```bash
git clone https://github.com/Paresh-95/Python-TextToSpeech-.git
cd your TextToSpeech GTTS

2. Create a virtual environment (recommended): (Skip For .Exe)

```bash
python -m venv venv


3.Install the required packages: (Skip For .Exe)

```bash
pip install -r requirements.txt  


Usage

4.Run the application: 

```bash 
python app.py   (Skip For .Exe)


    1.Open your web browser and navigate to http://localhost:5000/.
    2.Enter text, select a voice, and click the "Speak" button.
    3.You can download the generated audio as an MP3 file by clicking the "Download as MP3" link.


OR

cd EXE FILE
run TextToSpeech.exe 


Contributing

Contributions are welcome! Please feel free to create issues and submit pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.


### requirements.txt (Skip For .Exe)

To create a `requirements.txt` file, you can use the `pip freeze` command to list the installed packages in your virtual environment. Run the following command while your virtual environment is activated:

```bash
pip freeze > requirements.txt
