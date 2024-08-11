'''1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?'''

# steps:

# 1) Open terminal

# 2) Create env1 -> virtualenv env1
# 3) Create env2 -> virtualenv env2

# 4) activate any environment -> .\env1\Scripts\activate.ps1

# 5) pip install some packages -> pip install pandas ,pyjokes

# 6)create requirements.txt file -> pip freeze > requirements.txt

# now re install all env1 pckages in env2

# 1) deactivate env1
# 2) activate env2 -> .\env2\Scripts\activate.ps1
# 3) pip install -r .\requirements.txt