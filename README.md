# color-solver
My first Sikuli project. A simple [The Color!](http://game.ioxapp.com/color/) solver written in Sikuli (Python)

Environment
----------
Developed on Ubuntu Linux 14.04 (run in Windows 7 with VMware Workstation 10.0.1)  

* Host Machine
  + OS : Windows 7 64bit
  + CPU : Intel(R)Core(TM) i5 CPU 650 @ 3.20 GHz

* Guest Machine
  + OS : Ubuntu Linux 14.04 32bit
  + Browser : FireFox 31.0
  + Resolution : 1920 * 1680

Development Tools
------------
* [Sikuli 1.0.1](http://www.sikuli.org/)
  + [Java 7](http://openjdk.java.net/)
  + [OpenCV 2.4.9](http://opencv.org/)
  + [Python 2.7.6](https://www.python.org/) 
  

Demo
--------
Here's the [video](https://drive.google.com/file/d/1gLx5Rek4FMFJaGMF4j7wDpXBtDM2vfmK/view?usp=sharing)

On average, the program can solve about 100 levels per minute.  
(Since the CPU have to handle the recording, it was slightly slower than its average speed in the video)


BTW
------
You can easily beat the game by using the following JavaScript code:  
`$( "#box span" ).each(function() {
          $( this ).click();
});`
 


