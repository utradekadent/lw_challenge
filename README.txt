INTRODUCTION
-------------------------------
The technical basis for the solution which addresses core use cases and handling multi-language UI tests is Playwright and Pytest (Python).

The main use cases are covered by four (core) tests:
	- test_copy_paste_translation.py
	- test_file_translation.py
	- test_settings_persistence.py
	- test_swap_languages.py

There is also a 'conftest.py' file containing shared fixtures, as well as a Page Object Model called 'translator.py'.

The 'source_text.docx' from the 'test_files' folder is needed for 'test_file_translation' to succeed.

The provided config file 'pytest.ini' is used to specify test paths, fixture markers, and nothing else.

The 'test_homepage.py' is an example of how multi-language UI testing can be handled using parametrisation. It comes with its own 'conftest.py'.




DIRECTORY STRUCTURE
-------------------------------

lw_challenge/
├── extra_tests/
│   ├── i18n/
│   │   ├── da.json
│   │   ├── de.json
│   │   ├── en.json
│   │   ├── es-es.json
│   │   └── fr-fr.json
│   ├── conftest.py
│   └── test_homepage.py
├── pages/
│   ├── __init__.py
│   └── translator.py
├── test_files/
│   └── source_text.docx
├── tests/
│   ├── __init__.py
│   ├── confttest.py
│   ├── test_copy_paste_translation.py
│   ├── test_file_translation.py
│   ├── test_settings_persistence.py
│   └── test_swap_languages.py
├── pytest.ini
├── README.txt
└── requirements.txt


INSTALLATION
-------------------------------

	WINDOWS (tested against Win 10 and 11 Home)
	
	1.	Install Python.

		a. Visit the official page for Python https://www.python.org/downloads/ on the Windows operating system. Locate a reliable version of Python 3, preferably 3.13.3, which was used in creating this solution. Choose the correct link for your device from the options provided: either Windows installer (64-bit) or Windows installer (32-bit) and proceed to download the executable file.
	
		b. Once you have downloaded the installer, open the .exe file, such as python-3.13.3-amd64.exe, by double-clicking it to launch the Python installer. 
			
		c. Check 'Add python.exe to PATH'.
			
		c. After Clicking the 'Install Now' button the setup will start installing Python on your Windows system.
			
		d. After completing the setup. Python will be installed on your Windows system. You will see a successful message.
			
		e. Open a command prompt (cmd) and run
			
			python --version
			
		to verify the Python installation in Windows.
			
			
	2.	Install required packages.
			
		a. Unzip 'lw_challenge.zip'.
			
		b. Right-click on the 'lw_challenge' directory and select 'Open in Terminal'.
			
		c. Run
				
			pip install -r .\requirements.txt
				
	3. 	Install Playwright browsers
				
		playwright install
					

	LINUX (Tested against Ubuntu 20.04 and 24.04)
	
	1.	Untar 'lw_challenge.tar.gz' and go to the root directory of the project. Then, open a terminal and run
		
		mkdir lw_challenge
		tar -xvf lw.challenge.tar.gz -C lw_challenge/
		cd lw_challenge/
			
	2.	Install pip
			
		sudo apt update
		sudo apt install python3-pip
			
	3.	Install required packages, ignoring pytest-retry (no matching distribution found for this package)
		
		grep -v 'unwanted-package-name' requirements.txt | pip install -r /dev/stdin
			
	4. Install Playwright browsers
	
		sudo playwright install-deps
		playwright install
	
	
	
		

RUNNING THE TESTS
-------------------------------

To execute the core tests, run

	pytest -s -k 'translator'

(The -s option is only needed for 'test_file_translation' to display load time-related information)
	
To execute the multi-langage UI test, run

	pytest -k 'homepage'
	
(I think this one will make more sense when I explain it during code walkthrough but feel free to give it a go!)


Or, execute all tests by simply running

	pytest -s
	
You can execute tests in verbose mode by adding the '-v' option, e.g.

	pytest -v -s -k 'translator'
	

NOTES
-------------------------------

1.	All tests will run in headed mode by default. To run in headless mode, comment out line #12 of the 'conftest.py' file.

2.	To slow down browser interactions (clicks, typing, and navigation), uncomment line #13 of the 'conftest.py' file.
	
3.	Although the framework support cross-browser testing, all tests will be executed in Chromium by default. This can be changed by modifying the parameter(s) in line #6 of the 'conftest.py' file.
	
The supported browsers are:
	- chromium
	- firefox
	- chrome
	- msedge
	- webkit (Safari)
	
4.	The tests seem pretty robust, however, when uploading doc files into the translator, I have seen an intermittent error "An unexpected error has occurred during the document translation.". I suspect it has to do with with Firebase request throttling (403 error). As a result, I have introduced a logic to retry 'test_file_translation' in case it fails. Pytest will re-execute it 3 times with 5-second intervals. If the test still fails, I reccomend switching to msedge as the test browser, as I had best results while using it.

GOOD LUCK!
