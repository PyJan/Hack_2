"""main script to run code for different purposes"""

import argparse
import subprocess
import pathlib

def main():
    """main func, usage: python run.py --runtype build; python run.py --runtype streamlit etc."""
    parser = argparse.ArgumentParser(description='Process various run types')
    choices = ['build', 'streamlit', 'test_backend', 'test_usecases', 'test_db',
               'update_db']
    parser.add_argument('--runtype', choices=choices, help=f'Select run type from {choices}', required=True)
    args = parser.parse_args()

    match args.runtype:
        case 'build':
            subprocess.run("conda env update --name ai_whisperers_env --file environment.yml --prune", shell=True)
            print('Environment updated')
        case 'streamlit':
            subprocess.run(r"streamlit run  C:\Users\jansv\IdeaProjects\Hack_2\hackathon_day\project_structure\front_end\run_ui.py", shell=True)
        case 'test_backend':
            print('in test backend')
        case 'test_usecases':
            print('in use cases')
        case 'test_db':
            print('in test db')
        case 'update_db':
            print('in update db')


if __name__ == '__main__':
    main()