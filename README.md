# Speech-To-Text

## **Demo**

[![Nice](https://img.youtube.com/vi/6ggAcNcVgtU/0.jpg)](https://www.youtube.com/watch?v=6ggAcNcVgtU)

Click the picture to get the video demo


This is a project that allows user to record their speech, and then it 
automatically converts it to text, then translate the text to the given language.
I created this project because coming from a family that doesn't speak english, my family often doesn't 
communicate well with people speaking english. I created this app in hope to assist their transition
of using english to communicate. Although this app is definitely not perfect, but I learned a lot of
libraries related to speech-to-text. Also, I utilized Kivy framework to create an app, which is really fun 
in the process too.

## Usage

To run the program:
```
python main.py
```
Then press the button called record then start speaking.

<!-- I don't know how you would do this. See my other PR -->
If you don't want to run the app run the method 
```console
if __name__ == 'other':
```
and start speaking. Press the keyboard letter 'r' when you are done speaking.


## **Dependencies**
* Google Trans
* Keyboard
* Kivy
* Numpy
* Scipy
* Sound Device
* Sound File
* SpeechRecognition

## **Installation**
After you cloned the respository, you use command line to reach your 
directory of this project and then type
```console
pip3 install -r requirements.txt
```



## **Future Possible Functionalities**
* Add a timer so the user know when the recording will end
* Create a better UI 
* Allow custom duration of recording instead of constant recording


## **Contact**
For any bugs and advices, contact me at
**yaowenc2@illinois.edu**.

Special thanks to [Terry Kim](https://github.com/terrykim1211) for debugging some bugs for this project

## **Licence**
Released under the [MIT License](https://github.com/jonschlinkert/update-copyright/blob/master/LICENSE).
