# Surfs Up

## Overview of the Analysis

After a recent trip to Hawaii, we conceived the idea of setting up a surf and shake shop in Oahu. Our friend, W. Avy, has provided us with weather data in a *SQLite* database named *"hawaii.sqlite"*. He has suggested we use this dataset to analyze the weather before we embark in our entrepreneurial venture.

We are concerned about the amount of precipitation on Oahu, since there needs to be enough rain to keep everything green, but not so much that you lose out on that ideal surfing and ice cream weather.

After ensuring that we had full access to the dataset and the ability to query the precipitation and temperature statistics with the correct date formats, our analysis focused on comparing the key differences in weather between June and December, to determine if the surf and ice cream shop business is sustainable year-round. We also propose two recommendations we wish to explote in order to further fine-tune this analysis.

## Methodology

To conduct the analysis, we utilized our experience with *Pandas* and *Numpy*, as well as *Matplotlib* and *Datetime* to run the necessary queries, generate dataframes from the results, and plot the data graphically. In addition, we employed *SQLAlchemy* to access, map and explore the *SQLite* dataset using *Jupyter Notebook*. The data for June and December is presented as summary statistics.

## Results

The following table presents the summary temperature statistics for the month of June:

![June statistics](Resources/June_stats.png)

The following table presents the summary temperature statistics for the month of December:

![December statistics](Resources/December_stats.png)

To better complement the interpretation of these tables, we present the following histograms of temperature distribution for both months:

![June histogram](Resources/June_histogram.png)

![December histogram](Resources/December_histogram.png)

As can be observed from the tables and the graphs, there are three main takeaways from our analysis:

* The average temperature for both months is only a few degrees different, with June temperatures averaging 74.9 degrees F and December temperatures averaging 71.0 degrees F.

* Even in December, temperatures can reach a balmy 83.0 degrees F.

* Temperatures in June are subject to more variability (i.e., they are spread more broadly around the mean), than temperatures in December. Nevertheless, 95% of the time, June temperatures range between 68.4 degrees F and 81.5 degrees F (i.e. two standard deviations from the mean temperature), while 95% of the time, December temperatures range between 63.5 degrees F and 78.5 degrees F.

## Summary and Recommendations

Based on the temperature statistics obtained above, Oahu weather seems relatively consistent year-round, with average temperatures and expected temperature ranges well within the weather window for the surf and shake business.

The Hawaiian islands are well known for their micro-climates, with weather also varying significantly between the windward and leeward shores.

In order to further our analysis and make a better location choice for our business, we would like to repeat our statistics but this time by weather station. First, we would repeat the temperature statistics dataframe for each station and compare them. Second, we would also conduct a precipitation statistic for each station. That way, we can choose a location that has the best temperatures combined with the least precipitation.