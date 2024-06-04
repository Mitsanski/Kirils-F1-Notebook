import os

# Define the number of files and template name
num_files = 24
template = "round*.html"

# Get the current working directory
cwd = os.getcwd()

# Loop through the number of files
for i in range(1, num_files + 1):
    # Create the filename with zero-padding for numbering
    filename = f"round{i:02d}.html"
    # Create the full path
    filepath = os.path.join(cwd, filename)

    # Open the file in write mode (will create if non-existent)
    with open(filepath, "w") as f:
        # Write an empty template content (you can add content here)
        f.write("")

print(f"Created {num_files} files with template '{template}' in {cwd}")
