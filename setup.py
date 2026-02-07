import setuptools #type:ignore

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME="MEDICAL_CHATBOT_RAG_SYSTEM"
AUTHOR_USER_NAME="Chamika-Dilshan-Anuruddha"
AUTHOR_USER_EMAIL="anuruddhaedcd@gmail.com"
SRC_REPO="MedicalChatbot"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_USER_EMAIL,
    description="A medical chatbot for know simple medical informations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)