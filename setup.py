import setuptools

def _requirements():
    return ["os"]

def _test_requirements():
    return ["os"]
 
setuptools.setup(
    name="kotodama",
    version="0.0.7",
    author="Yoshiki Ohira",
    author_email="ohira.yoshiki@irl.sys.es.osaka-u.ac.jp",
    description="日本語の動詞を活用形に変換する",
    long_description="日本語の動詞に対して、過去・伝聞・様態といった活用ラベルを入力し、動詞の活用形を変換するプログラムです",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    package_data={
        'kotodama': ['data/kotodama_dic.csv'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)