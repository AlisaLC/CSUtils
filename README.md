# Counter Strike 2 Utils
## CS2 Match Downloader
You can easily downlod your CS2 matches with your share code using the following command

`python download.py CSGO-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX`

the resulting demo will be saved in `demos` directory.

## CS2 Match Analyzer
You can analyze your matches with `DemoAnalyzer` class. By using `demoparser2` library, we can parse CS2 matches and analyze anything we want in python. The class only features grenade data extraction, but a lot more can and will be added soon. By using the following command, all the grenades thrown in the game will be stored in `results/grenades.csv` and a plot for grenades thrown in each map will be generated in the `results` directory.

`python analyze.py demos/[your_demo.dem]`