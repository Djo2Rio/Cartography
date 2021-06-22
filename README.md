#             HOW TO USE CARTOGRAPHY ![](https://i.imgur.com/wCCrBms.png)




# Windows tutorial


First Step : 
- Download Neo4j Desktop at https://neo4j.com/download/.
- Install it and run it.
Now you should see a window like this one (without the Project and Project 1).
Click on the "New" button and a project call Project should appear.
Click on the "Add" button and select "Local DBMS" and choose the Name for the database and password that you want then click on "Create".

![](https://i.imgur.com/2ybJKZo.png)

Well Done ! You have complete the first Neo4j part !


Next you should have the Cartography.zip file.
Create a folder name Cartography_unzip and unzip it in this one.

Next step :  
- For this step you should have python 3.9. You can download it at https://www.python.org/downloads/.
- In the file explorator go to the folder Cartography_unzip click on it. The path should look like this .../Cartography_zip/Cartography.
- Go on the "file" button and click on "open with Windows Powershell" and open it without admin right.
- In this window type this command ``python3 -m venv tutorial-env``
Wait for it to be executed then type ``tutorial-env\Scripts\activate.bat``
- Finally type ``python -m pip install -r requirements.txt``
Well done you are almost done.
- To launch the program type :
 ``python .\main.py 'bolt://neo4j:{password}@localhost:7687'``. Replace password by the password that you choose before in the Neo4j step.(Don't forget to remove the '{' and '}').

Now you can go back to Neo4j and click on Open.
A window will appear and you should see the result of this cartography of Planete Solidaire.


## :rotating_light: Please note that you don't need to normalize the files, the programm will do it by itself.
# Advanced tutorial

If you are on linux you can run the project by typing ```python3 -m venv tutorial-env```, `source tutorial-env/bin/activate`, ` python -m pip install -r requirements.txt` in the terminal where the folder cartography is while Neo4j is running and after that you can launch the cartography with :
`python ./main.py 'bolt://neo4j:{password}@localhost:7687' `
Replace password by the password that you choose before in the Neo4j step. (Don't forget to remove the '{' and '}').
