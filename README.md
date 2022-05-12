# Pitches

## By Florence Wambui

### Description
This is an application that allows users to post, comment,like and vote for their favorite pitches as group in various categories.

### Setup Installation
##### Prequisites
- python3
- pip
- virtualenv

On the terminal:
```
git clone https://github.com/FloWambui/Pitches.git
```

```
cd Pitches
```
```
source virtual/bin/activate
```
```
pip install flask
```
```
chmod a+x start.sh
```
```
./start.sh
```
```
python3 manage.py server
```
- Open the browser and nagigate http://127.0.0.1:5000/

### Behavior Driven Development (BDD)
A new user:
- User will be able to view other peoples comments.
- User will not be able to comment untill the user registers and logs in.
- User will not be able to create a pitch until user registers and logs in.
- User will not be able to either downvote or upvote untill the user registers and logs in.

Current User:
- User will login with same credentials used to register.
- User inputs wrong credentials will be alerted.
- User inputs correct credentials, user will be logged in.
- User will be able to create a pitch.
- User will be able to views other peoples pitches.
- User will be able to comment on other peoples pitches.
- User will be able to either downvote or upvote other peoples pitches.


### Technologies Used
- HTML
- Python
- Bootstrap
- Flask

### Authors Info
Email - gflorencewambui@gmail.com