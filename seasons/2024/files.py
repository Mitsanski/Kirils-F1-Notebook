import os

# Define the range of file numbers
start = 10
end = 24

# Read the content of the template file
with open('template.html', 'r') as template_file:
    template_content = template_file.read()

# Create new files based on the template
for i in range(start, end + 1):
    new_file_name = f'round{i}.html'
    with open(new_file_name, 'w') as new_file:
        new_file.write(template_content)

print(f"Files round{start}.html to round{end}.html have been created based on template.html.")
