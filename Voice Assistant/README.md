# Virtual Assistant using AI

  In this project, we are developing a Virtual Assistant system for desktops that is aiming towards the fast and easy daily life usage, helping users to the fullest.

Features of the project:  
→ Launching apps with facial recognition security.  
→ Sending mails through voice commands.  
→ Make yourself up to date with top news, weather forecast etc.  
→ Opening websites and getting information about specific topics.  

## Requirements

1. Python 3.9
2. Microsoft Visual C++ redistributable (latest supported version)

## Installation

### Step 1: Clone Repository

Clone repo using this [link](https://github.com/JaiminRana01/VirtualAssistant-AIProject.git).

### Step 2: Set up the virtual environment.

To install libraries required for this project, you have to set up a new virtual environment.

#### Steps to install virtual environment module and set up a new virtual environment:

Open the terminal.

##### Installing the virtualenv package with pip:
```bash
pip install virtualenv
```

##### Creating a virtual environment:

Go to your **project’s directory in terminal** and run venv:
```bash
python -m venv env
```

##### Activating a virtual environment:
```bash
.\env\Scripts\activate
```

You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory.
```bash
where python
```

### Step 3: Installing Packages
You need to install all the required packages for this project. There is a requirements.txt file present in the project directory which consists of all the required package names and their version.

You have to install all the packages using this command:
```bash
pip install -r requirements.txt
```

You can check if all the packages are installed or not by this command:
```bash
pip list
```
## Usage
Run the main.py file from the project’s directory.

At first, The assistant will ask you to input Your Name and Email Address. Type in the information and you’re good to go.

Then, it will show **“say something...”**. Mic will be turned on and you can give voice commands now.

### Launch Apps
When a user gives a voice command to launch an app, the assistant will open the webcam for face recognition and if the user’s face is identified, it will launch that app.

#### Steps to add you face data for recognition:

##### 1. Give voice command
```
data set create
```

The assistant will turn your webcam on and will start capturing your face.

You have to keep your face in the frame. It will take 100 image samples and will save them in the Data/user/face directory in your project.

##### 2. Give voice command:
```
train model
```
The model will be trained using this face data (100 image samples).

#### To add the apps you want to launch:
→ In the **main.py** file, you have to add the app name and its file path in the dictionary (dict_app) (on Line 46). So that you can launch the app you want.

```python
if re.search("launch", res):

dict_app = {
'chrome': 'C:\Program Files\Google\Chrome\Application\chrome.exe',
}
```

Format:
```python
'app_name' : 'filepath_of_the_app'
```

  

#### When you want to launch any app, you have to give this voice command:
```
Launch <app_name>
```
The assistant will open the webcam and will analyse your face.

If your face is identified, it will launch that app.

### Send Email

When you want to send an email using this assistant, it will take text, voice input and will send the email.

**TEXT INPUT:**
```
User’s email ID and password,
Recipient’s email ID
```

**VOICE INPUT:**
```
Subject,
Body
```
After giving correct input, mail will be sent without opening any email client.

### Giving latest News
It will show and tell the latest news of today’s date as a voice output.

Voice command:
```
News
```

### Giving information about weather forecast:
it will show and tell the weather forecast as a voice output.

Voice command:
```
weather in <city>
```

### Getting information from Wikipedia:
When a user wants to search for anything, it will read the first 500 characters from the Wikipedia page and return them as a string in a well organized way.

Voice command:
```
tell me about <topic>
```

### Open any website:
It will open a website in your default browser according to voice input.

Voice command:
```
open <website domain>
```