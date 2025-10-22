Lab Members
Prital Jariwala
Lucas Greer


1.
git clone git@github.com:my-name/my-imaginary-repo.git
cd my-imaginary-repo
touch my_second_file.py
nano my_second_file.py

git add my_second_file.py (or .)
git commit -m "added my_second_file)
git push


2.

We both created a repository for this lab, and pulled the files that we needed to edit into the VM through VSCode. After the files were finalized, I pushed it into the RPI using
scp. If i needed to change anything, I used nano until the files were in a working condition. Honestly, this workflow is the most efficient considering ease of use between platforms.

3. 

GrovePi uses I2C (Inter-Integrated-Circuit) protocols to communicate with the MCU on the RaspPi. When reading and writing, the GrovePi has a "hard-coded" 100ms delay for operations to 
make sure that all operations go through with accuracy. 

4.

The RaspberryPi itself does not have a method to performing ADC, so it cannot take the voltagees from the potentiometer.
The Atmega on the GrovePi does the analog conversions and then sends it to the RPi.

5.

I would first see what commands that I am using that manipulate the backlight in any way. 
If those aren't working I can start checking to make sure all modules are working (such as GrovePi itself).
i2c detect is one command that is useful for seeing what i2c connections are on the grovepi, which is applicable to the LCD
screen. I would also use the grovepi (.py) files such as the version check (bash firmware_version_check.sh or sudo python grovepi_check.py)





























