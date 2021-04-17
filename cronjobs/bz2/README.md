## About

`SourceQuery.py` is an implementation of the Source Query protocol compatible Python 2.6. It has been made by Andreas Klauer.

It's available here : https://github.com/frostschutz/SourceLib

## Why

Since our main website is using phpBB, we could've have written an extension for phpBB using the `PHP Source Query` library. Thus, at each connection to the phpBB application, we would have launched a request to our dedicated server to retrieve the information.

We preferred to use a Python script launched by a cronjob for these main reasons: 

- Have an extra layer of security: the script is launched by the server and is jailed.
- Allows for greater scalability: you don't have to worry about the structure of phpBB, you can do whatever you want
- Once the client connects to the site, the recovery of data from the servers is done exclusively on his side in Ajax
