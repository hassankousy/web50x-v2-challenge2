# WEB50X V2 - IP address classifier

Task resolution process:

* Fork the repo
* Clone the forked repo to your local machine
* Resolve the task
* Commit your solution
* Push to GitHub
* create a pull request


Important Note: No third party packages or libraries are allowed!

Build a command line tool that receives an IP address in the format: x.x.x.x/x, and print the class of the IP address.

Class resolution should contain the following information:
1. IP address class (A, B, C, D, E)
2. IP address designation (Private, Public, Special)

References:

[https://www.meridianoutpost.com/resources/articles/IP-classes.php](https://www.meridianoutpost.com/resources/articles/IP-classes.php)

[https://github.com/laith43d/ipcalculator-LZ-](https://github.com/laith43d/ipcalculator-LZ-)


python main.py 127.0.0.1/24

Output: Class: A, Designation: Special


python main.py 192.168.1.1/24

Output: Class: C, Designation: Private

### classes ranges
![classes](https://imgs.search.brave.com/DNOd3nUKB-4pvXGfC3xXwElemt62Q6nHza3mk6dHytc/rs:fit:1200:543:1/g:ce/aHR0cDovLzQuYnAu/YmxvZ3Nwb3QuY29t/Ly0teWkybnZGcGF0/NC9VLTNkOEdCOUt2/SS9BQUFBQUFBQU5v/by9FamZKSUhpOGpN/NC9zMTYwMC9DbGFz/c2VzJTJCb2YlMkJJ/UC5wbmc)

### Private ranges
![private](https://imgs.search.brave.com/xhh4iYaT6-_6URHHfH6RFm-8rZvhe3bl54X70FAiPKo/rs:fit:1100:741:1/g:ce/aHR0cDovL3d3dy5s/b2dpY3VtLmNvL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDE2LzA4/L1ByaXZhdGUtSVAt/QWRkcmVzcy0xLnBu/Zw)
