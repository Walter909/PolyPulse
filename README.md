### `Project Structure`

JavaScript/TypeScript is the "default" for HTML/CSS projects, but is quite verbose and boilerplate-heavy.
For faster development, we will use Python as the backend.

NodeJS will communicate with the Python backend via HTTP calls to transfer data back and forth.

### `Setup`

1. Clone repository locally
2. **Start Python Backend**
   - Open new terminal
   - Navigate to `Backend/` directory
   - Make sure to create a .env file and add your api key at the top of the line for example: API_KEY="CHAT_GPT_KEY"
   - Run `app.py` to start the Python backend
3. **Start Frontend**
   - Open new terminal
   - Navigate to `/Frontend` project home directory, if not already there
   - Run `npm start` to start Node server; changes will automatically restart Node
4. Open `http://localhost:3000/` in your browser to view app
