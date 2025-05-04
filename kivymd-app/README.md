# KivyMD Counter App

This project is a simple KivyMD application that features a counter. The application displays a label showing the current counter value, an image, and a bottom bar with two buttons to increment and decrement the counter. The counter value is stored in a text file, allowing it to persist between sessions.

## Project Structure

```
kivymd-app
├── main.py                # Main entry point of the application
├── screens
│   └── main_screen.kv     # Kivy language layout for the main screen
├── assets
│   └── image.png          # Image asset used in the application
├── data
│   └── counter.txt        # Stores the current value of the counter
├── requirements.txt       # Lists the dependencies required for the project
└── README.md              # Documentation for the project
```

## Requirements

To run this application, you need to have the following dependencies installed:

- Kivy
- KivyMD

You can install the required packages using pip. Create a virtual environment and run:

```
pip install -r requirements.txt
```

## Running the Application

To run the application, execute the following command in your terminal:

```
python main.py
```

Make sure you have the `counter.txt` file in the `data` directory with an initial value (e.g., `0`) before running the application.

## Usage

- The application displays the current counter value.
- Use the "Increment" button to increase the counter.
- Use the "Decrement" button to decrease the counter.
- The counter value is saved in `counter.txt` and will be loaded when the application starts.

## License

This project is open-source and available under the MIT License.