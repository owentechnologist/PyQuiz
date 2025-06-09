# This is a simple python program for creating quizzes.


## Python-preparation Steps for running the program on your machine:



1. Create a virtual environment:

```
python3 -m venv Quiz
```

2. Activate it:  [This step is repeated anytime you want this venv back]

```
source Quiz/bin/activate
```

On windows you would do:

```
Quiz\Scripts\activate
```
If no permission in Windows
 The Fix (Temporary, Safe, Local):
In PowerShell as Administrator, run:
```

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
Then confirm with Y when prompted.



## Python will utilize this requirements.txt in the project:

```
psycopg[binary]

```

3. Install the libraries: [only necesary to do this one time per environment]

```
pip3 install -r requirements.txt
```
4. To start the program using a local file, do the following:
```
python Quiz.py <name of file> 
```
Example:
```
python Quiz.py Geography1.tsv
```

## Hint: If you want to create your own Quiz, you can ask ChatGPT the following prompt:
```
The following is an example of types of questions. (fill in the blank) questions and (T or F) questions. 
Using the format in the following, generate a sample of 20 questions regarding 
"any topic" 
without any numeric reference at the beginning of each line, randomly alternate between different types of question.

Most terms in Ballet are from the ______ language (fill in the blank)~french 
Alton Brown has good recipes (T or F)~T 
Brothers are a blessing (T or F)~T
_______ helps clean teeth when applied to a toothbrush (fill in the blank)~toothpaste
```
## Use any topic of interest and add any restrictions you wish regarding age of user, etc.
