#StackStorm Chuck Norris Pack

## About

Retrieve Chuck Norris quotes from the [Internet Chuck Norris DataBase](http://www.icndb.com/)

## Install

To install the Chuck Norris pack, run:
```
st2 run packs.install repo_url=tuxinvader/st2_chuck subtree=true packs=chuck
```

To uninstall the pack:
```
st2 run packs.uninstall packs=chuck
```

## Usage

To get your quotes, execute `st2 run chuck.get_chuck`  

For Example:
```
me@texas:/home/stanley$ st2 run chuck.get_chuck
.
id: 580516f07c1d960d3cec6ed9
status: succeeded
parameters: None
result: 
  exit_code: 0
  result: The truth will set you free. Unless Chuck Norris has you, in which case, forget it buddy!
  stderr: ''
  stdout: ''
me@texas:/home/stanley$
```

