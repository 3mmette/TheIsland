# **The Island**

***User Manual***

***Emmette Taylor | Applied Python Programming | Semester 3, 2023***

## **Introduction**

Welcome to The Island, a text based adventure game where you must find a way back to civilisation after finding yourself stranded on a mysterious island.  
This document is intended to provide users with all the required information to install and play the game.  
Any errors or mistakes found within this documentation or game may be sent to the author of this document, Emmette Taylor.

## **System Requirements**

This program should work on all modern operating systems.  
To run the game, it is a requirement to have the Python 3 interpreter installed on your computer.  
It can be downloaded from following website:  
https://www.python.org/downloads/   
Choose the latest version for your operating system and follow the prompts.  
You will also need the game files. Download the zipped game from GitHub and extract them to an easily accessible folder.


## **Starting the Game**

Navigate so that you are in the TheIsland folder.    
Left-click on the address bar at the top of the screen and copy the address.   
Search your computer for command prompt and open it.   
In the command line, type: cd (paste the copied address) - then press enter.  
Use the following command to start the game: python the_island.py

## **Overview**
You awake on a small boat tied to a jetty on The Island, and rescue can't come to you, so you're going to have to help yourself.  
The boat you are on doesn't seem to be working, so you're going to have to get it working or find some other way to escape.  
Check the dashboard on the boat to see what you need to get working to start the boat.  
The Island itself is surrounded by harsh ocean so swimming won't work. If you enter the water, it's certain death.  
The only things you have with you are an empty bag and a blank chart that will be filled in as you explore The Island.  
You have full energy and hydration for now, but that won't last long. Find things to eat and drink if you want to keep moving and survive. 

## **Specializations**

Everyone is good at something. At the start of the game you will be given a choice of four specializations that will give you different abilities on The Island.

>### **Strength**
>
>By default, you are only able to carry five things with you in your bag.  
 By specializing in strength, you will now be able to carry ten.

>### **Dexterity**
>
>By default, every time you move to a new location, you lose a point from your energy and hydration reserves.  
By specializing in dexterity, you will now lose a point of energy and hydration every second move.

>### **Charisma**
>
>Interacting with other beings can be hard if you don't know what they want.  
By specializing in charisma, you may not need to have to exact item to get help, discovered everything to display options, and even might get extra chances at puzzles.

>### **Intelligence**
>
>The Island is an unknown land, but that doesn't mean you have to go in blind.  
By specializing in intelligence, you can now see the energy and hydration values for all items.

## **Actions**

There are five actions that take a single keyword / letter command as an input.

>### **Help (H)**
>  
>Sometimes when you're on an adventure, you may forget what you are meant to be doing or what you can actually do. If you don't want to open this manual again, you can use the 'Help' or 'H' command. This will bring up a conversation in game that should be able to help and get you going again.  
Type 'Help' or 'H', followed by the [ENTER] key.

>### **Refresh (R)**
>
>Adventuring can be confusing, especially in the text based environment, as sometimes the information can just pile up. If at any point you would like to clean the screen up and reprint all the information about the location again, use the 'Refresh' or 'R' command.  
Type 'Refresh' or 'R', followed by the [ENTER] key.

>### **Bag (B)**  
>
>You will need to carry things around while adventuring on The Island. You have a bag with you that is able to store items. If there is room in your bag, and you take an item, it will be stored here for later use. You can use the 'Bag' or 'B' command to open you bag and see how many items are in it, and what they are. You can use items while they are in your bag.  
Type 'Bag' or 'B', followed by the [ENTER] key.

>### **Chart (C)**
>
>You will be exploring the unknown lands of The Island and have a chart to show you where you are on The Island, and what is around you. As you move around more location names will be revealed. You can open the chart and look at its contents by using the 'Chart' or 'C' command.  
Type 'Chart' or 'C', followed by the [ENTER] key.

>### **Quit (Q)**
>
>Sometimes it all gets too much on The Island, or you need to leave the adventure. You can use the 'Quit' or 'Q' command to leave the game.    
Type 'Quit' or 'Q', followed by the [ENTER] key.

There are eight commands that require the dual input of an action and a noun, with a space separating them.

>### **Move (M) + Cardinal Direction** 
>
>You will need to move around The Island to discover items and places that will help you escape. Each location will provide a brief description of what is located around you, and it is up to you to choose which direction to move in. Cardinal directions, like on a compass, are used to choose which way to go. You will use the 'Move' or 'M' command followed by the cardinal direction.  
Type 'Move' or 'M', followed by either 'North' or 'N', 'East' or 'E', 'South' or 'S' or 'West' or 'W', followed by the [ENTER] key.

The remaining dual input commands are used with an interactive noun in the game. These nouns are written in ***ALL CAPITAL LETTERS***. You can use the following commands on them, depending on what they are.  

>### **Look (L) + Capitalized Noun**
>
>You will need to gain information on your surroundings to be able to get off The Island. All nouns written in capital letters can have the 'Look' or 'L' command used on them. This will give you more information on the noun and may also reveal other things.  
Type 'Look' or 'L', followed by the 'Capitalized Noun', followed by the [ENTER] key.

>### **Interact (I) + Capitalized Noun**
>
>You will need to interact with your surroundings to be able to get off The Island. Interactions can come in many forms, whether you want to use an item you have in your bag with an object in front of you, enter a code or do anything with an object, you will use the 'Interact' or 'I' command. There will be a hint in the description if you are able to interact with an item.  
Type 'Interact' or 'I', followed by the 'Capitalized Noun', followed by the [ENTER] key.

>### **Open (O) + Capitalized Noun**
>
>You may have to open things to be able to get off The Island. When you use the 'Look' command on an object, you may be told that is closed. Use the 'Open' or 'O' command to open whatever it is, if it isn't locked.  
Type 'Open' or 'O', followed by the 'Capitalized Noun', followed by the [ENTER] key.

>### **Take (T) + Capitalized Noun**
>
>You have a bag with you and are going to need to take things with you to different locations to be able to get off The Island. Use the 'Take' or 'T' command to take the item and place it in your bag.  
Type 'Take' or 'T', followed by the 'Capitalized Noun', followed by the [ENTER] key.

>### **Drop (D) + Capitalized Noun**
>
>You have a bag with you, and sometimes you realize you don't need an item anymore or wish to make space for something more important. Use the 'Drop' or 'D' command to drop the item. Don't worry, it will remain in the location where you left it if you want to pick it up again.
Type 'Drop' or 'D', followed by the 'Capitalized Noun' which is in your bag, followed by the [ENTER] key.

>### **Speak (S) + Capitalized Noun of Non Player Character**
>
>Other beings inhabit The Island, who may help or inhibit your attempt to escape. There will be a hint that they can speak, and you can use the 'Speak' or 'S' command to start a conversation with them.  
Type 'Speak' or 'S', followed by the 'Capitalized Noun of Non Player Character', followed by the ENTER key.

>### **Eat (E) + Capitalized Noun**
>
>Adventuring can be exhausting, and unless you're light on your feet, you're going to need to eat and drink often. You will find items that you can eat to refuel your energy and stay hydrated. But be warned, not everything you can eat and drink should be eaten or drunk. Use the 'Eat' or 'E' command to eat or drink an edible item.  
Type 'Eat' or 'E', followed by the 'Capitalized Noun', followed by the ENTER key.

## **Conclusion**
Get off The Island, alive. It's that simple.
