import setuptools
 
setuptools.setup(
    name="kotodama",
    version="1.0",
    author="tennmoku71",
    author_email="tennmoku71@gmail.com",
    description="日本語の動詞を活用形に変換する",
    long_description="日本語の動詞に対して、過去・伝聞・様態といった活用ラベルを入力し、動詞の活用形を変換するプログラムです",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)