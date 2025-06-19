# ZAI Project

## Overview
ZAI is a conversational AI application that utilizes the ElevenLabs API to facilitate interactive conversations between users and an AI agent. The application is designed to manage conversation sessions, handle user inputs, and provide responses from the AI agent.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd ZAI
   ```

2. **Create a Virtual Environment**
   It is recommended to create a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required packages using pip.
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the root directory and add the following variables:
   ```
   AGENT_ID=<your_agent_id>
   ELEVENLABS_API_KEY=<your_api_key>
   ```

## Usage
To run the application, execute the following command:
```bash
python src/main.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.