
# Counter-Strike 2 Utilities Documentation
Welcome to the Counter-Strike 2 Utilities repository, a comprehensive toolkit designed to enhance your Counter-Strike 2 gameplay experience through advanced match downloading and analytical capabilities. This document provides detailed instructions on utilizing the two primary features of this toolkit: the CS2 Match Downloader and the CS2 Match Analyzer.

## CS2 Match Downloader
The CS2 Match Downloader allows users to efficiently retrieve their Counter-Strike 2 match demos using a share code. This utility simplifies the process of downloading and storing match demos for later analysis or viewing.

### Usage Instructions
To download a match, execute the following command in your terminal:
```shell
python download.py CSGO-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
```
Upon successful execution, the downloaded demo will be stored within the `demos` directory for easy access.

### Dependencies and Configuration
* The parsing of match share codes utilizes the algorithm provided by [akiver/csgo-sharecode](https://github.com/akiver/csgo-sharecode).
* Boiler, essential for demo downloading on Windows, can be obtained from [akiver/boiler-writer](https://github.com/akiver/akiver/boiler-writer). Users may substitute this with any compiled version of their choice by adjusting the invocation within download.py accordingly.

## CS2 Match Analyzer
The CS2 Match Analyzer empowers users to conduct in-depth analyses of their Counter-Strike 2 matches. Leveraging the `demoparser2` library, this tool provides insights into match dynamics, with a current focus on grenade usage.

### Features
* **Grenade Data Extraction**: Extract detailed information about grenade usage within a match, facilitating tactical analysis and strategy development.

### Analyzing a Match
To analyze grenade data from a match demo, utilize the following command:
```shell
python analyze.py demos/[your_demo.dem]
```
The analysis results, including grenade usage data, will be output to `results/grenades.csv`. Additionally, a visual representation of grenade throws across different maps will be generated within the `results` directory.

### Additional Resources
Map imagery and scaling information are acquired from [pnxenopoulos/awpy](https://github.com/pnxenopoulos/awpy), ensuring accurate representation and analysis.