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



3. Python will utilize this requirements.txt in the project:

```
psycopg[binary]

```

4. Install the libraries: [only necesary to do this one time per environment]

```
pip3 install -r requirements.txt
```
5. To start the program using a local file, do the following:
```
python Quiz.py <name of file> 
```
Example:
```
python Quiz.py Geography1.tsv
```

## Hint: If you want to create your own Quiz, you can ask ChatGPt the following prompt:
```
Using the following as an example, 
generate a sample of 20 questions regarding 
"global geography" 
without any numeric reference at the beginning of each line and providing one word answers, T, F.

Most terms in Ballet are from the ______ language (fill in the blank)~french 
Alton Brown has good recipes (T or F)~T 
Brothers are a blessing (T or F)~T
```