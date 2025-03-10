# Code-Bender : AI-Assisted Online Code Editor

## Overview ✨
Code-Bender is a web-based code editor built with Django and CodeMirror that allows users to write, edit, execute and save code in various programming languages. 
It provides users with an easy-to-use interface to code in several languages, with AI Assistance.
One Stop Platform for all coders to write code in different programming languages and to save their codes, all in a single online platform!

## Features ⚙️
- **Multi-language Support**
  Currently we provide support for 5 major programming languages.
  - Python
  - JavaScript
  - C
  - C++
  - Java

- **Theme Customization**
  Several themes and modes(Dark/Light) available for customization.

- **Code Execution**
  - Real-time code execution using RapidAPI's Code Compiler
  - Output display
  - Error handling

- **AI Assistance**
  - Real Time Code Generation.
  - Code Debugging and Error Identification.
  - Solving General Programming Queries using AI.

- **Sidebar Functionality**
  - Toggleable sidebar
  - AI Assistance
  - Separate output display
  - Scrollable content
  - Clean and sleek UI
 
- **User Profiles and database**
  - Ability to Save Code
  - One Stop platform to write and save all your codes
  - Retreive code as and when desirable

## Tech Stack 🤖
- Backend: Django
- Frontend: HTML, CSS, JavaScript
- LightWeight Code Editor: CodeMirror
- Code Execution: RapidAPI Code Compiler
- AI Assistance: Google Gemini API
- Additional Libraries: requests

## Installation 🖥️

1. Clone the repository:
```bash
git clone https://github.com/anantmahambrey/AI-Assisted-Code-Editor.git
cd code_editor
```

2. Install required packages:
```bash
pip install django requests google.generativeai
```

3. Apply migrations:
```bash
python manage.py migrate
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Visit `http://localhost:8000` in your browser to view code-bender

## Usage 🪴

### Code Editor
1. Select your preferred programming language from the dropdown
2. Choose a theme and mode and font-size if desired
3. Enter Code Title
4. Write your code in the editor
5. Click "Run Code" to execute
6. View output below the editor
7. Save your code for future reference

### Sidebar
1. Click "Ask AI" to show/hide the sidebar
2. Enter your doubt/problem
3. Click "Generate" to process the text
4. View results in the scrollable output area

### User profile
1. Click Your Username on the top left corner to view your user profile
2. Check all your previously saved codes
3. Click on "view" to view the code
4. Can read, copy and retreive the code as desired
5. Click on "delete" to delete the code

## Acknowledgments 😀
- CodeMirror for the text editor
- Google Gemini API for the AI Assistance
- RapidAPI for code execution
- Django community for the framework
- Contributors and testers

##### Let's get coding!✔️
