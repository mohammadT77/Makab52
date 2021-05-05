# PIP freeze & requirements.txt

You can simply export a list of your project requirements using command:  
`pip freeze > {your_target_file}`  
(usually `requirements.txt` or `reqs.txt`)

Try it!  
Then you see a list of package names into the file == version

It's completely Human-Readable and also Python Readable.  

So you can use `-r` option to use the file to install or upgrade your packages.  
`pip install -r {your-req-file}`

OK, Now try to install my screen_shot.py project requirements to run it!
