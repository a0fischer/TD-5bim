# TD-5bim

Practical work for 5BiM projects

## Goal of this project

runsphere.py is a python script that can display properties of a sphere based on its radius. 

## Installation instructions

Simply, download this git repository. 

Unzip the tarball by using command: ```unzip tarball.zip```

## How to use it ?

Basic command is :```python2 runsphere.py radius```
where you must write the radius you want for your sphere

Then, there are multiple parameters that you can use for displaying different sphere properties : 
- -v : display the volume
- -s : display the surface
- -d : display the diameter
- --load : load a sphere from file
- --save : save the sphere into a file

## Examples

The command:

```python2 runsphere.py 10```

Will return: 

```
  Sphere(10.0)
  radius is 10.0
```

Another command: 

```python2 runsphere.py 10 -v -s -d```

Will return: 

```
  Sphere(10.0)
  radius is 10.0
  volume is 3141.6
  surface is 1256.64
  diameter is 100.0
```

## Documentation

Some documentation is available here : https://a0fischer.github.io/TD-5bim/

## Contributors

Aurélie Fischer, Miléna Kaag, David Parsons

