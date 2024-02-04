
import os

# os.mkdir('file_dir/test_dir')  # make directory

# os.rmdir('file_dir/test_dir')
# os.rmdir('file_dir')

main_dir = '/1_module_python/topic9_2/data'
filenames = os.listdir(main_dir)

for filename in filenames:
    file_path = os.path.join(main_dir, filename)
    print(file_path)
    os.remove(file_path)

os.rmdir(main_dir)


# open('test.py', 'w')