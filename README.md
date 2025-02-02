# Code-Bender : AI-Assisted Online Code Editor

## Overview ✨
Code-Bender is a web-based code editor built with Django and CodeMirror that allows users to write, edit, and execute code in various programming languages. 
It provides users with an easy-to-use interface to code in several languages, with AI Assistance.

## Features ⚙️
- **Multi-language Support**
  - Python
  - JavaScript
  - C
  - C++
  - Java

- **Theme Customization**
  Several themes and modes available for customization.

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

## Tech Stack 🤖
- Backend: Django
- Frontend: HTML, CSS, JavaScript
- Code Editor: CodeMirror
- Code Execution: RapidAPI Code Compiler
- AI Assistance: Google Gemini API
- Additional Libraries: requests

## Installation 🖥️

1. Clone the repository:
```bash
git clone https://github.com/anantmahambrey/AI-Assisted-Code-Editor
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

5. Visit `http://localhost:8000` in your browser

## Usage 🪴

### Code Editor
1. Select your preferred programming language from the dropdown
2. Choose a theme and mode if desired
3. Write your code in the editor
4. Click "Run Code" to execute
5. View output below the editor

### Sidebar
1. Click "Ask AI" to show/hide the sidebar
2. Enter your doubt/problem
3. Click "Generate" to process the text
4. View results in the scrollable output area

## Troubleshooting

### Common Issues
1. **API Connection Failed**
   - Check your internet connection
   - Verify API key is correct
   - Ensure RapidAPI subscription is active

2. **Code Execution Errors**
   - Check console for error messages
   - Verify code syntax
   - Check language selection

3. **Sidebar Issues**
   - Clear browser cache
   - Check for JavaScript console errors
   - Verify CSRF token is present
  

## Acknowledgments 😀
- CodeMirror for the text editor
- Google Gemini API for the AI Assistance
- RapidAPI for code execution
- Django community for the framework
- Contributors and testers
