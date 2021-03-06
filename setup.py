import setuptools
from glob import glob
import os
def main():
    setuptools.setup(
        name="gitpuller_wrapper",
        version='0.0.0',
        url="",
        author="Alex Tennant",
        description="Cute little wrapper for nbgitpuller so you can just paste URLs and get stuff on your hub",
        packages=setuptools.find_packages(),
        install_requires=[
            'notebook',
            'nbgitpuller',
        ],
        data_files=[
            (
                'share/jupyter/nbextensions/gitpuller_wrapper', 
                 glob('gitpuller_wrapper/static/*'))
            ,
            (
                'etc/jupyter/jupyter_notebook_config.d', 
                ['gitpuller_wrapper/etc/serverextension.json']
            ),
            (
                'etc/jupyter/nbconfig/notebook.d', 
                ['gitpuller_wrapper/etc/nbextension.json']
            )
        ],
        zip_safe=False,
        include_package_data=True
    )

if __name__ == '__main__':
    main()
    # TODO: Do this in like a pip wheel or someting? I think this might be
    # what we call "bad practice" 
    os.system("jupyter serverextension enable --py gitpuller_wrapper")
    os.system("jupyter nbextension install --py gitpuller_wrapper --user")
    os.system("jupyter nbextension enable --py gitpuller_wrapper --user")