import setuptools


with open("README.md", encoding="utf8") as f:
    readme = f.read()


setuptools.setup(
    name="libertem-jupyter-proxy",
    version="0.1",
    url="",
    author="",
    license="BSD",
    description="Run LiberTEM in JupyterLab",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["Jupyter"],
    classifiers=["Framework :: Jupyter"],
    install_requires=[
        'jupyter-server-proxy',
    ],
    entry_points={
        "jupyter_serverproxy_servers": [
            "libertem = libertem_jupyter_proxy:setup_libertem",
        ]
    },
    package_data={"libertem_jupyter_proxy": ["icons/*"]},
    project_urls={},
)
