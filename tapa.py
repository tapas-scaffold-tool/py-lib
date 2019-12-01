import os

from tapas.tools import prompt_bool, download_file, init_git_repo, prompt_str


# Require from user to enter parameters in this function
def ask():
    prompt_str('module_name', prompt_string="Enter module name: ")
    prompt_bool('git', default_value="y", prompt_string="Init git repository? [Y/n]: ")
    prompt_bool('gitignore', default_value="y", prompt_string="Create python .gitignore file? [Y/n]: ")
    prompt_bool('readme', default_value="y", prompt_string="Create README.md file? [Y/n]: ")
    prompt_bool('travis', default_value="y", prompt_string="Create .travis.yml file? [Y/n]: ")


# Perform additional actions after generation in this function
def post_init(
        git: bool,
        gitignore: bool,
        readme: bool,
        travis: bool,
):
    if gitignore:
        download_file('https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore', '.gitignore')

    if not readme:
        os.remove('README.md')

    if not travis:
        os.remove('.travis.yml')

    if git:
        init_git_repo()
