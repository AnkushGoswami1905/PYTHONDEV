# Create two virtual environments, install few packages in the first one. How do you 
# create a similar environment in the second one? 

'''

# # 1.>Creating virtual env-

# cd C:\PYTHONDEV\PRACTICE_SET_13
# python -m venv C:\PYTHONDEV\PRACTICE_SET_13\env1
# python -m venv C:\PYTHONDEV\PRACTICE_SET_13\env2

# # 2.>Activating an env and installing module and deactivating them-

# Activate the Virtual Environment- .\env1\scripts\activate
# Install Packages- pip install panda
# Deactivate the Virtual Environment- deactivate

# # 3.>Freeze the installed packages to a requirements file- 
                 
# Activate the Virtual Environment- .\env1\scripts\activate
# Freeze the installed packages to a requirements file- pip freeze > requirements.txt
# Deactivate the Virtual Environment- deactivate

# # 4.>Install the same packages on diff env using the requirements file-

# Activate the second Virtual Environment- .\env2\scripts\activate.ps1
# Install the same packages using the requirements file- pip install -r .\requirements.txt
# Deactivate the second virtual environmen- deactivate

'''