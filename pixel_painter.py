# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

#hehe

def pixel_painter(filename, dark_char):
    try:
        # Read the input file contents
        with open(filename, 'r') as file:
            lines = file.readlines()
        # Prepare the output filename
        output_filename = filename.split('.')[0] + '.txt'
        # Open the output file for writing
        with open(output_filename, 'w') as output_file:
            # Process each line in the CSV file
            for line in lines:
                # Convert each line to a list of integers
                run_lengths = list(map(int, line.strip().split(',')))
                row_pixels = ''
                # Alternating light (space) and dark (dark_char) pixels
                is_light = True
                for run in run_lengths:
                    if is_light:
                        row_pixels += ' ' * run # Light pixels
                    else:
                        row_pixels += dark_char * run # Dark pixels
                    is_light = not is_light # Switch between light and dark
                # Write the processed line to the output file
                output_file.write(row_pixels + '\n')
        print(f"{output_filename} created!")
    except FileNotFoundError:
        print("The file was not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    dark_char = input("Enter a character: ")
    pixel_painter(filename, dark_char)