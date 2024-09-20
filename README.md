# 3D ASCII Earth

This project creates a rotating 3D representation of the Earth in ASCII, using Python and Pygame.

## Project Contents

The project is divided into 5 parts, each part including the functionalities of the previous parts:

1. `code_00.py`: Basic Pygame setup
2. `code_01.py`: Addition of Projection and Object classes
3. `code_02.py`: Implementation of 3D rotation
4. `code_03.py`: Creation of the sphere
5. `code_04.py`: Addition of ASCII characters to represent the Earth

The complete and final code can be found in `code_04.py`.

## Prerequisites

- Python 3.x
- Pygame
- NumPy

## Installation

1. Ensure you have Python installed on your system.
2. Create a virtual environment:
   ```
   python -m venv env
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source env/bin/activate
     ```
4. Install the necessary dependencies:
   ```
   pip install pygame numpy
   ```

## Usage

1. Clone this repository or download the files.
2. Make sure you have the `earth_W140_H35.txt` file in the same directory as the Python scripts.
3. Run the script of your choice. For example, to run the final version:
   ```
   python code_04.py
   ```

## Features

- Display of a 3D sphere representing the Earth
- Continuous rotation of the sphere
- Representation of the Earth's surface with ASCII characters

## Customization

You can adjust the following parameters in `code_04.py`:

- `WIDTH`, `HEIGHT`: Window dimensions
- `R`: Sphere radius
- `MAP_WIDTH`, `MAP_HEIGHT`: ASCII map dimensions
- `FPS`: Refresh rate

## Note

This project is an educational demonstration and can be used as a basis for more complex 3D ASCII visualization projects.



git clone https://github.com/Schosmiel/3D-ASCII-Earth.git

