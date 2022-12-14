import os
import shutil

from cookiecutter.main import cookiecutter


project_type = "{{ cookiecutter.project_type }}"

# Generate __tmp directory
files_before = os.listdir(".")
template_dirname = f"__cc_{project_type}"
print(
    "|" + ' "{}" template specific options '.format(project_type).center(60, "-") + "|"
)
cookiecutter(template_dirname)

files_after = os.listdir(".")
diff = sorted(list(set(files_after) - set(files_before)))
final_dirname = diff[0]
if not os.path.isdir(final_dirname) or len(diff) > 1:
    raise ValueError("Unexpected directory content:  {}".format(diff))

# Remove templates
for d in files_before:
    shutil.rmtree(d)

# Copy content and rename directory
shutil.move(final_dirname, "__cc2_tmp")  # rename temporarily
for f in os.listdir("__cc2_tmp"):
    shutil.move(os.path.join("__cc2_tmp", f), f)
os.rmdir("__cc2_tmp")

os.rename(os.path.join("..", project_type), os.path.join("..", final_dirname))
