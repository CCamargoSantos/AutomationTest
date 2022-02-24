# Search Validation
It contains a python script that runs the requested assignment for the QA automation process

It tried to do as follows:
1. Go to https://www.microsoft.com/es-mx/
2. Go to Windows
3. Go to Search
4. Search for “Xbox” and click on "Comprar"
5. Once in the result page you will see "Aplicaciones" click on it
6. Count the elements on the first 3 pages and print the sum of elements and all the titles
7. Go back to the first page and select the first NON-FREE option and STORE the price for later comparison
8. If you see a "Registration" pop up, close it
9. In this page, you will see the price again, compare first price vs current prince and they should match
10. Click on the "3 dot" button next to "Comprar" button and add the item to the CART
11. Verify the app takes you to the Shopping Cart page and verify you have one element available
12. Delete the item and verify you have 0 elements: "Tu carro está vacío" message should be present


## Getting Started
---
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
python3 dice 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Search_Validation.py (Automation script structure)
+-- chromedriver.exe      (Critical driver for chrome)             
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Python installed selenium (full) package
* Python installed keyboard (full) package
* chromedriver.exe (must be in the same folder of the runing script)

## Authors
---
* Camilo Camargo
