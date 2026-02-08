import sys
from pathlib import Path

# Get sys.argv variables and validate 
input_file = sys.argv[1]
output_filepath_filename = sys.argv[2] # Must split off filename for input in kml

def validate_input_file(input_file: str):
    path = Path(input_file)
    try:
        pass

    except Exception as e:
        print(e)